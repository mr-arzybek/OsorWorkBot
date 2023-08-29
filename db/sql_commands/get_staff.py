# ====================================================================================================================
from aiogram import types, Dispatcher

from db.db_bish.ORM_Bish import cursor_bish
from db.db_osh.ORM_Osh import cursor_osh
from db.db_moscow_1.ORM_Moscow_1 import cursor_moscow_1
from db.db_moscow_2.ORM_Moscow_2 import cursor_moscow_2

# ====================================================================================================================

async def sql_command_staff_bishkek(message: types.Message):
    cursor_bish.execute("SELECT * FROM staff")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        employees = cursor_bish.fetchmany(batch_size)
        if not employees:
            break

        for staff in employees:
            await message.answer(f"Имя {staff[0]}\n"
                                 f"Номер тел: {staff[1]}\n"
                                 f"График: {staff[2]}\n"
                                 f"Филиал: {staff[3]}")


async def sql_command_staff_osh(message: types.Message):
    cursor_osh.execute("SELECT * FROM staff")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        employees = cursor_osh.fetchmany(batch_size)
        if not employees:
            break

        for staff in employees:
            await message.answer(f"Имя {staff[0]}\n"
                                 f"Номер тел: {staff[1]}\n"
                                 f"График: {staff[2]}\n"
                                 f"Филиал: {staff[3]}")


async def sql_command_staff_moscow_1(message: types.Message):
    cursor_moscow_1.execute("SELECT * FROM staff")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        employees = cursor_moscow_1.fetchmany(batch_size)
        if not employees:
            break

        for staff in employees:
            await message.answer(f"Имя {staff[0]}\n"
                                 f"Номер тел: {staff[1]}\n"
                                 f"График: {staff[2]}\n"
                                 f"Филиал: {staff[3]}")


async def sql_command_staff_moscow_2(message: types.Message):
    cursor_moscow_2.execute("SELECT * FROM staff")

    batch_size = 5  # Количество записей (людей) для извлечения
    while True:
        employees = cursor_moscow_2.fetchmany(batch_size)
        if not employees:
            break

        for staff in employees:
            await message.answer(f"Имя {staff[0]}\n"
                                 f"Номер тел: {staff[1]}\n"
                                 f"График: {staff[2]}\n"
                                 f"Филиал: {staff[3]}")

# ====================================================================================================================

def register_sql_commands(dp: Dispatcher):
    dp.register_message_handler(sql_command_staff_bishkek, commands=['Сотрудники_Бишкек'])
    dp.register_message_handler(sql_command_staff_osh, commands=['Сотрудники_Ош'])
    dp.register_message_handler(sql_command_staff_moscow_1, commands=['Сотрудники_Москва_1'])
    dp.register_message_handler(sql_command_staff_moscow_2, commands=['Сотрудники_Москва_2'])
