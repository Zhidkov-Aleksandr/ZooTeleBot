import logging
from pathlib import Path
from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message

router = Router()
logger = logging.getLogger("handlers.feedback")

FEEDBACK_PATH = Path("data/feedback.txt")

@router.message(F.text.regexp(r"^/feedback\s+"))
async def collect_feedback(msg: Message):
    text = msg.text.split(maxsplit=1)[1] if " " in msg.text else ""
    if not text:
        await msg.answer("Отправь отзыв так: <code>/feedback твой текст</code>")
        return

    FEEDBACK_PATH.parent.mkdir(exist_ok=True)
    FEEDBACK_PATH.touch(exist_ok=True)

    with FEEDBACK_PATH.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} — {msg.from_user.full_name}: {text}\n")
    await msg.answer("Спасибо за отзыв! 🐾")
    logger.info("feedback from %s saved", msg.from_user.id)
