import time

from config import CHECK_INTERVAL
from services.swim_service import SwimService
from core.logger import logger


class Scheduler:

    def __init__(self):

        self.services = [SwimService()]

    def start(self):
        logger.info("Scheduler Started")

        while True:

            for service in self.services:

                try:
                    service.check()

                except Exception as e:
                    print(e)

            time.sleep(CHECK_INTERVAL)
