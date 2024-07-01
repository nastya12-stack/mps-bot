import asyncio
import os

import dotenv
from aiogram import Bot, Dispatcher
from routes import router


async def main() -> None:
    dotenv.load_dotenv()
    token = os.getenv("BOT_TOKEN")

    bot = Bot(token)

    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

# Entry point
#Hello поменяй start.py
if __name__ == "__main__":
    asyncio.run(main())