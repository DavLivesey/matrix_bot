from aiogram import types, F, Router
from ..main import DBCommands
from .data import ADDUSER
from loader import dp
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()
#adduser = ADDUSER()
class Dialog(StatesGroup):
    answer = State()
    
@router.message(Command('add_fullname'))
async def start_adding(message: types.Message, state: FSMContext):
    print('urra')
    await Dialog.otvet.states
    await message.reply('Введите ФИО')
    await state.set_data(Dialog.answer)