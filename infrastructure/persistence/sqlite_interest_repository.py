from database.db import get_connection

from domain.knowledge.ports import InterestRepositoryPort


class SqliteInterestRepository(InterestRepositoryPort):

    def save(self, category: str):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO knowledge_interest
            (
                category
            )
            VALUES
            (
                ?
            )
            """,
            (category,),
        )

        conn.commit()

        conn.close()

    def find_all(self) -> list[str]:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT category

            FROM knowledge_interest

            WHERE enabled = 1
            """)

        rows = cursor.fetchall()

        conn.close()

        return [row[0] for row in rows]
