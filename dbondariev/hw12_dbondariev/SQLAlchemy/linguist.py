"""
Linguist - a simple language learning application.

The application allows users to create decks of flashcards. Each flashcard
belongs to a deck and contains an English word, its Ukrainian translation
and an optional tip to help the user remember it.

Models: User, Deck, Card.
CRUD functions are provided for each model, together with input validation,
existence checks for related records and database error handling.
"""

from __future__ import annotations

import re
from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session as SessionType,
    mapped_column,
    relationship,
    sessionmaker,
)
from werkzeug.security import check_password_hash, generate_password_hash

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class LinguistError(Exception):
    """Base exception for all Linguist application errors."""


class ValidationError(LinguistError):
    """Raised when input data fails validation."""


class NotFoundError(LinguistError):
    """Raised when a referenced record does not exist."""


class DuplicateEmailError(LinguistError):
    """Raised when trying to create a user with an already used email."""


class Base(DeclarativeBase):
    """Base class for all ORM models."""


class User(Base):
    """A user of the Linguist application."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    decks: Mapped[list["Deck"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    cards: Mapped[list["Card"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"


class Deck(Base):
    """A deck of flashcards belonging to a user."""

    __tablename__ = "decks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="decks")
    cards: Mapped[list["Card"]] = relationship(back_populates="deck", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Deck(id={self.id!r}, name={self.name!r}, user_id={self.user_id!r})"


class Card(Base):
    """A single flashcard: an English word, its Ukrainian translation and a tip."""

    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    deck_id: Mapped[int] = mapped_column(ForeignKey("decks.id"), nullable=False)
    word: Mapped[str] = mapped_column(String(255), nullable=False)
    translation: Mapped[str] = mapped_column(String(255), nullable=False)
    tip: Mapped[str | None] = mapped_column(String(500), nullable=True)

    user: Mapped["User"] = relationship(back_populates="cards")
    deck: Mapped["Deck"] = relationship(back_populates="cards")

    def __repr__(self) -> str:
        return (
            f"Card(id={self.id!r}, deck_id={self.deck_id!r}, word={self.word!r}, "
            f"translation={self.translation!r}, tip={self.tip!r})"
        )


engine = create_engine("sqlite:///linguist.db")
Session = sessionmaker(bind=engine, expire_on_commit=False)


def init_db() -> None:
    """Create all tables in the database."""
    Base.metadata.create_all(engine)


@contextmanager
def session_scope() -> Iterator[SessionType]:
    """Provide a transactional scope around a series of operations.

    Commits on success, rolls back on any exception (re-raising it) and
    always closes the session. This removes the need to duplicate
    try/commit/rollback/close boilerplate in every CRUD function.
    """
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def _require_non_empty_str(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field_name!r} must be a non-empty string.")
    return value.strip()


def _require_email(email: str) -> str:
    email = _require_non_empty_str(email, "email")
    if not EMAIL_RE.match(email):
        raise ValidationError(f"{email!r} is not a valid email address.")
    return email


def _require_positive_int(value: int, field_name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValidationError(f"{field_name!r} must be a positive integer.")
    return value


# --------------------------------------------------------------------------- #
# User CRUD
# --------------------------------------------------------------------------- #

def user_create(name: str, email: str, password: str) -> User:
    """Create a new user and return the User object."""
    name = _require_non_empty_str(name, "name")
    email = _require_email(email)
    password = _require_non_empty_str(password, "password")

    user = User(name=name, email=email, password_hash=generate_password_hash(password))
    try:
        with session_scope() as session:
            session.add(user)
    except IntegrityError as exc:
        raise DuplicateEmailError(f"Email already registered: {email!r}") from exc
    return user


def user_get_by_id(user_id: int) -> User | None:
    """Retrieve a user by their ID and return the User object."""
    user_id = _require_positive_int(user_id, "user_id")
    with session_scope() as session:
        return session.get(User, user_id)


def user_update_name(user_id: int, name: str) -> User | None:
    """Update the name of a user and return the updated User object."""
    user_id = _require_positive_int(user_id, "user_id")
    name = _require_non_empty_str(name, "name")
    with session_scope() as session:
        user = session.get(User, user_id)
        if user is None:
            return None
        user.name = name
        return user


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """Change the password of a user. Return True on success, False otherwise."""
    user_id = _require_positive_int(user_id, "user_id")
    old_password = _require_non_empty_str(old_password, "old_password")
    new_password = _require_non_empty_str(new_password, "new_password")
    with session_scope() as session:
        user = session.get(User, user_id)
        if user is None or not user.check_password(old_password):
            return False
        user.set_password(new_password)
        return True


def user_delete_by_id(user_id: int) -> bool:
    """Delete a user by their ID. Return True on success, False otherwise."""
    user_id = _require_positive_int(user_id, "user_id")
    with session_scope() as session:
        user = session.get(User, user_id)
        if user is None:
            return False
        session.delete(user)
        return True


# --------------------------------------------------------------------------- #
# Deck CRUD
# --------------------------------------------------------------------------- #

def deck_create(name: str, user_id: int) -> Deck:
    """Create a new deck belonging to a user and return the Deck object."""
    name = _require_non_empty_str(name, "name")
    user_id = _require_positive_int(user_id, "user_id")
    with session_scope() as session:
        if session.get(User, user_id) is None:
            raise NotFoundError(f"User with id={user_id} does not exist.")
        deck = Deck(name=name, user_id=user_id)
        session.add(deck)
        session.flush()
        session.expunge(deck)
    return deck


def deck_get_by_id(deck_id: int) -> Deck | None:
    """Retrieve a deck by its ID and return the Deck object."""
    deck_id = _require_positive_int(deck_id, "deck_id")
    with session_scope() as session:
        return session.get(Deck, deck_id)


def deck_update(deck_id: int, name: str) -> Deck | None:
    """Update the name of a deck and return the updated Deck object."""
    deck_id = _require_positive_int(deck_id, "deck_id")
    name = _require_non_empty_str(name, "name")
    with session_scope() as session:
        deck = session.get(Deck, deck_id)
        if deck is None:
            return None
        deck.name = name
        return deck


def deck_delete_by_id(deck_id: int) -> bool:
    """Delete a deck by its ID. Return True on success, False otherwise."""
    deck_id = _require_positive_int(deck_id, "deck_id")
    with session_scope() as session:
        deck = session.get(Deck, deck_id)
        if deck is None:
            return False
        session.delete(deck)
        return True


# --------------------------------------------------------------------------- #
# Card CRUD
# --------------------------------------------------------------------------- #

def card_create(
    user_id: int,
    deck_id: int,
    word: str,
    translation: str,
    tip: str | None = None,
) -> Card:
    """Create a new flashcard belonging to a deck and return the Card object."""
    user_id = _require_positive_int(user_id, "user_id")
    deck_id = _require_positive_int(deck_id, "deck_id")
    word = _require_non_empty_str(word, "word")
    translation = _require_non_empty_str(translation, "translation")
    if tip is not None:
        tip = _require_non_empty_str(tip, "tip")

    with session_scope() as session:
        if session.get(User, user_id) is None:
            raise NotFoundError(f"User with id={user_id} does not exist.")
        deck = session.get(Deck, deck_id)
        if deck is None:
            raise NotFoundError(f"Deck with id={deck_id} does not exist.")
        if deck.user_id != user_id:
            raise ValidationError(
                f"Deck {deck_id!r} does not belong to user {user_id!r}."
            )
        card = Card(user_id=user_id, deck_id=deck_id, word=word, translation=translation, tip=tip)
        session.add(card)
        session.flush()
        session.expunge(card)
    return card


def card_get_by_id(card_id: int) -> Card | None:
    """Retrieve a flashcard by its ID and return the Card object."""
    card_id = _require_positive_int(card_id, "card_id")
    with session_scope() as session:
        return session.get(Card, card_id)


def card_filter(sub_word: str) -> tuple[Card, ...]:
    """Retrieve all flashcards containing ``sub_word`` in the word,
    translation, or tip fields and return a tuple of Card objects."""
    sub_word = _require_non_empty_str(sub_word, "sub_word")
    pattern = f"%{sub_word}%"
    stmt = select(Card).where(
        Card.word.like(pattern)
        | Card.translation.like(pattern)
        | Card.tip.like(pattern)
    )
    with session_scope() as session:
        return tuple(session.scalars(stmt).all())


def card_update(
    card_id: int,
    word: str | None = None,
    translation: str | None = None,
    tip: str | None = None,
) -> Card | None:
    """Update the fields of a flashcard and return the updated Card object."""
    card_id = _require_positive_int(card_id, "card_id")
    if word is not None:
        word = _require_non_empty_str(word, "word")
    if translation is not None:
        translation = _require_non_empty_str(translation, "translation")
    if tip is not None:
        tip = _require_non_empty_str(tip, "tip")

    with session_scope() as session:
        card = session.get(Card, card_id)
        if card is None:
            return None
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
        return card


def card_delete_by_id(card_id: int) -> bool:
    """Delete a flashcard by its ID. Return True on success, False otherwise."""
    card_id = _require_positive_int(card_id, "card_id")
    with session_scope() as session:
        card = session.get(Card, card_id)
        if card is None:
            return False
        session.delete(card)
        return True


if __name__ == "__main__":
    init_db()

