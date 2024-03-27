import asyncio
import logging
import sqlite3
from config import HOST, PG_PSWD, PG_USER

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s'
                           u'[%(asctime)s]  %(message)s',
                    level=logging.INFO)

async def create_db():
    create_db_command = open('/home/BLOOD.LOCAL/admin_sz/Projects/matrix_bot/create_dbl.sql', 'r').read()
    logging.info('Connection to db...')
    conn = sqlite3.connect ('users.db')
    cur = conn.cursor('')
    await cur.execute(create_db_command)
    logging.info('Table was created')
    await conn.close()


async def create_pool():
    return sqlite3.connect('users.db')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_pool())
