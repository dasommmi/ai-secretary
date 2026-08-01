import sqlite3

from domain.knowledge.ports import InterestRepositoryPort


class SqliteInterestRepository(InterestRepositoryPort):

    def __init__(self, db_path: str = "assistant.db"):

        self.db_path = db_path

    def save(self, category: str):

        with sqlite3.connect(self.db_path) as conn:

            conn.execute(
                """
                INSERT OR IGNORE INTO knowledge_interest
                (
                    category,
                    enabled
                )
                VALUES
                (
                    ?,
                    1
                )
                """,
                (category,),
            )

    def find_all(self) -> list[str]:

        with sqlite3.connect(self.db_path) as conn:

            cursor = conn.execute("""
                SELECT category
                FROM knowledge_interest
                WHERE enabled = 1
                """)

            rows = cursor.fetchall()

            return [row[0] for row in rows]

    def delete(self, category: str):

        with sqlite3.connect(self.db_path) as conn:

            conn.execute(
                """
                DELETE FROM knowledge_interest
                WHERE category = ?
                """,
                (category,),
            )
