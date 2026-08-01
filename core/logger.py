import logging
import os


LOG_DIR = "logs"


if not os.path.exists(LOG_DIR):

    os.makedirs(LOG_DIR)


logger = logging.getLogger("ai-secretary")


logger.setLevel(logging.INFO)


formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")


file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")


file_handler.setFormatter(formatter)


console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)


logger.addHandler(file_handler)


logger.addHandler(console_handler)
