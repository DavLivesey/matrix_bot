from aiogram.filters.callback_data import CallbackData

class ADDUSER(CallbackData, prefix='add_user'):
    fullname: str
    apteka: bool
    zkgu: bool
    bgu1: bool
    bgu2: bool
    dieta: bool
    mis: bool
    tis: bool
    sed: bool