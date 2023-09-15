# ====================================================================================================================
from aiogram import types, Dispatcher
from config import Admins, Director

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2


# ====================================================================================================================

async def sql_being_late_bishkek(message: types.Message):
    lateness = cursor_bish.execute("SELECT * FROM being_late").fetchall()

    for time in lateness:
        if message.from_user.id in Admins or Director:
            await message.answer(f'Данные: \n'
                                 f'ФИО: {time[1]}\n'
                                 f'Дата: {time[2]}\n'
                                 f'Время прибытия: {time[3]}\n'
                                 f'Город: {time[4]}')
        else:
            await message.answer('Вы не админ!')


async def sql_being_late_osh(message: types.Message):
    lateness = cursor_osh.execute("SELECT * FROM being_late").fetchall()

    for time in lateness:
        if message.from_user.id in Admins or Director:
            await message.answer(f'Данные: \n'
                                 f'ФИО: {time[1]}\n'
                                 f'Дата: {time[2]}\n'
                                 f'Время прибытия: {time[3]}\n'
                                 f'Город: {time[4]}')
        else:
            await message.answer('Вы не админ!')


async def sql_being_late_moscow_1(message: types.Message):
    lateness = cursor_moscow_1.execute("SELECT * FROM being_late").fetchall()

    for time in lateness:
        if message.from_user.id in Admins or Director:
            await message.answer(f'Данные: \n'
                                 f'ФИО: {time[1]}\n'
                                 f'Дата: {time[2]}\n'
                                 f'Время прибытия: {time[3]}\n'
                                 f'Город: {time[4]}')
        else:
            await message.answer('Вы не админ!')


async def sql_being_late_moscow_2(message: types.Message):
    lateness = cursor_moscow_2.execute("SELECT * FROM being_late").fetchall()

    for time in lateness:
        if message.from_user.id in Admins or Director:
            await message.answer(f'Данные: \n'
                                 f'ФИО: {time[1]}\n'
                                 f'Дата: {time[2]}\n'
                                 f'Время прибытия: {time[3]}\n'
                                 f'Город: {time[4]}')
        else:
            await message.answer('Вы не админ!')


# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_being_late_bishkek, commands=['Контроль_Бишкек'])
    dp.register_message_handler(sql_being_late_osh, commands=['Контроль_Ош'])
    dp.register_message_handler(sql_being_late_moscow_1, commands=['Контроль_Москва_1'])
    dp.register_message_handler(sql_being_late_moscow_2, commands=['Контроль_Москва_2'])
