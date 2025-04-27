# bot/services/sharing.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def share_keyboard(animal_id: str) -> InlineKeyboardMarkup:
    deep_link = f"https://t.me/your_bot_username?start={animal_id}"
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton("Поделиться результатом 🐾", url=deep_link)]]
    )