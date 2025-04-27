"""
Обработчик deep-link вида https://t.me/<бот>?start=<animal_id>
(используется кнопкой «Поделиться результатом»).
"""
import json
from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message

from templates.result_texts import build_result_text
from bot.services.media import animal_image
from bot.services.sharing import share_keyboard

router = Router()

BASE_DIR = Path(__file__).resolve().parents[2]
ANIMALS = json.loads((BASE_DIR / "data" / "animals.json").read_text(encoding="utf-8"))


@router.message(F.text.regexp(r"^/start\s+\w+"))
async def deep_start(msg: Message):
    # сообщение формата "/start <animal_id>"
    _, animal_id = msg.text.split(maxsplit=1)

    animal = ANIMALS.get(animal_id)
    if not animal:
        await msg.answer("Не удалось распознать ссылку 🙈")
        return

    await msg.answer_photo(
        photo=animal_image(animal["image"]),
        caption=build_result_text(animal),
        reply_markup=share_keyboard(animal_id),
    )
