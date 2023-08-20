CREATE_PRODUCT_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products
    (id INTEGER PRIMARY KEY,
    name_ VARCHAR(255),
    date_coming VARCHAR(15),
    date_care VARCHAR(15),
    city VARCHAR(30) 
    )
"""

PRODUCT_INSERT_QUERY = """
    INSERT OR IGNORE INTO products (name_, date_coming, date_care, city) VALUES (?,?,?,?)
"""

CREATE_BOOKING_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS bookings 
    (id INTEGER PRIMARY KEY,
    name_product VARCHAR(255),
    start_of_armor VARCHAR(20),
    end_of_armor VARCHAR(20),
    name_customer VARCHAR(255),
    name_salesman VARCHAR(255),
    city VARCHAR(20)
    )
"""

BOOKING_INSERT_QUERY = """
    INSERT OR IGNORE INTO bookings 
    (name_product, start_of_armor, end_of_armor, name_customer, name_salesman, city)
    VALUES (?,?,?,?,?,?)
"""