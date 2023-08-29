import sqlite3
from db.db_bish import sql_queris_bish

db_bish = sqlite3.connect("db/db_bish/Bishkek_db")
cursor_bish = db_bish.cursor()


def sql_create_bish():
    if db_bish:
        print("База Бишкек подключена!")
    cursor_bish.execute(sql_queris_bish.CREATE_PRODUCT_TABLE_QUERY)
    cursor_bish.execute(sql_queris_bish.CREATE_BOOKING_TABLE_QUERY)
    cursor_bish.execute(sql_queris_bish.CREATE_STAFF_TABLE_QUERY)
    db_bish.commit()



async def bish_sql_product_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris_bish.PRODUCT_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


async def bish_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris_bish.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


async def bish_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris_bish.STAFF_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()


async def bish_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_bish.execute(sql_queris_bish.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_bish.commit()