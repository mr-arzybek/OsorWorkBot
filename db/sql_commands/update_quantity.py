
def update_product_coming_quantity(cursor, quantity, articul):
    cursor.execute("""UPDATE products_coming
    SET quantity = quantity - ?
    WHERE articul = ?""", (quantity, articul))
