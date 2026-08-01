from database.db import get_connection


def save_memory(user_id, content, category="memo", importance=3):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memories
        (
            user_id,
            content,
            category,
            importance
        )
        VALUES (?, ?, ?, ?)
        """,
        (user_id, content, category, importance),
    )

    conn.commit()
    conn.close()


def get_memories(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, content, category, importance, created_at
        FROM memories
        WHERE user_id = ?
        ORDER BY id DESC
        """,
        (user_id,),
    )

    memories = cursor.fetchall()

    conn.close()

    return memories


def delete_memory(user_id, memory_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM memories
        WHERE id = ?
        AND user_id = ?
        """,
        (memory_id, user_id),
    )

    conn.commit()
    conn.close()
