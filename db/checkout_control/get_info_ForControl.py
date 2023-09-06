from aiogram import Dispatcher
from config import bot
from db.db_bish.ORM_Bish import cursor_bish


import sqlite3
import datetime

# Открываем соединение с базой данных
# conn = sqlite3.connect('your_database.db')
# cursor = conn.cursor()

# Получаем начало текущего месяца
today = datetime.date.today()
start_of_month = today.replace(day=1)

# Выполняем запрос к базе данных
cursor_bish.execute("SELECT * FROM records WHERE date >= ?", (start_of_month,))
records = cursor_bish.fetchall()

# Здесь можно отправить записи, например, по электронной почте или сохранить их в файл


