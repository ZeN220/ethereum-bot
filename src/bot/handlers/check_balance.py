from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.bot.states.check_balance import CheckBalanceState
from src.infrastructure.ethereum import Etherscan

check_balance_router = Router()


@check_balance_router.callback_query(Text("check_balance"))
async def enter_address(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text("Enter address for check balance")
    await state.set_state(CheckBalanceState.waiting_for_address)


@check_balance_router.message(CheckBalanceState.waiting_for_address)
async def check_balance(
    message: Message, state: FSMContext, ethereum: Etherscan
):
    try:
        balance = await ethereum.get_balance(message.text)
    except TypeError:
        await message.answer("Invalid address")
    else:
        await message.answer(f"Balance: {balance} ETH")
    await state.clear()
