from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config.settings import TELEGRAM_TOKEN

from interfaces.telegram.handlers import (
    help_command,
    status_command,
    remember_command,
    memories_command,
    ask_command,
    health_command,
    content_command,
    text_message_handler,
)
from application.logger import logger


class TelegramReceiver:

    def __init__(self):

        self.app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        self.app.add_handler(CommandHandler("help", help_command))

        self.app.add_handler(CommandHandler("status", status_command))

        self.app.add_handler(CommandHandler("remember", remember_command))

        self.app.add_handler(CommandHandler("memories", memories_command))

        self.app.add_handler(CommandHandler("ask", ask_command))

        self.app.add_handler(CommandHandler("health", health_command))

        self.app.add_handler(CommandHandler("content", content_command))

        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, text_message_handler)
        )

    def start(self):

        logger.info("Telegram Receiver Started")

        self.app.run_polling()
