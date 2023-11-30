from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database


storage = MemoryStorage()

TOKEN = config('TOKEN')

Admins = [659106628, 659106628]

Director = [659106628, ]
bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)


# ip = config('ip')
# PostgresUser = config('PostgresUser')
# PostgresPassword = config('PostgresPassword')
# DATABASE = config('DATABASE')

POSTGRES_URL = "postgresql://postgres:238484@db:5432/OSOR_DB"

data_b = Database(POSTGRES_URL)


