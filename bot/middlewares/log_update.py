from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Any
import logging
import json
from pydantic import BaseModel

logger = logging.getLogger("update")


class LogUpdate(BaseMiddleware):
    """Логирует входящее событие и время его обработки."""

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Any],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        # название типа: Message, CallbackQuery, etc.
        event_name = event.__class__.__name__
        logger.debug("⬇️  %s", event_name)

        # аккуратно сериализуем
        if isinstance(event, BaseModel):
            try:
                logger.debug(json.dumps(event.model_dump(mode="json"), ensure_ascii=False))
            except ValueError:
                # если попался объект с не-json-able полями
                logger.debug(repr(event))
        else:
            logger.debug(repr(event))

        try:
            return await handler(event, data)
        except Exception:
            logger.exception("❌ Ошибка при обработке %s", event_name)
            raise
