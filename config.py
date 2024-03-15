import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_LIST = [int(os.getenv('ADMIN_1')), int(os.getenv('ADMIN_2'))]
HOST = os.getenv('HOST')
PG_PSWD = os.getenv('PG_PSWD')
PG_USER = os.getenv('PG_USER')

