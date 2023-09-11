import sqlite3
from db.db_osh import sql_queris_osh

db_osh = sqlite3.connect("db/db_osh/osh.db")
cursor_osh = db_osh.cursor()


def sql_create_osh():
    if db_osh:
        print("База Ош подключена!")
    cursor_osh.execute(sql_queris_osh.CREATE_PRODUCT_COMING_TABLE_QUERY)
    cursor_osh.execute(sql_queris_osh.CREATE_PRODUCT_CARE_TABLE_QUERY)
    cursor_osh.execute(sql_queris_osh.CREATE_BOOKING_TABLE_QUERY)
    cursor_osh.execute(sql_queris_osh.CREATE_STAFF_TABLE_QUERY)
    cursor_osh.execute(sql_queris_osh.CREATE_BEING_LATE_TABLE_QUERY)
    db_osh.commit()


async def osh_sql_product_coming_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.PRODUCT_COMING_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()

""" Удаление прихода товаров из базы! """

async def sql_command_all_products_coming():
    return cursor_osh.execute("SELECT * FROM products_coming").fetchall()


async def sql_command_delete_coming(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_osh.execute("DELETE FROM products_coming WHERE id = ?", (id,))

    db_osh.commit()


"""========================"""

async def osh_sql_product_care_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.PRODUCT_CARE_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()

""" Удаление из базы! """

async def sql_command_all_products_care():
    return cursor_osh.execute("SELECT * FROM products_care").fetchall()


async def sql_command_delete_care(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_osh.execute("DELETE FROM products_care WHERE id = ?", (id,))

    db_osh.commit()


"""========================"""


async def osh_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()



""" Удаление броней товаров из базы! """


async def sql_command_all_booking():
    return cursor_osh.execute("SELECT * FROM booking").fetchall()


async def sql_command_delete_booking(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_osh.execute("DELETE FROM booking WHERE id = ?", (id,))

    db_osh.commit()


"""========================"""


async def osh_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.STAFF_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()

""" Удаление сотрудников из базы! """


async def sql_command_all_staff():
    return cursor_osh.execute("SELECT * FROM staff").fetchall()


async def sql_command_delete_staff(id):
    id = int(id)  # Преобразовать id в целое число

    cursor_osh.execute("DELETE FROM staff WHERE id = ?", (id,))

    db_osh.commit()


"""========================"""

async def osh_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()
