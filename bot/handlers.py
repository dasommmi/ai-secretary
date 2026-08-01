from telegram import Update
from telegram.ext import ContextTypes
from services.assistant_service import chat
from services.content_service import ContentService
from services.content_session_service import ContentSessionService

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

content_service = ContentService()

session_service = ContentSessionService()


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
        🤖 AI Secretary
        
Available Commands

[System]

/help
/status


[Memory]

/remember xxx
/memories


[AI]

/ask 질문


[Content]

/content restaurant
        """
    )


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

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


async def health_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

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


async def remember_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text("기억할 내용을 입력해주세요.")
        return

    user_id = str(update.effective_user.id)

    save_memory(user_id, text)

    await update.message.reply_text(f"🧠 기억했습니다.\n\n{text}")


async def memories_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = str(update.effective_user.id)

    memories = get_memories(user_id)

    if not memories:
        await update.message.reply_text("저장된 기억이 없습니다.")
        return

    message = "🧠 기억 목록\n\n"

    for memory in memories:
        message += f"{memory[0]}. " f"{memory[1]}\n"

    await update.message.reply_text(message)


async def ask_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = " ".join(context.args)

    if not text:

        await update.message.reply_text("질문을 입력해주세요.")

        return

    answer = chat(text)

    await update.message.reply_text(answer)


async def content_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text("사용법: /content restaurant")

        return

    content_type = context.args[0]

    user_id = str(update.effective_user.id)

    session_service.create(user_id, content_type)

    form = content_service.get_form(content_type)

    await update.message.reply_text(
        f"""
✍️ {content_type} 작성 시작

아래 양식을 작성해주세요.

{form}
"""
    )


async def content_generate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = " ".join(context.args)

    if not text:

        await update.message.reply_text("작성할 내용을 입력해주세요.")

        return

    service = ContentService()

    request = service.parse("restaurant", text)

    prompt = service.build_prompt("restaurant", request)

    result = service.generate(prompt)

    file_path = service.write_markdown("restaurant", result)

    await update.message.reply_text(
        f"""
    📝 글 생성 완료
    
    파일 저장:
    
    {file_path}
    """
    )


async def text_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = str(update.effective_user.id)

    session = session_service.get(user_id)

    if not session:

        return

    content_type = session["content_type"]

    request = content_service.parse(content_type, update.message.text)

    prompt = content_service.build_prompt(content_type, request)

    result = content_service.generate(prompt)

    file_path = content_service.write_markdown(content_type, result)

    session_service.remove(user_id)

    await update.message.reply_text(
        f"""
📝 작성 완료

파일 생성:

{file_path}
"""
    )
