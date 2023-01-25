from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.bot.keyboads.start import get_start_keyboard

start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message):
    await send_start_message(message)


async def send_start_message(message: Message):
    await message.answer("Start message", reply_markup=get_start_keyboard())
