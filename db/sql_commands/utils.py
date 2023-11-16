def update_product_coming_quantity(cursor, quantity, articul):
    cursor.execute("""UPDATE products_coming
    SET quantity = quantity - ?
    WHERE articul = ?""", (quantity, articul))


def get_product_from_category(cursor, category, city):
    try:
        cursor.execute("""SELECT * FROM products_coming
                        WHERE category = ? AND city = ?""", (category, city))
        products = cursor.fetchall()
        return products
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None


def get_product_from_articul(cursor, articul, city):
    try:
        cursor.execute("""SELECT name_, info_product, photo FROM products_coming
                        WHERE articul = ? AND city = ?""", (articul, city))
        product = cursor.fetchone()
        return product
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None