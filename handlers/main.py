from aiogram import types
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError

from config import ADMIN_LIST
from loader import db, dp, bot


class DBCommands:
    pool: Connection = db
    ADD_NEW_USER = 'INSERT INTO users(fullname, ) ' \
                    'VALUES ($1) RETURNING ID'
    DELETE_USER = 'DELETE FROM users WHERE id=$1'
    CHECK_USER = 'SELECT id FROM users WHERE fullname=$1'
    ADD_APTEKA = 'UPDATE user SET 1C_APTEKA=True where id=$1'
    ADD_HR = 'UPDATE user SET 1C_ZKGU=True where id=$1'
    ADD_BGU_1 = 'UPDATE user SET 1С_BGU_1=True where id=$1'
    ADD_BGU_2 = 'UPDATE user SET 1С_BGU_2=True where id=$1'
    ADD_1С_DIETA = 'UPDATE user SET 1С_DIETA=True where id=$1'
    ADD_MIS = 'UPDATE user SET MIS=True where id=$1'
    ADD_TIS = 'UPDATE user SET TIS=True where id=$1'
    ADD_SED = 'UPDATE user SET SED=True where id=$1'
    DELETE_APTEKA = 'UPDATE user SET 1C_APTEKA=False where id=$1'
    DELETE_HR = 'UPDATE user SET 1C_ZKGU=False where id=$1'
    DELETE_BGU_1 = 'UPDATE user SET 1С_BGU_1=False where id=$1'
    DELETE_BGU_2 = 'UPDATE user SET 1С_BGU_2=False where id=$1'
    DELETE_1С_DIETA = 'UPDATE user SET 1С_DIETA=False where id=$1'
    DELETE_MIS = 'UPDATE user SET MIS=False where id=$1'
    DELETE_TIS = 'UPDATE user SET TIS=False where id=$1'
    DELETE_SED = 'UPDATE user SET SED=False where id=$1'
    

    async def add_new_user(self, fullname):
        command = self.ADD_NEW_USER
        await self.pool.fetchval(command)
