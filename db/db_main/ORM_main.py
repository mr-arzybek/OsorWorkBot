import asyncpg
from db import sql_queris
from config import POSTGRES_URL

async def create_tables():
    connection = await asyncpg.connect(POSTGRES_URL)
    try:
        await connection.execute(sql_queris.CREATE_PRODUCT_COMING_TABLE_QUERY)
        await connection.execute(sql_queris.CREATE_PRODUCT_CARE_TABLE_QUERY)
        await connection.execute(sql_queris.CREATE_BOOKING_TABLE_QUERY)
        await connection.execute(sql_queris.CREATE_STAFF_TABLE_QUERY)
        await connection.execute(sql_queris.CREATE_BEING_LATE_TABLE_QUERY)

        print("База данных успешно подключена и таблицы созданы")
    finally:
        await connection.close()

async def sql_product_coming_insert(state):
    async with asyncpg.connect(POSTGRES_URL) as connection:
        async with state.proxy() as data:
            await connection.execute(sql_queris.PRODUCT_COMING_INSERT_QUERY, *data.values())

async def sql_command_all_products_coming():
    async with asyncpg.connect(POSTGRES_URL) as connection:
        return await connection.fetch("SELECT * FROM products_coming")

async def sql_command_delete_coming(id):
    id = int(id)
    async with asyncpg.connect(POSTGRES_URL) as connection:
        await connection.execute("DELETE FROM products_coming WHERE id = $1", id)

async def sql_product_care_insert(state):
    async with asyncpg.connect(POSTGRES_URL) as connection:
        async with state.proxy() as data:
            await connection.execute(sql_queris.PRODUCT_CARE_INSERT_QUERY, *data.values())

async def sql_command_all_products_care():
    async with asyncpg.connect(POSTGRES_URL) as connection:
        return await connection.fetch("SELECT * FROM products_care")

async def sql_command_delete_care(id):
    id = int(id)
    async with asyncpg.connect(POSTGRES_URL) as connection:
        await connection.execute("DELETE FROM products_care WHERE id = $1", id)

async def sql_booking_insert(state):
    async with asyncpg.connect(POSTGRES_URL) as connection:
        async with state.proxy() as data:
            await connection.execute(sql_queris.BOOKING_INSERT_QUERY, *data.values())

async def sql_command_all_booking():
    async with asyncpg.connect(POSTGRES_URL) as connection:
        return await connection.fetch("SELECT * FROM booking")

async def sql_command_delete_booking(id):
    id = int(id)
    async with asyncpg.connect(POSTGRES_URL) as connection:
        await connection.execute("DELETE FROM booking WHERE id = $1", id)

async def sql_staff_insert(state):
    async with asyncpg.connect(POSTGRES_URL) as connection:
        async with state.proxy() as data:
            await connection.execute(sql_queris.STAFF_INSERT_QUERY, *data.values())

async def sql_command_all_staff():
    async with asyncpg.connect(POSTGRES_URL) as connection:
        return await connection.fetch("SELECT * FROM staff")

async def sql_command_delete_staff(id):
    id = int(id)
    async with asyncpg.connect(POSTGRES_URL) as connection:
        await connection.execute("DELETE FROM staff WHERE id = $1", id)

async def sql_being_late_insert(state):
    async with asyncpg.connect(POSTGRES_URL) as connection:
        async with state.proxy() as data:
            await connection.execute(sql_queris.BEING_LATE_INSERT_QUERY, *data.values())
