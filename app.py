import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message
from mustafar import config


bot = Bot(token=config.bot_token.get_secret_value())
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_message(message: Message):
    user = message.from_user
    await bot.send_message(chat_id=-1002098726070, text=f"Пользователь {user.first_name} "\
                            f"{user.last_name} под ником {user.username} хочет присоединиться к Вам",
                              parse_mode=ParseMode.HTML)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())