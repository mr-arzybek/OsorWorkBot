import sqlite3
from . import sql_queries

db = sqlite3.connect("test.db")
cursor = db.cursor()


def sql_create():
    if db:
        print("Database connected")
    cursor.execute(sql_queries.CREATE_PRODUCT_TABLE_QUERY)
    cursor.execute(sql_queries.CREATE_BOOKING_TABLE_QUERY)
    db.commit()


async def sql_product_insert(state):
    async with state.proxy() as data:
        cursor.execute(sql_queries.PRODUCT_INSERT_QUERY, tuple(data.values()))
        db.commit()


async def sql_booking_insert(state):
    async with state.proxy() as data:
        cursor.execute(sql_queries.BOOKING_INSERT_QUERY, tuple(data.values()))
        db.commit()
