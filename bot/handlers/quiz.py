import json
import logging
from pathlib import Path

from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()
logger = logging.getLogger("handlers.quiz")

BASE_DIR = Path(__file__).resolve().parents[2]          # <корень проекта>
QUIZ_DATA = (BASE_DIR / "data" / "quiz.json").read_text(encoding="utf-8")
QUESTIONS = json.loads(QUIZ_DATA)
TOTAL = len(QUESTIONS)

class QuizState(StatesGroup):
    question = State()

# --- запуск викторины ---------------------------------------------------- #

@router.callback_query(F.data == "quiz_start")
async def quiz_start(clb: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.update_data(current=0, answers=[])
    await send_question(clb.message, 0, state)
    await clb.answer()

# --- вспомогательные функции -------------------------------------------- #

async def send_question(msg: Message, index: int, state: FSMContext) -> None:
    if index >= TOTAL:
        # все вопросы пройдены
        from bot.handlers.result import show_result  # локальный импорт во избежание циклов
        await show_result(msg, state)
        return

    q = QUESTIONS[index]
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=answer["text"],
                    callback_data=f"q{index}_a{ai}"
                )
            ]
            for ai, answer in enumerate(q["answers"])
        ]
    )
    await msg.answer(
        f"❓ Вопрос {index + 1} / {TOTAL}\n\n{q['question']}",
        reply_markup=keyboard,
    )
    await state.set_state(QuizState.question)

# --- обработка ответа ---------------------------------------------------- #

@router.callback_query(F.data.regexp(r"^q\d+_a\d+$"))
async def answer(clb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current = data["current"]
    answers = data["answers"]

    # разбор callback-data
    q_idx, a_idx = (int(x[1:]) for x in clb.data.split("_"))
    selected = QUESTIONS[q_idx]["answers"][a_idx]["weights"]
    answers.append(selected)

    # сохраняем
    await state.update_data(current=current + 1, answers=answers)
    await clb.message.edit_reply_markup(None)  # убираем кнопки у прошлого вопроса
    await send_question(clb.message, current + 1, state)
    await clb.answer()

@router.callback_query(F.data == "quiz_start")
async def quiz_start(cb: CallbackQuery, state: FSMContext):
    logger.info("callback received → start quiz")           # DEBUG
    await state.clear()
    await state.update_data(current=0, answers=[])
    await send_question(cb.message, 0, state)
    await cb.answer()