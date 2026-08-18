"""
Pytest test suite for the Linguist application.

Covers positive and negative CRUD scenarios for the User, Deck, and Card
models, using fixtures to set up and tear down an isolated SQLite database
for every test run.
"""

from __future__ import annotations

import os

import pytest

import linguist as lg

DB_FILE = "linguist.db"


@pytest.fixture(autouse=True)
def clean_db():
    """Start every test from a clean, freshly initialised database.

    The engine's connection pool is disposed before removing the SQLite
    file so that no stale, already-open connections keep pointing at the
    unlinked (deleted) file on disk.
    """
    lg.engine.dispose()
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    lg.init_db()
    yield
    lg.engine.dispose()
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)


@pytest.fixture
def user() -> lg.User:
    return lg.user_create("Alice", "alice@example.com", "password123")


@pytest.fixture
def deck(user: lg.User) -> lg.Deck:
    return lg.deck_create("Basic Verbs", user.id)


# --------------------------------------------------------------------------- #
# User CRUD
# --------------------------------------------------------------------------- #

def test_user_create():
    user = lg.user_create("Alice", "alice@example.com", "password123")
    assert user.id is not None
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    # password must never be stored in plain text
    assert user.password_hash != "password123"
    assert user.check_password("password123")


def test_user_get_by_id(user: lg.User):
    fetched = lg.user_get_by_id(user.id)
    assert fetched is not None
    assert fetched.name == "Alice"


def test_user_get_by_id_not_found():
    assert lg.user_get_by_id(999_999) is None


def test_user_update_name(user: lg.User):
    updated = lg.user_update_name(user.id, "Alicia")
    assert updated.name == "Alicia"
    assert lg.user_get_by_id(user.id).name == "Alicia"


def test_user_update_name_not_found():
    assert lg.user_update_name(999_999, "Ghost") is None


def test_user_change_password_wrong_old_password(user: lg.User):
    assert lg.user_change_password(user.id, "wrong_password", "newpass") is False


def test_user_change_password_success(user: lg.User):
    assert lg.user_change_password(user.id, "password123", "newpass") is True
    assert lg.user_change_password(user.id, "newpass", "another") is True


def test_user_delete_by_id(user: lg.User):
    assert lg.user_delete_by_id(user.id) is True
    assert lg.user_get_by_id(user.id) is None
    assert lg.user_delete_by_id(user.id) is False


def test_user_create_duplicate_email(user: lg.User):
    with pytest.raises(lg.DuplicateEmailError):
        lg.user_create("Someone Else", "alice@example.com", "otherpass")


@pytest.mark.parametrize(
    "name, email, password",
    [
        ("", "alice@example.com", "password123"),
        ("Alice", "", "password123"),
        ("Alice", "not-an-email", "password123"),
        ("Alice", "alice@example.com", ""),
        ("   ", "alice@example.com", "password123"),
    ],
)
def test_user_create_invalid_data(name, email, password):
    with pytest.raises(lg.ValidationError):
        lg.user_create(name, email, password)


# --------------------------------------------------------------------------- #
# Deck CRUD
# --------------------------------------------------------------------------- #

def test_deck_create(user: lg.User):
    deck = lg.deck_create("Basic Verbs", user.id)
    assert deck.id is not None
    assert deck.name == "Basic Verbs"
    assert deck.user_id == user.id


def test_deck_create_nonexistent_user():
    with pytest.raises(lg.NotFoundError):
        lg.deck_create("Orphan Deck", 999_999)


def test_deck_create_invalid_name(user: lg.User):
    with pytest.raises(lg.ValidationError):
        lg.deck_create("", user.id)


def test_deck_get_by_id(deck: lg.Deck):
    fetched = lg.deck_get_by_id(deck.id)
    assert fetched is not None
    assert fetched.name == "Basic Verbs"


def test_deck_get_by_id_not_found():
    assert lg.deck_get_by_id(999_999) is None


def test_deck_update(deck: lg.Deck):
    updated = lg.deck_update(deck.id, "Advanced Verbs")
    assert updated.name == "Advanced Verbs"


def test_deck_update_not_found():
    assert lg.deck_update(999_999, "Ghost Deck") is None


