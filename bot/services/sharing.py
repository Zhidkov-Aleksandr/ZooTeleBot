"""Cоставляет клавиатуру «Поделиться результатом»."""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def share_keyboard(animal_id: str) -> InlineKeyboardMarkup:
    """
    Возвращает разметку из ОДНОЙ кнопки-ссылки.
    Aiogram 3 (pydantic v2) требует, чтобы все аргументы
    конструктора передавались именованно.
    """
    deep_link = f"https://t.me/your_bot_username?start={animal_id}"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Поделиться результатом 🐾",
                    url=deep_link,
                )
            ]
        ]
    )
