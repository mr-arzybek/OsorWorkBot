import sqlite3
import sql_queries


def db_connect():
    global db, cursor

    with sqlite3.connect("bish.db") as db:
        cursor = db.cursor()

        if db:
            print("Database connected")
            db.execute(sql_queries.CREATE_PRODUCT_TABLE_QUERY)

        db.commit()


async def sql_product_insert(state):
    async with state.proxy() as data:
        cursor.execute(sql_queries.PRODUCT_INSERT_QUERY, tuple(data.values()))
        db.commit()
