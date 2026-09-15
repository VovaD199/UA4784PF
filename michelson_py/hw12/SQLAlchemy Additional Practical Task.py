import sqlite3

DB_NAME = "linguist.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS decks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            translation TEXT NOT NULL,
            tip TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        )
    """)
    
    conn.commit()
    conn.close()

init_db()


class User:
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class Deck:
    def __init__(self, id: int, name: str, user_id: int):
        self.id = id
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"Deck(id={self.id}, name='{self.name}', user_id={self.user_id})"


class Card:
    def __init__(self, id: int, user_id: int, word: str, translation: str, tip: str):
        self.id = id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

    def __repr__(self):
        return f"Card(id={self.id}, user_id={self.user_id}, word='{self.word}', translation='{self.translation}', tip='{self.tip}')"


def user_create(name: str, email: str, password: str) -> User:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return User(id=user_id, name=name, email=email, password=password)


def user_get_by_id(user_id: int) -> User:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, password FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(id=row[0], name=row[1], email=row[2], password=row[3])
    return None


def user_update_name(user_id: int, name: str) -> User:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    conn.commit()
    conn.close()
    return user_get_by_id(user_id)


def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    
    if row and row[0] == old_password:
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False


def user_delete_by_id(user_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    rowcount = cursor.rowcount
    conn.commit()
    conn.close()
    return rowcount > 0


def deck_create(name: str, user_id: int) -> Deck:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO decks (name, user_id) VALUES (?, ?)", (name, user_id))
    conn.commit()
    deck_id = cursor.lastrowid
    conn.close()
    return Deck(id=deck_id, name=name, user_id=user_id)


def deck_get_by_id(deck_id: int) -> Deck:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, user_id FROM decks WHERE id = ?", (deck_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Deck(id=row[0], name=row[1], user_id=row[2])
    return None


def deck_update(deck_id: int, name: str) -> Deck:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE decks SET name = ? WHERE id = ?", (name, deck_id))
    conn.commit()
    conn.close()
    return deck_get_by_id(deck_id)


def deck_delete_by_id(deck_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM decks WHERE id = ?", (deck_id,))
    rowcount = cursor.rowcount
    conn.commit()
    conn.close()
    return rowcount > 0


def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cards (user_id, word, translation, tip) VALUES (?, ?, ?, ?)",
        (user_id, word, translation, tip)
    )
    conn.commit()
    card_id = cursor.lastrowid
    conn.close()
    return Card(id=card_id, user_id=user_id, word=word, translation=translation, tip=tip)


def card_get_by_id(card_id: int) -> Card:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_id, word, translation, tip FROM cards WHERE id = ?", (card_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Card(id=row[0], user_id=row[1], word=row[2], translation=row[3], tip=row[4])
    return None


def card_filter(sub_word: str) -> tuple[Card, ...]:
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT id, user_id, word, translation, tip FROM cards 
        WHERE word LIKE ? OR translation LIKE ? OR tip LIKE ?
    """
    search_pattern = f"%{sub_word}%"
    cursor.execute(query, (search_pattern, search_pattern, search_pattern))
    rows = cursor.fetchall()
    conn.close()
    
    cards = [Card(id=r[0], user_id=r[1], word=r[2], translation=r[3], tip=r[4]) for r in rows]
    return tuple(cards)


def card_update(card_id: int, word: str = None, translation: str = None, tip: str = None) -> Card:
    current_card = card_get_by_id(card_id)
    if not current_card:
        return None

    new_word = word if word is not None else current_card.word
    new_translation = translation if translation is not None else current_card.translation
    new_tip = tip if tip is not None else current_card.tip

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cards SET word = ?, translation = ?, tip = ? WHERE id = ?",
        (new_word, new_translation, new_tip, card_id)
    )
    conn.commit()
    conn.close()
    return card_get_by_id(card_id)


def card_delete_by_id(card_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cards WHERE id = ?", (card_id,))
    rowcount = cursor.rowcount
    conn.commit()
    conn.close()
    return rowcount > 0

if __name__ == "__main__":
    user = user_create("Test User", "test@gmail.com", "password123")
    print(user)