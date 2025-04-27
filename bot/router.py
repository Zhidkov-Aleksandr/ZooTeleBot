from aiogram import Router
from bot.handlers import guardian

from bot.handlers import (
    start,
    quiz,
    result,
    contact,
    feedback,
    sharing as sharing_handler,   # deep-link обработчик
)

def setup_routers() -> Router:
    root_router = Router()

    root_router.include_router(start.router)
    root_router.include_router(quiz.router)
    root_router.include_router(result.router)
    root_router.include_router(contact.router)
    root_router.include_router(feedback.router)
    root_router.include_router(sharing_handler.router)
    root_router.include_router(guardian.router)
    return root_router