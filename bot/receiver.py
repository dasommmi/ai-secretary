from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)

import config

from bot.handlers import (
    help_command,
    status_command,
    remember_command,
    memories_command,
    ask_command,
    health_command,
)


class TelegramReceiver:

    def __init__(self):

        self.app = (
            ApplicationBuilder()
            .token(
                config.TELEGRAM_TOKEN
            )
            .build()
        )


        self.app.add_handler(
            CommandHandler(
                "help",
                help_command
            )
        )


        self.app.add_handler(
            CommandHandler(
                "status",
                status_command
            )
        )


        self.app.add_handler(
            CommandHandler(
                "remember",
                remember_command
            )
        )


        self.app.add_handler(
            CommandHandler(
                "memories",
                memories_command
            )
        )


        self.app.add_handler(
            CommandHandler(
                "ask",
                ask_command
            )
        )

        self.app.add_handler(
            CommandHandler(
                "health",
                health_command
            )
        )


    def start(self):

        print(
            "Telegram Receiver Started"
        )


        self.app.run_polling()