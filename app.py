import threading
import argparse


from database.db import init_db

from core.scheduler import Scheduler
from core.runtime import RuntimeManager

from config import (
    set_environment,
    print_config,
)



scheduler = None
runtime = RuntimeManager()


def run_scheduler():

    global scheduler


    scheduler = Scheduler()

    scheduler.start()



if __name__ == "__main__":


    parser = argparse.ArgumentParser()


    parser.add_argument(
        "--prod",
        action="store_true"
    )


    args = parser.parse_args()



    if args.prod:

        set_environment(
            "prod"
        )

    else:

        set_environment(
            "dev"
        )

    runtime.start(
        "PROD" if args.prod else "DEV"
    )

    print_config()



    init_db()



    print(
        "Scheduler : Starting"
    )



    threading.Thread(
        target=run_scheduler,
        daemon=True
    ).start()



    # 환경 설정 이후 import
    from bot.receiver import TelegramReceiver



    TelegramReceiver().start()