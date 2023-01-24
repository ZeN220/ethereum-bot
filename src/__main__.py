import asyncio

from aiogram import Bot, Dispatcher

from src.config import Config


async def main():
    config = Config.from_file("config.toml")

    bot = Bot(token=config.telegram.bot_token)
    dispatcher = Dispatcher()

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
