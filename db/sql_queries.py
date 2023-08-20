CREATE_PRODUCT_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    date_coming VARCHAR(15),
    date_care VARCHAR(15),
    city VARCHAR(30) 
    )
"""

PRODUCT_INSERT_QUERY = """
    INSERT OR IGNORE INTO products VALUES (?,?,?,?,?)
"""