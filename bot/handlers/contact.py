import logging
from pathlib import Path
from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()
logger = logging.getLogger("handlers.contact")

CONTACT_FILE = Path("data/contact_requests.txt")

@router.message(F.text == "/contact")
async def request_contact(msg: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Отправить мои контакты ☎️", request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await msg.answer("Как с тобой связаться? Нажми кнопку, чтобы передать номер телефона.", reply_markup=kb)

@router.message(F.contact)
async def save_contact(msg: Message):
    CONTACT_FILE.parent.mkdir(exist_ok=True)
    CONTACT_FILE.touch(exist_ok=True)
    with CONTACT_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} — {msg.from_user.full_name} — {msg.contact.phone_number}\n")
    await msg.answer("Спасибо! Мы свяжемся с тобой как можно скорее.")
    logger.info("contact request from %s saved", msg.from_user.id)
