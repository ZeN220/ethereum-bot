from aiogram import Dispatcher

from .add_line import add_line_router
from .check_balance import check_balance_router
from .rules import rules_router
from .start import start_router


def setup_routers(dispatcher: Dispatcher):
    dispatcher.include_router(rules_router)
    dispatcher.include_router(start_router)
    dispatcher.include_router(check_balance_router)
    dispatcher.include_router(add_line_router)


__all__ = ["rules_router", "setup_routers"]
