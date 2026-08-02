import argparse
import threading

from application.knowledge.generate_daily_digest_use_case import (
    GenerateDailyDigestUseCase,
)
from config import (
    set_environment,
    print_config,
)
from core.runtime import runtime_manager
from core.scheduler import Scheduler
from database.db import init_db
from infrastructure.ai.openrouter_knowledge_curator import OpenRouterKnowledgeCurator
from infrastructure.notification.composite_notifier import CompositeNotifier
from infrastructure.notification.kakao_notifier import KakaoNotifier
from infrastructure.notification.telegram_notifier import TelegramNotifier
from infrastructure.persistence.sqlite_digest_repository import SqliteDigestRepository
from infrastructure.persistence.sqlite_interest_repository import (
    SqliteInterestRepository,
)
from infrastructure.scheduling.daily_digest_scheduler import DailyDigestScheduler

scheduler = None
digest_scheduler = None


def run_scheduler():

    global scheduler

    scheduler = Scheduler()

    scheduler.start()


def run_digest_scheduler():

    global digest_scheduler

    interest_repository = SqliteInterestRepository()

    digest_repository = SqliteDigestRepository()

    curator = OpenRouterKnowledgeCurator()

    use_case = GenerateDailyDigestUseCase(
        interest_repository=interest_repository,
        digest_repository=digest_repository,
        curator=curator,
    )

    notifier = CompositeNotifier(
        [
            TelegramNotifier(),
            KakaoNotifier(),
        ]
    )

    digest_scheduler = DailyDigestScheduler(
        use_case=use_case,
        notifier=notifier,
    )

    digest_scheduler.start()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--prod", action="store_true")

    args = parser.parse_args()

    if args.prod:

        set_environment("prod")

    else:

        set_environment("dev")

    runtime_manager.start("PROD" if args.prod else "DEV")

    print_config()

    from core.logger import logger

    init_db()

    logger.info("Scheduler : Starting")

    logger.info("AI Secretary starting")

    threading.Thread(target=run_digest_scheduler, daemon=True).start()
    # 환경 설정 이후 import
    from bot.receiver import TelegramReceiver

    TelegramReceiver().start()
