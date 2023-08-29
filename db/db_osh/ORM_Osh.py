import sqlite3
from db.db_osh import sql_queris_osh

db_osh = sqlite3.connect("db/db_osh/osh.db")
cursor_osh = db_osh.cursor()


def sql_create_osh():
    if db_osh:
        print("База Ош подключена!")
    cursor_osh.execute(sql_queris_osh.CREATE_PRODUCT_TABLE_QUERY)
    cursor_osh.execute(sql_queris_osh.CREATE_BOOKING_TABLE_QUERY)
    cursor_osh.execute(sql_queris_osh.CREATE_STAFF_TABLE_QUERY)
    db_osh.commit()


async def osh_sql_product_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.PRODUCT_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()


async def osh_sql_booking_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.BOOKING_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()


async def osh_sql_staff_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.STAFF_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()

async def osh_sql_being_late_insert(state):
    async with state.proxy() as data:
        cursor_osh.execute(sql_queris_osh.BEING_LATE_INSERT_QUERY, tuple(data.values()))
        db_osh.commit()
