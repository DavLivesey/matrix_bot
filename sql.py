import asyncio
import logging
from syslog import LOG_PERROR
import time
import asyncpg
from config import HOST, PG_PSWD, PG_USER

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s'
                           u'[%(asctime)s]  %(message)s',
                    level=logging.INFO)

async def create_db():
    create_db_command = open('/home/BLOOD.LOCAL/admin_sz/Projects/matrix_bot/create_dbl.sql', 'r').read()
    logging.info('Connection to db...')
    conn: asyncpg.Connection = await asyncpg.connect(
        user=PG_USER,
        password=PG_PSWD,
        host=HOST
    )
    await conn.execute(create_db_command)
    logging.info('Table was created')
    await conn.close()


async def create_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PG_PSWD,
        host=HOST
    )


if __name__ == '__main__':
    while True:
        try:
            loop.run_until_complete(create_db())
        except:
            time.sleep(5)
        loop = asyncio.get_event_loop()