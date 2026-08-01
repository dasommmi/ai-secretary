import requests

from config import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN


def send_message(message: str):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    response = requests.post(
        url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message}, timeout=10
    )

    if not response.ok:
        print(response.text)
