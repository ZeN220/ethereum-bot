from aiogram import Dispatcher

from .check_balance import check_balance_router
from .rules import rules_router
from .start import start_router


def setup_routers(dispatcher: Dispatcher):
    dispatcher.include_router(rules_router)
    dispatcher.include_router(start_router)
    dispatcher.include_router(check_balance_router)


__all__ = ["rules_router", "setup_routers"]
