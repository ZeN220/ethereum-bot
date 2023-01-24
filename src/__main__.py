import asyncio

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.bot.middlewares import DatabaseMiddleware
from src.config import Config


async def main():
    config = Config.from_file("config.toml")

    engine = create_async_engine(config.database.dns)
    session_maker = sessionmaker(bind=engine, class_=AsyncSession, future=True)

    bot = Bot(token=config.bot.token)
    dispatcher = Dispatcher()

    dispatcher.update.middleware(DatabaseMiddleware(session_maker))

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
