from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from src.database import UserService

rules_router = Router()


@rules_router.callback_query(Text("accept_rules"))
async def accept_rules(query: CallbackQuery, user_service: UserService):
    await user_service.create(query.from_user.id)
    await query.answer("Thanks!")
    await query.message.delete()
