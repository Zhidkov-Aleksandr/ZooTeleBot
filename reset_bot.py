import asyncio
from aiogram import Bot

TOKEN = "7676053709:AAEM_40GkPuf-QiL-IkpVlnPtdl9f75AvGQ"  # Hardcode the token
async def reset():
    bot = Bot(TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    print("✅ Webhook удалён, очередь очищена.")

asyncio.run(reset())