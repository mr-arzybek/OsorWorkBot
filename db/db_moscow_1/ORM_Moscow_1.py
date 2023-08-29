import sqlite3
from db.db_moscow_1 import sql_queris_moscow_1

db_moscow_1 = sqlite3.connect("db/db_moscow_1/Moscow_1.db")
cursor_moscow_1 = db_moscow_1.cursor()


def sql_create_moscow_1():
    if db_moscow_1:
        print("База Москва-1 подключена!")
    cursor_moscow_1.execute(sql_queris_moscow_1.CREATE_PRODUCT_TABLE_QUERY)
    cursor_moscow_1.execute(sql_queris_moscow_1.CREATE_BOOKING_TABLE_QUERY)
    cursor_moscow_1.execute(sql_queris_moscow_1.CREATE_STAFF_TABLE_QUERY)
    db_moscow_1.commit()


async def moscow_1_sql_product_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris_moscow_1.PRODUCT_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()


async def moscow_1_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris_moscow_1.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()


async def moscow_1_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris_moscow_1.STAFF_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()


async def moscow_1_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_moscow_1.execute(sql_queris_moscow_1.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_moscow_1.commit()
