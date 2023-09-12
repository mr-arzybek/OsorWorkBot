import sqlite3
from db import sql_queris
from config import Director
from aiogram import types

db_bish = sqlite3.connect("db/db_bish/Bishkek_db")
cursor_bish = db_bish.cursor()


def sql_create_bish():
    if db_bish:
        print("База Бишкек подключена!")
    cursor_bish.execute(sql_queris.CREATE_PRODUCT_COMING_TABLE_QUERY)
    cursor_bish.execute(sql_queris.CREATE_PRODUCT_CARE_TABLE_QUERY)
    cursor_bish.execute(sql_queris.CREATE_BOOKING_TABLE_QUERY)
    cursor_bish.execute(sql_queris.CREATE_STAFF_TABLE_QUERY)
    cursor_bish.execute(sql_queris.CREATE_BEING_LATE_TABLE_QUERY)
    db_bish.commit()


async def bish_sql_product_coming_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris.PRODUCT_COMING_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


""" Удаление прихода товаров из базы! """


async def sql_command_all_products_coming():
    return cursor_bish.execute("SELECT * FROM products_coming").fetchall()


async def sql_command_delete_coming(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_bish.execute("DELETE FROM products_coming WHERE id = ?", (id,))

    db_bish.commit()


"""========================"""


async def bish_sql_product_care_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris.PRODUCT_CARE_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


""" Удаление из базы! """


async def sql_command_all_products_care():
    return cursor_bish.execute("SELECT * FROM products_care").fetchall()


async def sql_command_delete_care(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_bish.execute("DELETE FROM products_care WHERE id = ?", (id,))

    db_bish.commit()


"""========================"""


async def bish_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


""" Удаление броней товаров из базы! """


async def sql_command_all_booking():
    return cursor_bish.execute("SELECT * FROM booking").fetchall()


async def sql_command_delete_booking(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_bish.execute("DELETE FROM booking WHERE id = ?", (id,))

    db_bish.commit()


"""========================"""


async def bish_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris.STAFF_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


""" Удаление сотрудников из базы! """


async def sql_command_all_staff():
    return cursor_bish.execute("SELECT * FROM staff").fetchall()


async def sql_command_delete_staff(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_bish.execute("DELETE FROM staff WHERE id = ?", (id,))

    db_bish.commit()


"""========================"""


async def bish_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()
