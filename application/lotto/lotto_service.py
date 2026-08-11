from application.logger import logger
from infrastructure.clients.dhlottery_client import DHLotteryClient


class LottoService:

    def purchase(self):

        client = DHLotteryClient()

        try:

            logger.info("Weekly lottery purchase started")

            client.start()

            # 로또 6/45
            lotto_success = client.purchase_lotto()

            # 연금복권720+
            pension_success = client.purchase_pension_lottery()

            if lotto_success and pension_success:

                logger.info("Weekly lottery purchase completed successfully")

                return True

            logger.warning("Weekly lottery purchase partially failed")

            return False

        except Exception:

            logger.exception("Weekly lottery purchase failed")

            return False

        finally:

            client.close()
