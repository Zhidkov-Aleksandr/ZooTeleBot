import asyncio, os
from aiogram import Bot

async def reset():
    bot = Bot(os.getenv("BOT_TOKEN"))
    await bot.delete_webhook(drop_pending_updates=True)
    print("Webhook удалён, очередь очищена.")

asyncio.run(reset())