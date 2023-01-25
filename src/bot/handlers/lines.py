from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from src.database.models import User

lines_router = Router()


@lines_router.callback_query(Text("lines"))
async def show_lines(query: CallbackQuery, user: User):
    if not user.lines:
        await query.message.edit_text("You have no lines yet")
    formatted_lines = "\n".join(line.seed for line in user.lines)
    await query.message.edit_text(f"Here are your lines:\n{formatted_lines}")
