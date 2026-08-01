import threading
import argparse


from database.db import init_db
from core.scheduler import Scheduler

from config import (
    set_environment,
    print_config,
)



def run_scheduler():

    Scheduler().start()



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



    print_config()



    init_db()


    from bot.receiver import TelegramReceiver

    threading.Thread(
        target=run_scheduler,
        daemon=True
    ).start()



    TelegramReceiver().start()