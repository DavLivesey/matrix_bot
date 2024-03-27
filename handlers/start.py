#from .callbacks.admins import ADDUSER
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_TOKEN, ADMIN_LIST


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
    user_keyboard = InlineKeyboardMarkup(inline_keyboard=
        [
        [
            InlineKeyboardButton(text="Посмотреть пользователя", callback_data='see_user'),
        ],
    ]
    )
    admin_keyboard = InlineKeyboardMarkup(inline_keyboard=
        [
        [   
            InlineKeyboardButton(text="Создать пользователя", callback_data='add_fullname'),
            InlineKeyboardButton(text="Посмотреть пользователя", callback_data='see_user'),
            InlineKeyboardButton(text='Редактировать пользователя', callback_data='edit_user'),
            InlineKeyboardButton(text='Удалить пользователя', callback_data='delete_user')
        ]
    ]
    )

    if user_id in ADMIN_LIST:
        await message.reply(text='Что Вы хотите делать?', reply_markup=admin_keyboard)
    else:
        await message.reply(text='Что Вы хотите делать?', reply_markup=user_keyboard) 


