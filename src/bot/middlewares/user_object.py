from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Update, User

from src.database import UserService


class UserObjectMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ):
        event_from_user: User = data["event_from_user"]
        user_service: UserService = data["user_service"]
        user = await user_service.get(event_from_user.id)
        data["user"] = user
        return await handler(event, data)
