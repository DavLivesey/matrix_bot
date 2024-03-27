import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.callbacks.admins import router

import config
from sql import create_pool

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s'
                           u'[%(asctime)s]  %(message)s',
                    level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()
db = loop.run_until_complete(create_pool())
dp.include_routers(router)