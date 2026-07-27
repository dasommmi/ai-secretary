import os

from dotenv import load_dotenv

load_dotenv()

CHECK_INTERVAL = 10

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")