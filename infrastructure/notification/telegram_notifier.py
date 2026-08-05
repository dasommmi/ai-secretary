import requests

from config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


class TelegramNotifier:

    def send(self, message: str):

        url = f"https://api.telegram.org/" f"bot{TELEGRAM_TOKEN}/sendMessage"

        response = requests.post(
            url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message}
        )

        response.raise_for_status()
