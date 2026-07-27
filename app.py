import logging
import time

from bot.sender import send_message
from services.swim_monitor import SwimMonitor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

CHECK_INTERVAL = 10

monitor = SwimMonitor()

last_remain = -1

send_message("🤖 AI 비서 시작!")

while True:

    try:

        remain, total = monitor.check()

        logging.info(f"현재 좌석 : {remain}/{total}")

        if remain > 0 and remain != last_remain:

            send_message(
                f"""
🏊 자리 발생!!

강좌
{monitor.TARGET}

현재
{remain}/{total}

{monitor.URL}
"""
            )

        last_remain = remain

    except Exception:

        logging.exception("Swim Monitor Error")

    time.sleep(CHECK_INTERVAL)