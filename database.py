import sqlite3

DB_NAME = "db.sqlite"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     email TEXT UNIQUE NOT NULL,
                     password TEXT NOT NULL)''')
        conn.commit()

def get_db_connection():
    return sqlite3.connect(DB_NAME)
