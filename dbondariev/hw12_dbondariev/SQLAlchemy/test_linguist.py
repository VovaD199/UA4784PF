"""
Test script for the Linguist application.

Runs a series of CRUD operations against the User, Deck, and Card models
and verifies expected behaviour using assert statements.
"""

import os

import linguist as lg


DB_FILE = "linguist.db"


def setup_db() -> None:
    """Start from a clean database for repeatable test runs."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    lg.init_db()


def test_user_crud() -> None:
    user = lg.user_create("Alice", "alice@example.com", "password123")
    assert user.id is not None
    assert user.name == "Alice"
    assert user.email == "alice@example.com"

    fetched = lg.user_get_by_id(user.id)
    assert fetched is not None
    assert fetched.name == "Alice"

    updated = lg.user_update_name(user.id, "Alicia")
    assert updated.name == "Alicia"
    assert lg.user_get_by_id(user.id).name == "Alicia"

    # wrong old password -> failure
    assert lg.user_change_password(user.id, "wrong_password", "newpass") is False
    # correct old password -> success
    assert lg.user_change_password(user.id, "password123", "newpass") is True

    assert lg.user_get_by_id(999999) is None

    assert lg.user_delete_by_id(user.id) is True
    assert lg.user_get_by_id(user.id) is None
    assert lg.user_delete_by_id(user.id) is False

    print("User CRUD tests passed.")


def test_deck_crud() -> None:
    user = lg.user_create("Bob", "bob@example.com", "secret")

    deck = lg.deck_create("Basic Verbs", user.id)
    assert deck.id is not None
    assert deck.name == "Basic Verbs"
    assert deck.user_id == user.id

    fetched = lg.deck_get_by_id(deck.id)
    assert fetched is not None
    assert fetched.name == "Basic Verbs"

    updated = lg.deck_update(deck.id, "Advanced Verbs")
    assert updated.name == "Advanced Verbs"

    assert lg.deck_get_by_id(999999) is None

    assert lg.deck_delete_by_id(deck.id) is True
    assert lg.deck_get_by_id(deck.id) is None
    assert lg.deck_delete_by_id(deck.id) is False

    print("Deck CRUD tests passed.")


def test_card_crud() -> None:
    user = lg.user_create("Carol", "carol@example.com", "pass")

    card1 = lg.card_create(user.id, "cat", "кіт", "Think of a small furry animal.")
    card2 = lg.card_create(user.id, "dog", "собака", "Man's best friend.")
    card3 = lg.card_create(user.id, "catalog", "каталог", "A list of items, contains 'cat'.")

    assert card1.id is not None
    assert card1.word == "cat"
    assert card1.translation == "кіт"

    fetched = lg.card_get_by_id(card1.id)
    assert fetched is not None
    assert fetched.word == "cat"

    updated = lg.card_update(card1.id, tip="A domestic feline.")
    assert updated.tip == "A domestic feline."
    assert updated.word == "cat"  # unchanged fields stay the same

    updated2 = lg.card_update(card2.id, word="puppy", translation="цуценя")
    assert updated2.word == "puppy"
    assert updated2.translation == "цуценя"

    # filter by substring found in "word" field ("cat" and "catalog")
    results = lg.card_filter("cat")
    words = {c.word for c in results}
    assert "cat" in words
    assert "catalog" in words
    assert "puppy" not in words

    # filter by substring found in the "tip" field
    results_tip = lg.card_filter("feline")
    assert len(results_tip) == 1
    assert results_tip[0].word == "cat"

    # filter with no matches
    assert lg.card_filter("xyz_no_match") == ()

    assert lg.card_get_by_id(999999) is None

    assert lg.card_delete_by_id(card3.id) is True
    assert lg.card_get_by_id(card3.id) is None
    assert lg.card_delete_by_id(card3.id) is False

    print("Card CRUD tests passed.")


if __name__ == "__main__":
    setup_db()
    test_user_crud()
    test_deck_crud()
    test_card_crud()
    print("All Linguist tests passed successfully!")

