# ====================================================================================================================
from aiogram import types, Dispatcher
from config import bot, Admins

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2


# ====================================================================================================================

async def sql_command_staff_bishkek(message: types.Message):
    employees = cursor_bish.execute("SELECT * FROM staff").fetchall()

    for staff in employees:
        if message.from_user.id in Admins:
            await bot.send_photo(message.from_user.id, photo=staff[5], caption=f"Имя {staff[0]}\n"
                                                                               f"Номер тел: {staff[1]}\n"
                                                                               f"Информация о сотруднике: {staff[2]}"
                                                                               f"График: {staff[3]}\n"
                                                                               f"Филиал: {staff[4]}")
        else:
            await message.answer("Вы не админ!")


async def sql_command_staff_osh(message: types.Message):
    employees = cursor_osh.execute("SELECT * FROM staff").fetchall()

    for staff in employees:
        if message.from_user.id in Admins:
            await bot.send_photo(message.from_user.id, photo=staff[5], caption=f"Имя {staff[0]}\n"
                                                                               f"Номер тел: {staff[1]}\n"
                                                                               f"Информация о сотруднике: {staff[2]}"
                                                                               f"График: {staff[3]}\n"
                                                                               f"Филиал: {staff[4]}")
        else:
            await message.answer("Вы не админ!")


async def sql_command_staff_moscow_1(message: types.Message):
    cursor_moscow_1.execute("SELECT * FROM staff")
    employees = cursor_moscow_1.execute("SELECT * FROM staff").fetchall()

    for staff in employees:
        if message.from_user.id:
            await bot.send_photo(message.from_user.id, photo=staff[5], caption=f"Имя {staff[0]}\n"
                                                                               f"Номер тел: {staff[1]}\n"
                                                                               f"Информация о сотруднике: {staff[2]}"
                                                                               f"График: {staff[3]}\n"
                                                                               f"Филиал: {staff[4]}")
        else:
            await message.answer("Вы не админ!")


async def sql_command_staff_moscow_2(message: types.Message):
    employees = cursor_moscow_2.execute("SELECT * FROM staff").fetchall()

    for staff in employees:
        if message.from_user.id in Admins:
            await bot.send_photo(message.from_user.id, photo=staff[5], caption=f"Имя {staff[0]}\n"
                                                                               f"Номер тел: {staff[1]}\n"
                                                                               f"Информация о сотруднике: {staff[2]}"
                                                                               f"График: {staff[3]}\n"
                                                                               f"Филиал: {staff[4]}")
        else:
            await message.answer("Вы не админ!")

# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_staff_bishkek, commands=['Сотрудники_Бишкек'])
    dp.register_message_handler(sql_command_staff_osh, commands=['Сотрудники_Ош'])
    dp.register_message_handler(sql_command_staff_moscow_1, commands=['Сотрудники_Москва_1'])
    dp.register_message_handler(sql_command_staff_moscow_2, commands=['Сотрудники_Москва_2'])
