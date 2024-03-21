from aiogram import types, F
from ..main import DBCommands
from data import ADDUSER
from loader import dp
from aiogram.filters import command
from aiogram.filters.state import StateFilter


adduser = ADDUSER()
class Dialog(StateFilter):
    otvet = StateFilter()
    
@dp.message_handler(command='add_user')
async def start_adding(message: types.Message):
    await Dialog.otvet.states
    await message.reply('Введите ФИО')