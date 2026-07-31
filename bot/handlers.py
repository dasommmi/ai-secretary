from telegram import Update
from telegram.ext import ContextTypes
from services.assistant_service import chat
from services.content_service import ContentService

from config import (
    CHECK_INTERVAL,
    get_environment,
    AI_MODEL,
)
from services.memory_service import (
    save_memory,
    get_memories,
)
from core.runtime import runtime_manager

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
        🤖 AI Secretary
        
        Available Commands
        
        /help
        /status
        /remember xxx
        /memories
        /ask 질문
        /content restaurant
        """
    )


async def status_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        f"""
🤖 AI Secretary


Environment : {get_environment()}


Status

🟢 Running


🏊 Swim Monitor

Interval : {CHECK_INTERVAL} sec


🤖 AI Model

{AI_MODEL}
"""
    )

async def health_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    health = runtime_manager.get_status()


    await update.message.reply_text(
        f"""
🤖 AI Secretary Health


Environment :

{health["environment"]}


Status :

{health["status"]}


Uptime :

{health["uptime"]}
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


async def ask_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    text = " ".join(context.args)


    if not text:

        await update.message.reply_text(
            "질문을 입력해주세요."
        )

        return


    answer = chat(text)


    await update.message.reply_text(
        answer
    )


async def content_command(
            update: Update,
            context: ContextTypes.DEFAULT_TYPE
    ):

    if not context.args:

        await update.message.reply_text(
            """
사용법

/content restaurant
"""
        )

        return

    content_type = context.args[0]

    service = ContentService()

    try:

        form = service.get_form(content_type)

        await update.message.reply_text(form)

    except ValueError as e:

        await update.message.reply_text(str(e))

async def content_generate_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    text = " ".join(context.args)


    if not text:

        await update.message.reply_text(
            "작성할 내용을 입력해주세요."
        )

        return


    service = ContentService()


    request = service.parse(
        "restaurant",
        text
    )


    prompt = service.build_prompt(
        "restaurant",
        request
    )


    result = service.generate(
        prompt
    )


    await update.message.reply_text(
        result
    )