from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.result import guardian_button
from bot.services.sharing import share_keyboard


def test_guardian_button_structure():
    kb: InlineKeyboardMarkup = guardian_button("https://example.com")

    rows = kb.inline_keyboard
    assert len(rows) == 2, "Ожидаем два ряда кнопок"

    urls = [btn.url for btn in rows[0]]
    assert urls == ["https://example.com"]

    cb_data = [btn.callback_data for btn in rows[1]]
    assert cb_data == ["quiz_start"]


def test_share_keyboard_url():
    kb: InlineKeyboardMarkup = share_keyboard("tiger")

    assert len(kb.inline_keyboard) == 1
    btn: InlineKeyboardButton = kb.inline_keyboard[0][0]

    assert btn.text.startswith("Поделиться"), "Неверный текст кнопки"
    assert "start=tiger" in btn.url, "Глубокая ссылка не содержит id животного"
