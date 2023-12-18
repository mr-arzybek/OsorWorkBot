from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.db_psql.db_osor import Database

# Инициализация хранилища для хранения состояний FSM
storage = MemoryStorage()

# Получение значения токена из переменной окружения
TOKEN = config('TOKEN')

# Список администраторов
Admins = [5676759336, 5676759336, 5676759336]

# Список директоров (если это нужно)
Director = [5676759336]



# Инициализация бота с использованием токена
bot = Bot(TOKEN)

# Инициализация диспетчера с использованием бота и хранилища
dp = Dispatcher(bot=bot, storage=storage)

# Получение значений из переменных окружения
ip = config('ip')
PostgresUser = config('PostgresUser')
PostgresPassword = config('PostgresPassword')
DATABASE = config('DATABASE')

# Формирование строки подключения к PostgreSQL
POSTGRES_URL = config('POSTGRES_URL', default="postgresql://postgres:123@127.0.0.1:5432/osor_tg_bot")

# Получение значения DESTINATION из переменной окружения
DESTINATION = config('DESTINATION')

# Инициализация объекта для работы с базой данных
data_b = Database(POSTGRES_URL)
