async def update_product_coming_quantity(pool, quantity, articul):
    try:
        async with pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(
                    """UPDATE products_coming
                       SET quantity = quantity - $1
                       WHERE articul = $2""",
                    quantity, articul
                )
    except Exception as e:
        print(f"Error executing SQL query: {e}")



async def get_product_from_category(cursor, category, city):
    try:
        async with cursor.transaction():
            products = await cursor.fetch(
                """SELECT * FROM products_coming
                WHERE category = $1 AND city = $2""",
                category, city
            )
            return products
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None

async def get_product_from_articul(cursor, articul, city):
    try:
        # Выполняем запрос с использованием асинхронного соединения
        result = await cursor.fetchrow(
            """SELECT name_, info_product, photo FROM products_coming
            WHERE articul = $1 AND city = $2""",
            articul, city
        )
        return result
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None
