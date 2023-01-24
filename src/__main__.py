import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.bot.handlers import setup_routers
from src.bot.middlewares import DatabaseMiddleware, RulesMiddleware
from src.config import Config


async def main():
    config = Config.from_file("config.toml")
    logging.basicConfig(
        level=config.logging.level, format=config.logging.format
    )

    engine = create_async_engine(config.database.dns)
    session_maker = sessionmaker(bind=engine, class_=AsyncSession, future=True)

    bot = Bot(token=config.telegram.bot_token)
    dispatcher = Dispatcher()

    setup_routers(dispatcher)

    dispatcher.update.outer_middleware(DatabaseMiddleware(session_maker))
    dispatcher.message.outer_middleware(RulesMiddleware())

    await dispatcher.start_polling(
        bot, allowed_updates=["message", "callback_query"]
    )


if __name__ == "__main__":
    asyncio.run(main())
