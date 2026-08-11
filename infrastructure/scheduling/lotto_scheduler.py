from application.lotto.lotto_service import LottoService

from application.logger import logger
from infrastructure.notification.telegram_notifier import TelegramNotifier


class LottoScheduler:

    def __init__(self):

        self.lotto_service = LottoService()
        self.notifier = TelegramNotifier()

        from apscheduler.schedulers.background import BackgroundScheduler

        self.scheduler = BackgroundScheduler()

    def start(self):

        logger.info("LottoScheduler started")

        self.scheduler.add_job(
            self.execute,
            trigger="cron",
            day_of_week="wed",
            hour=10,
            minute=0,
            max_instances=1,
            coalesce=True,
        )

        self.scheduler.start()

    def execute(self):

        logger.info("Weekly lotto purchase started")

        success = self.lotto_service.purchase()

        if success:

            logger.info("Weekly lotto purchase completed")

            self.notifier.send("""
🎟 로또 자동 구매 완료

이번 주 로또 6/45
자동선택 5게임

구매가 정상적으로 완료되었습니다.
""".strip())

        else:

            logger.warning("Weekly lotto purchase failed")

            self.notifier.send("""
⚠️ 로또 자동 구매 실패

이번 주 로또 6/45 구매에 실패했습니다.

로그를 확인해주세요.
""".strip())
