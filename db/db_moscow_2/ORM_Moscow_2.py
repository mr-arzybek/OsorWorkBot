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
    db_moscow_2.commit()


async def moscow_2_sql_product_coming_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.PRODUCT_COMING_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


async def moscow_2_sql_product_care_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.PRODUCT_CARE_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


async def moscow_2_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


async def moscow_2_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.STAFF_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()


async def moscow_2_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_moscow_2.execute(sql_queris_moscow_2.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_moscow_2.commit()
