from aiogram.fsm.state import State, StatesGroup


class CheckBalanceState(StatesGroup):
    waiting_for_address = State()
