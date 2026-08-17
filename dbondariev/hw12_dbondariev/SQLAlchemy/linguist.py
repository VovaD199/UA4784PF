"""
Linguist - a simple language learning application.

The application allows users to create decks of flashcards. Each flashcard
contains an English word, its Ukrainian translation and a tip to help the
user remember it.

Models: User, Deck, Card.
CRUD functions are provided for each model.
"""

from __future__ import annotations

from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
    relationship,
)


class Base(DeclarativeBase):
    """Base class for all ORM models."""


class User(Base):
    """A user of the Linguist application."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    decks: Mapped[list["Deck"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    cards: Mapped[list["Card"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"


class Deck(Base):
    """A deck of flashcards belonging to a user."""

    __tablename__ = "decks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="decks")

    def __repr__(self) -> str:
        return f"Deck(id={self.id!r}, name={self.name!r}, user_id={self.user_id!r})"


class Card(Base):
    """A single flashcard: an English word, its Ukrainian translation and a tip."""

    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    word: Mapped[str] = mapped_column(String(255), nullable=False)
    translation: Mapped[str] = mapped_column(String(255), nullable=False)
    tip: Mapped[str] = mapped_column(String(500), nullable=True)

    user: Mapped["User"] = relationship(back_populates="cards")

    def __repr__(self) -> str:
        return (
            f"Card(id={self.id!r}, word={self.word!r}, "
            f"translation={self.translation!r}, tip={self.tip!r})"
        )



engine = create_engine("sqlite:///linguist.db")
Session = sessionmaker(bind=engine)


def init_db() -> None:
    """Create all tables in the database."""
    Base.metadata.create_all(engine)



def user_create(name: str, email: str, password: str) -> User:
    """Create a new user and return the User object."""
    with Session() as session:
        user = User(name=name, email=email, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        session.expunge(user)
        return user


def user_get_by_id(user_id: int) -> User | None:
    """Retrieve a user by their ID and return the User object."""
    with Session() as session:
        user = session.get(User, user_id)
        if user is not None:
            session.expunge(user)
        return user


def user_update_name(user_id: int, name: str) -> User | None:
    """Update the name of a user and return the updated User object."""
    with Session() as session:
        user = session.get(User, user_id)
        if user is None:
            return None
        user.name = name
        session.commit()
        session.refresh(user)
        session.expunge(user)
        return user


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """Change the password of a user. Return True on success, False otherwise."""
    with Session() as session:
        user = session.get(User, user_id)
        if user is None or user.password != old_password:
            return False
        user.password = new_password
        session.commit()
        return True


def user_delete_by_id(user_id: int) -> bool:
    """Delete a user by their ID. Return True on success, False otherwise."""
    with Session() as session:
        user = session.get(User, user_id)
        if user is None:
            return False
        session.delete(user)
        session.commit()
        return True



def deck_create(name: str, user_id: int) -> Deck:
    """Create a new deck belonging to a user and return the Deck object."""
    with Session() as session:
        deck = Deck(name=name, user_id=user_id)
        session.add(deck)
        session.commit()
        session.refresh(deck)
        session.expunge(deck)
        return deck


def deck_get_by_id(deck_id: int) -> Deck | None:
    """Retrieve a deck by its ID and return the Deck object."""
    with Session() as session:
        deck = session.get(Deck, deck_id)
        if deck is not None:
            session.expunge(deck)
        return deck


def deck_update(deck_id: int, name: str) -> Deck | None:
    """Update the name of a deck and return the updated Deck object."""
    with Session() as session:
        deck = session.get(Deck, deck_id)
        if deck is None:
            return None
        deck.name = name
        session.commit()
        session.refresh(deck)
        session.expunge(deck)
        return deck


def deck_delete_by_id(deck_id: int) -> bool:
    """Delete a deck by its ID. Return True on success, False otherwise."""
    with Session() as session:
        deck = session.get(Deck, deck_id)
        if deck is None:
            return False
        session.delete(deck)
        session.commit()
        return True



def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """Create a new flashcard and return the Card object."""
    with Session() as session:
        card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
        session.add(card)
        session.commit()
        session.refresh(card)
        session.expunge(card)
        return card


def card_get_by_id(card_id: int) -> Card | None:
    """Retrieve a flashcard by its ID and return the Card object."""
    with Session() as session:
        card = session.get(Card, card_id)
        if card is not None:
            session.expunge(card)
        return card


def card_filter(sub_word: str) -> tuple[Card, ...]:
    """Retrieve all flashcards containing ``sub_word`` in the word,
    translation, or tip fields and return a tuple of Card objects."""
    with Session() as session:
        pattern = f"%{sub_word}%"
        cards = (
            session.query(Card)
            .filter(
                Card.word.like(pattern)
                | Card.translation.like(pattern)
                | Card.tip.like(pattern)
            )
            .all()
        )
        for card in cards:
            session.expunge(card)
        return tuple(cards)


def card_update(
    card_id: int,
    word: str | None = None,
    translation: str | None = None,
    tip: str | None = None,
) -> Card | None:
    """Update the fields of a flashcard and return the updated Card object."""
    with Session() as session:
        card = session.get(Card, card_id)
        if card is None:
            return None
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
        session.commit()
        session.refresh(card)
        session.expunge(card)
        return card


def card_delete_by_id(card_id: int) -> bool:
    """Delete a flashcard by its ID. Return True on success, False otherwise."""
    with Session() as session:
        card = session.get(Card, card_id)
        if card is None:
            return False
        session.delete(card)
        session.commit()
        return True


if __name__ == "__main__":
    init_db()

