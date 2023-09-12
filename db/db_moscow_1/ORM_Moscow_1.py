import sqlite3
from db import sql_queris

db_moscow_1 = sqlite3.connect("db/db_moscow_1/Moscow_1.db")
cursor_moscow_1 = db_moscow_1.cursor()


def sql_create_moscow_1():
    if db_moscow_1:
        print("База Москва-1 подключена!")
    cursor_moscow_1.execute(sql_queris.CREATE_PRODUCT_COMING_TABLE_QUERY)
    cursor_moscow_1.execute(sql_queris.CREATE_PRODUCT_CARE_TABLE_QUERY)
    cursor_moscow_1.execute(sql_queris.CREATE_BOOKING_TABLE_QUERY)
    cursor_moscow_1.execute(sql_queris.CREATE_STAFF_TABLE_QUERY)
    cursor_moscow_1.execute(sql_queris.CREATE_BEING_LATE_TABLE_QUERY)
    db_moscow_1.commit()


async def moscow_1_sql_product_coming_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris.PRODUCT_COMING_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()

""" Удаление прихода товаров из базы! """

async def sql_command_all_products_coming():
    return cursor_moscow_1.execute("SELECT * FROM products_coming").fetchall()


async def sql_command_delete_coming(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_1.execute("DELETE FROM products_coming WHERE id = ?", (id,))

    db_moscow_1.commit()


"""========================"""

async def moscow_1_sql_product_care_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris.PRODUCT_CARE_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()

""" Удаление из базы! """

async def sql_command_all_products_care():
    return cursor_moscow_1.execute("SELECT * FROM products_care").fetchall()


async def sql_command_delete_care(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_1.execute("DELETE FROM products_care WHERE id = ?", (id,))

    db_moscow_1.commit()


"""========================"""

async def moscow_1_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()


""" Удаление броней товаров из базы! """


async def sql_command_all_booking():
    return cursor_moscow_1.execute("SELECT * FROM booking").fetchall()


async def sql_command_delete_booking(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_1.execute("DELETE FROM booking WHERE id = ?", (id,))

    db_moscow_1.commit()


"""========================"""


async def moscow_1_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris.STAFF_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()

""" Удаление сотрудников из базы! """


async def sql_command_all_staff():
    return cursor_moscow_1.execute("SELECT * FROM staff").fetchall()


async def sql_command_delete_staff(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_1.execute("DELETE FROM staff WHERE id = ?", (id,))

    db_moscow_1.commit()


"""========================"""



async def moscow_1_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()
