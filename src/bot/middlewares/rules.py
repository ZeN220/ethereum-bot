from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.bot.keyboads.rules import get_rules_keyboard
from src.database import UserService


class RulesMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ):
        user_service: UserService = data["user_service"]
        user = await user_service.get(event.from_user.id)
        if user is None:
            await event.answer(
                "It's rules!", reply_markup=get_rules_keyboard()
            )
            return
        data["user"] = user
        return await handler(event, data)
