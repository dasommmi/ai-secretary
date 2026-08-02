from database.db import get_connection


class SqliteKakaoTokenRepository:

    def save(
        self,
        access_token: str,
        refresh_token: str,
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM kakao_tokens
            """)

        cursor.execute(
            """
            INSERT INTO kakao_tokens(
                id,
                access_token,
                refresh_token
            )
            VALUES(1, ?, ?)
            """,
            (
                access_token,
                refresh_token,
            ),
        )

        conn.commit()
        conn.close()

    def find(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT access_token, refresh_token
            FROM kakao_tokens
            WHERE id = 1
            """)

        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        print(row[0])
        print(row[1])

        return {
            "access_token": row[0],
            "refresh_token": row[1],
        }
