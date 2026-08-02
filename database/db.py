import sqlite3

DB_NAME = "assistant.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()

    cursor = conn.cursor()

    # ----------------------------
    # Memory
    # ----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT,

            content TEXT NOT NULL,

            category TEXT DEFAULT 'memo',

            importance INTEGER DEFAULT 3,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

    # ----------------------------
    # KAKAO TOKENS
    # ----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kakao_tokens (
            id INTEGER PRIMARY KEY,
            access_token TEXT NOT NULL,
            refresh_token TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

    # ----------------------------
    # Knowledge Interest
    # ----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_interest (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            category TEXT UNIQUE NOT NULL,

            enabled INTEGER DEFAULT 1,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

    # ----------------------------
    # Daily Digest
    # ----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_digest (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            digest_date TEXT NOT NULL,

            category TEXT NOT NULL,

            question TEXT NOT NULL,

            answer TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

    conn.commit()

    conn.close()
