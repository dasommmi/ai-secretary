import time

from config.settings import CHECK_INTERVAL
from application.swim.swim_service import SwimService
from application.logger import logger


class Scheduler:

    def __init__(self):

        self.services = [SwimService()]

    def start(self):
        logger.info("Scheduler Started")

        while True:

            for service in self.services:

                try:
                    service.check()

                except Exception:
                    logger.exception(f"{service.__class__.__name__}.check() failed")

            time.sleep(CHECK_INTERVAL)