def test_deck_delete_by_id(deck: lg.Deck):
    assert lg.deck_delete_by_id(deck.id) is True
    assert lg.deck_get_by_id(deck.id) is None
    assert lg.deck_delete_by_id(deck.id) is False


# --------------------------------------------------------------------------- #
# Card CRUD
# --------------------------------------------------------------------------- #

def test_card_create(user: lg.User, deck: lg.Deck):
    card = lg.card_create(user.id, deck.id, "cat", "кіт", "Think of a small furry animal.")
    assert card.id is not None
    assert card.word == "cat"
    assert card.translation == "кіт"
    assert card.deck_id == deck.id
    assert card.user_id == user.id


def test_card_create_nonexistent_user(deck: lg.Deck):
    with pytest.raises(lg.NotFoundError):
        lg.card_create(999_999, deck.id, "cat", "кіт")


def test_card_create_nonexistent_deck(user: lg.User):
    with pytest.raises(lg.NotFoundError):
        lg.card_create(user.id, 999_999, "cat", "кіт")


def test_card_create_deck_belongs_to_other_user(user: lg.User, deck: lg.Deck):
    other_user = lg.user_create("Bob", "bob@example.com", "secretpw")
    with pytest.raises(lg.ValidationError):
        lg.card_create(other_user.id, deck.id, "cat", "кіт")


@pytest.mark.parametrize("word, translation", [("", "кіт"), ("cat", "")])
def test_card_create_invalid_data(user: lg.User, deck: lg.Deck, word, translation):
    with pytest.raises(lg.ValidationError):
        lg.card_create(user.id, deck.id, word, translation)


def test_card_get_by_id(user: lg.User, deck: lg.Deck):
    card = lg.card_create(user.id, deck.id, "cat", "кіт")
    fetched = lg.card_get_by_id(card.id)
    assert fetched is not None
    assert fetched.word == "cat"


def test_card_get_by_id_not_found():
    assert lg.card_get_by_id(999_999) is None


def test_card_update(user: lg.User, deck: lg.Deck):
    card1 = lg.card_create(user.id, deck.id, "cat", "кіт", "Think of a small furry animal.")
    card2 = lg.card_create(user.id, deck.id, "dog", "собака", "Man's best friend.")

    updated = lg.card_update(card1.id, tip="A domestic feline.")
    assert updated.tip == "A domestic feline."
    assert updated.word == "cat"  # unchanged fields stay the same

    updated2 = lg.card_update(card2.id, word="puppy", translation="цуценя")
    assert updated2.word == "puppy"
    assert updated2.translation == "цуценя"


def test_card_update_not_found():
    assert lg.card_update(999_999, word="ghost") is None


def test_card_update_invalid_data(user: lg.User, deck: lg.Deck):
    card = lg.card_create(user.id, deck.id, "cat", "кіт")
    with pytest.raises(lg.ValidationError):
        lg.card_update(card.id, word="")


def test_card_filter(user: lg.User, deck: lg.Deck):
    lg.card_create(user.id, deck.id, "cat", "кіт", "A domestic feline.")
    lg.card_create(user.id, deck.id, "dog", "собака", "Man's best friend.")
    lg.card_create(user.id, deck.id, "catalog", "каталог", "A list of items, contains 'cat'.")

    results = lg.card_filter("cat")
    words = {c.word for c in results}
    assert "cat" in words
    assert "catalog" in words
    assert "dog" not in words

    results_tip = lg.card_filter("feline")
    assert len(results_tip) == 1
    assert results_tip[0].word == "cat"

    assert lg.card_filter("xyz_no_match") == ()


def test_card_delete_by_id(user: lg.User, deck: lg.Deck):
    card = lg.card_create(user.id, deck.id, "cat", "кіт")
    assert lg.card_delete_by_id(card.id) is True
    assert lg.card_get_by_id(card.id) is None
    assert lg.card_delete_by_id(card.id) is False


def test_deck_delete_cascades_cards(user: lg.User, deck: lg.Deck):
    card = lg.card_create(user.id, deck.id, "cat", "кіт")
    assert lg.deck_delete_by_id(deck.id) is True
    assert lg.card_get_by_id(card.id) is None

