import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from mustafar import BOT_API


bot = Bot(token=BOT_API)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Ну привет!")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())