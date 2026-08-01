from datetime import date

from database.db import get_connection
from domain.knowledge.entities import DailyDigest
from domain.knowledge.ports import DigestRepositoryPort


class SqliteDigestRepository(DigestRepositoryPort):

    def save(self, digest: DailyDigest):

        conn = get_connection()

        cursor = conn.cursor()

        for item in digest.items:

            cursor.execute(
                """
                INSERT INTO knowledge_digest
                (
                    digest_date,
                    category,
                    question,
                    answer
                )
                VALUES
                (
                    ?, ?, ?, ?
                )
                """,
                (
                    digest.digest_date.isoformat(),
                    item.category,
                    item.question,
                    item.answer,
                ),
            )

        conn.commit()

        conn.close()

    def exists_today(self) -> bool:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM knowledge_digest

            WHERE digest_date = ?
            """,
            (date.today().isoformat(),),
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count > 0
