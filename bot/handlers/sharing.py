import json
from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message

from templates.result_texts import build_result_text
from bot.services.media import animal_image
from bot.services.sharing import share_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


router = Router()

BASE_DIR = Path(__file__).resolve().parents[2]          # <корень проекта>
ANIMALS = json.loads(
    (BASE_DIR / "data" / "animals.json").read_text(encoding="utf-8")
)

@router.message(F.text.regexp(r"^/start\s+\w+"))
async def deep_start(msg: Message):
    """
    Обрабатывает ссылку вида  https://t.me/your_bot_username?start=<animal_id>
    """
    parts = msg.text.split(maxsplit=1)
    if len(parts) == 1:
        # обычный /start перехватит start.py
        return

    animal_id = parts[1]
    animal = ANIMALS.get(animal_id)
    if not animal:
        await msg.answer("Не удалось распознать ссылку 🙈")
        return

    await msg.answer_photo(
        photo=animal_image(animal["image"]),
        caption=build_result_text(animal),
        reply_markup=share_keyboard(animal_id),
    )
def share_keyboard(animal_id: str) -> InlineKeyboardMarkup:
    deep_link = f"https://t.me/your_bot_username?start={animal_id}"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Поделиться результатом 🐾",   # <-- именованные!
                    url=deep_link,
                )
            ]
        ]
    )