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

        TELEGRAM_TOKEN = os.getenv(
            "TELEGRAM_PROD_TOKEN"
        )

    else:

        TELEGRAM_TOKEN = os.getenv(
            "TELEGRAM_DEV_TOKEN"
        )



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


TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)



# ======================
# AI Config
# ======================

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)


OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)



# ======================
# Initial Environment
# ======================

set_environment(
    os.getenv(
        "APP_ENV",
        "dev"
    )
)



def print_config():

    print(
        """
================================

🤖 AI Secretary

Environment : {}
Telegram    : {}

================================
""".format(
            APP_ENV.upper(),
            "DEV BOT"
            if APP_ENV == "dev"
            else "PROD BOT"
        )
    )