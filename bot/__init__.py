from __future__ import annotations

import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv          # ← NEW

from utils.logger import setup_logging
from bot.middlewares.log_update import LogUpdate

# ────────────────────── логирование ──────────────────────
setup_logging()
logger = logging.getLogger("bot.init")

# ────────────────────── переменные .env ──────────────────
ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=False)        # ← NEW

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.critical("Переменная BOT_TOKEN не установлена! "
                    "Добавьте её в .env или окружение.")
    raise RuntimeError("BOT_TOKEN is missing")

# ────────────────────── объекты Aiogram ──────────────────
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()

# Логируем каждое входящее обновление
dp.message.middleware(LogUpdate())
dp.callback_query.middleware(LogUpdate())