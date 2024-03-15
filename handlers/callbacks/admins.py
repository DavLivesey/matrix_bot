from loader import dp 
from aiogram import types
from main import DBCommands


dp.callback_query('add_user')
async def add_user(callback: types.CallbackQuery, fullname):
    await DBCommands.add_new_user(fullname=fullname)