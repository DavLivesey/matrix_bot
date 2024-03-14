from aiogram import types
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError

from config import ADMIN_LIST
from loader import db, dp, bot


class DBCommands:
    pool: Connection = db
    ADD_NEW_USER
    EDIT_USER
    DELETE_USER
    CHECK_USER
    GET_FULLNAME
    GET_NAME