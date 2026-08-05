import os

from dotenv import load_dotenv

load_dotenv()


# ======================
# Environment
# ======================

APP_ENV = "dev"


def set_environment(env: str):

    global APP_ENV
    global TELEGRAM_TOKEN

    APP_ENV = env.lower()

    if APP_ENV == "prod":

        TELEGRAM_TOKEN = os.getenv("TELEGRAM_PROD_TOKEN")

    else:

        TELEGRAM_TOKEN = os.getenv("TELEGRAM_DEV_TOKEN")


def get_environment():

    return APP_ENV.upper()


# ======================
# Common Config
# ======================

CHECK_INTERVAL = 10
AI_MODEL = "openrouter/free"


# ======================
# Telegram Config
# ======================

TELEGRAM_TOKEN = None
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ======================
# KAKAO Config
# ======================

KAKAO_ACCESS_TOKEN = os.getenv("KAKAO_ACCESS_TOKEN")
KAKAO_REFRESH_TOKEN = os.getenv("KAKAO_REFRESH_TOKEN")
KAKAO_REST_API_KEY = os.getenv("KAKAO_REST_API_KEY")
KAKAO_CLIENT_SECRET = os.getenv("KAKAO_CLIENT_SECRET")

# ======================
# AI Config
# ======================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ======================
# Initial Environment
# ======================

set_environment(os.getenv("APP_ENV", "dev"))


def print_config():

    print("""
================================

🤖 AI Secretary

Environment : {}
Telegram    : {}

================================
""".format(APP_ENV.upper(), "DEV BOT" if APP_ENV == "dev" else "PROD BOT"))


# ======================
# Lottery Config
# ======================

LOTTO_ID = os.getenv("LOTTO_ID")
LOTTO_PASSWORD = os.getenv("LOTTO_PASSWORD")
LOTTO_HEADLESS = os.getenv("LOTTO_HEADLESS", "true").lower() == "true"
