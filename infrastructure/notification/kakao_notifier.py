import json

import requests

from config.settings import (
    KAKAO_REST_API_KEY,
    KAKAO_CLIENT_SECRET,
)
from infrastructure.persistence.sqlite_kakao_token_repository import (
    SqliteKakaoTokenRepository,
)


class KakaoNotifier:

    URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    TOKEN_URL = "https://kauth.kakao.com/oauth/token"

    def __init__(self):

        self.token_repository = SqliteKakaoTokenRepository()

        token = self.token_repository.find()

        self.access_token = token["access_token"]
        self.refresh_token = token["refresh_token"]

    def send(self, message: str):

        response = self._send_message(message)

        if response.status_code == 401:

            self.refresh_access_token()

            self._send_message(message)

            return

        response.raise_for_status()

    def _send_message(self, message: str):

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        template_object = {
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com",
            },
        }

        return requests.post(
            self.URL,
            headers=headers,
            data={"template_object": json.dumps(template_object)},
        )

    def refresh_access_token(self):

        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "client_id": KAKAO_REST_API_KEY,
                "client_secret": KAKAO_CLIENT_SECRET,
                "refresh_token": self.refresh_token,
            },
        )

        print("STATUS:", response.status_code)
        print("BODY:", response.text)

        response.raise_for_status()

        data = response.json()

        self.access_token = data["access_token"]

        if "refresh_token" in data:
            self.refresh_token = data["refresh_token"]

        self.token_repository.save(
            self.access_token,
            self.refresh_token,
        )
