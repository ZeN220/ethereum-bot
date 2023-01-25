from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.bot.states.add_line import AddLineState
from src.database import LineService
from src.infrastructure.mnemonic import validation_seeds

add_line_router = Router()


@add_line_router.callback_query(Text("add_line"))
async def enter_seeds(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text("Input your seeds phrases. One per line.")
    await state.set_state(AddLineState.waiting_for_seed)


@add_line_router.message(AddLineState.waiting_for_seed)
async def add_line(
    message: Message, line_service: LineService, state: FSMContext
):
    seeds = message.text.split("\n")
    valid_seeds = validation_seeds(seeds)
    if not valid_seeds:
        await message.answer("No valid seeds")
        return

    seeds_answer = await message.answer(f"Find {len(valid_seeds)} valid seeds")
    seeds, count_duplicates = await line_service.create_many(
        valid_seeds, message.from_user.id
    )
    await seeds_answer.edit_text(
        f"Added {len(seeds)} seeds. {count_duplicates} duplicates"
    )

    await state.clear()
