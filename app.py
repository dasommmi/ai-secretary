import threading
from database.db import init_db

from bot.receiver import TelegramReceiver
from core.scheduler import Scheduler


def run_scheduler():
    Scheduler().start()


if __name__ == "__main__":
    init_db()

    threading.Thread(
        target=run_scheduler,
        daemon=True
    ).start()

    TelegramReceiver().start()
