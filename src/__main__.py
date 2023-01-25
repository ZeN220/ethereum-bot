import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.bot import middlewares
from src.bot.handlers import setup_routers
from src.config import Config
from src.infrastructure.ethereum import Etherscan


async def main():
    config = Config.from_file("config.toml")
    logging.basicConfig(
        level=config.logging.level, format=config.logging.format
    )

    engine = create_async_engine(config.database.dns)
    session_maker = sessionmaker(bind=engine, class_=AsyncSession, future=True)

    ethereum = Etherscan(config.etherscan.api_key)

    bot = Bot(token=config.telegram.bot_token)
    dispatcher = Dispatcher()

    setup_routers(dispatcher)

    dispatcher.update.outer_middleware(
        middlewares.DatabaseMiddleware(session_maker)
    )
    dispatcher.update.outer_middleware(middlewares.UserObjectMiddleware())
    dispatcher.message.outer_middleware(middlewares.RulesMiddleware())

    await dispatcher.start_polling(
        bot, allowed_updates=["message", "callback_query"], ethereum=ethereum
    )


if __name__ == "__main__":
    asyncio.run(main())
