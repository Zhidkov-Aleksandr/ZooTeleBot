import asyncio
import logging

from aiogram import F
from aiogram.enums import UpdateType
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot import bot, dp
from bot.router import setup_routers
from utils.logger import setup_logger
import logging

setup_logger("totem_bot")
logger = logging.getLogger("totem_bot")

dp.include_router(setup_routers())

async def on_startup() -> None:
    logger.info("Bot starting up…")

async def main() -> None:
    # Для long-polling:
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == "__main__":
    asyncio.run(main())
