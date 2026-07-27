from telegram import Update
from telegram.ext import ContextTypes

from config import CHECK_INTERVAL


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
        🤖 AI Secretary
        
        Available Commands
        
        /help
        
        /status
        """
    )


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"""
🤖 AI Secretary

Status

🟢 Running

🏊 Swim Monitor

Interval : {CHECK_INTERVAL} sec
"""
    )