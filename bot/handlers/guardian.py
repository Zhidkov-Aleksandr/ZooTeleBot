# bot/handlers/guardian.py
from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

TEXT = (
    "<b>Что такое программа опеки?</b>\n\n"
    "Вы помогаете зоопарку содержать выбранное животное, "
    "а мы присылаем вам сертификат опекуна, приглашения "
    "на закрытые встречи и новости вашего подопечного."
)

@router.callback_query(F.data == "guardian_info")
async def guardian_info(cb: CallbackQuery):
    await cb.answer()           # закрыть «часики»
    await cb.message.answer(TEXT, disable_web_page_preview=True)