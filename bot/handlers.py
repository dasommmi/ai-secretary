from telegram import Update
from telegram.ext import ContextTypes

from config import CHECK_INTERVAL
from services.memory_service import (
    save_memory,
    get_memories,
)

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


async def remember_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text(
            "기억할 내용을 입력해주세요."
        )
        return


    user_id = str(update.effective_user.id)

    save_memory(
        user_id,
        text
    )


    await update.message.reply_text(
        f"🧠 기억했습니다.\n\n{text}"
    )



async def memories_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user_id = str(update.effective_user.id)

    memories = get_memories(user_id)


    if not memories:
        await update.message.reply_text(
            "저장된 기억이 없습니다."
        )
        return


    message = "🧠 기억 목록\n\n"

    for memory in memories:
        message += (
            f"{memory[0]}. "
            f"{memory[1]}\n"
        )


    await update.message.reply_text(message)