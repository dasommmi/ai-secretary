import json
import requests

from config import KAKAO_ACCESS_TOKEN


class KakaoNotifier:

    URL = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    def send(self, message: str):

        headers = {
            "Authorization": f"Bearer {KAKAO_ACCESS_TOKEN}",
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

        response = requests.post(
            self.URL,
            headers=headers,
            data={"template_object": json.dumps(template_object)},
        )

        response.raise_for_status()
