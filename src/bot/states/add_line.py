from aiogram.fsm.state import State, StatesGroup


class AddLineState(StatesGroup):
    waiting_for_seed = State()
