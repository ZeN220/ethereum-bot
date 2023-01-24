from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Update
from sqlalchemy.orm import sessionmaker

from src.database import UserService


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ):
        async with self.session_maker() as session:
            data["user_service"] = UserService(session)
            return await handler(event, data)
