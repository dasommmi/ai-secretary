import threading

from bot.receiver import TelegramReceiver
from core.scheduler import Scheduler


def run_scheduler():
    Scheduler().start()


if __name__ == "__main__":

    threading.Thread(
        target=run_scheduler,
        daemon=True
    ).start()

    TelegramReceiver().start()