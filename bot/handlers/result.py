import json
import logging
from pathlib import Path

from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.fsm.context import FSMContext

from bot.services.scoring import choose_totem
from bot.services.media import animal_image
from bot.services.sharing import share_keyboard
from templates.result_texts import build_result_text

router = Router()
logger = logging.getLogger("handlers.result")

BASE_DIR = Path(__file__).resolve().parents[2]
ANIMALS = json.loads((BASE_DIR / "data" / "animals.json").read_text(encoding="utf-8"))


# ────────────────────────── клавиатура «опека / ещё раз» ──────────────────────────
def guardian_button(url: str) -> InlineKeyboardMarkup:
    """
    1-я строка — ссылка «Что такое программа опеки?» (url)
    2-я строка — callback «Пройти ещё раз»
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Что такое программа опеки?",
                    url=url,
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔄 Пройти ещё раз",
                    callback_data="quiz_start",
                )
            ],
        ]
    )
# ───────────────────────────────────────────────────────────────────────────────────


async def show_result(msg: Message, state: FSMContext) -> None:
    data = await state.get_data()
    answers = data.get("answers", [])
    animal_id = choose_totem(answers)
    animal = ANIMALS[animal_id]

    # картинка + описание + кнопки опеки
    await msg.answer_photo(
        photo=animal_image(animal["image"]),
        caption=build_result_text(animal),
        reply_markup=guardian_button(animal["guardian_link"]),
    )

    # отдельным сообщением кнопка «поделиться»
    await msg.answer(
        "Поделись открытием с друзьями!",
        reply_markup=share_keyboard(animal_id),
    )

    logger.info("user %s finished quiz → %s", msg.from_user.id, animal_id)
    await state.clear()
