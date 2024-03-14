import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN, ADMIN_LIST


print(ADMIN_LIST)
bot = Bot(token=BOT_TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_message(message: Message):
    user = message.from_user
    user_id = user.id
    await bot.send_message(chat_id=-1002098726070, text=f"Пользователь {user.first_name} "\
                            f"{user.last_name} под ником {user.username} хочет присоединиться к Вам",
                              parse_mode=ParseMode.HTML)

    user = [
        [
            KeyboardButton(text="Посмотреть пользователя"),
        ],
    ]
    admin = [
        [
            KeyboardButton(text="Посмотреть пользователя"),
            KeyboardButton(text='Редактировать пользователя'),
            KeyboardButton(text='Удалить пользователя')
        ]
    ]
    user_keyboard = ReplyKeyboardMarkup(keyboard=user)
    admin_keyboard = ReplyKeyboardMarkup(keyboard=admin)
    if user_id in ADMIN_LIST:
        await message.reply(text='Что Вы хотите делать?', reply_markup=admin_keyboard)
    else:
        await message.reply(text='Что Вы хотите делать?', reply_markup=user_keyboard) 

