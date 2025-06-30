import sqlite3

def create_connection():
    conn = sqlite3.connect("quiz_scores.db")
    return conn

def create_table():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')
        conn.commit()
    finally:
        conn.close()


def save_score(name, score):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

def get_high_score():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result if result else ("No scores yet", 0)
