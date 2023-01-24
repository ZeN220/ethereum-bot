from aiogram import Dispatcher

from .rules import rules_router


def setup_routers(dispatcher: Dispatcher):
    dispatcher.include_router(rules_router)


__all__ = ["rules_router", "setup_routers"]
