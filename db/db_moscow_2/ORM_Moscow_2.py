import sqlite3
from db.db_moscow_2 import sql_queris_moscow_2

db_moscow_2 = sqlite3.connect("db/db_moscow_2/Moscow_2.db")
cursor_moscow_2 = db_moscow_2.cursor()


def sql_create_moscow_2():
    if db_moscow_2:
        print("База Москва-2 подключена!")
    cursor_moscow_2.execute(sql_queris_moscow_2.CREATE_PRODUCT_COMING_TABLE_QUERY)
    cursor_moscow_2.execute(sql_queris_moscow_2.CREATE_PRODUCT_CARE_TABLE_QUERY)
    cursor_moscow_2.execute(sql_queris_moscow_2.CREATE_BOOKING_TABLE_QUERY)
    cursor_moscow_2.execute(sql_queris_moscow_2.CREATE_STAFF_TABLE_QUERY)
    cursor_moscow_2.execute(sql_queris_moscow_2.CREATE_BEING_LATE_TABLE_QUERY)
    db_moscow_2.commit()


async def moscow_2_sql_product_coming_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.PRODUCT_COMING_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


""" Удаление прихода товаров из базы! """


async def sql_command_all_products_coming():
    return cursor_moscow_2.execute("SELECT * FROM products_coming").fetchall()


async def sql_command_delete_coming(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_2.execute("DELETE FROM products_coming WHERE id = ?", (id,))

    db_moscow_2.commit()


"""========================"""


async def moscow_2_sql_product_care_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.PRODUCT_CARE_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


""" Удаление из базы! """


async def sql_command_all_products_care():
    return cursor_moscow_2.execute("SELECT * FROM products_care").fetchall()


async def sql_command_delete_care(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_2.execute("DELETE FROM products_care WHERE id = ?", (id,))

    db_moscow_2.commit()


"""========================"""


async def moscow_2_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


""" Удаление броней товаров из базы! """


async def sql_command_all_booking():
    return cursor_moscow_2.execute("SELECT * FROM booking").fetchall()


async def sql_command_delete_booking(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_2.execute("DELETE FROM booking WHERE id = ?", (id,))

    db_moscow_2.commit()


"""========================"""


async def moscow_2_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.STAFF_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()

""" Удаление сотрудников из базы! """


async def sql_command_all_staff():
    return cursor_moscow_2.execute("SELECT * FROM staff").fetchall()


async def sql_command_delete_staff(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_moscow_2.execute("DELETE FROM staff WHERE id = ?", (id,))

    db_moscow_2.commit()


"""========================"""

async def moscow_2_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()
