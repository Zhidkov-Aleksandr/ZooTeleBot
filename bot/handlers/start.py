import logging
from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from utils.logger import setup_logger

BASE_DIR = Path(__file__).resolve().parents[2]
INTRO_MD = (BASE_DIR / "templates" / "intro.md").read_text(encoding="utf-8")

logger = setup_logger("handlers.start")
router = Router()

@router.message(F.text == "/start")
async def cmd_start(msg: Message, state: FSMContext) -> None:
    await state.clear()
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Начать викторину",
                    callback_data="quiz_start",
                )
            ]
        ]
    )
    await msg.answer(INTRO_MD, reply_markup=kb)