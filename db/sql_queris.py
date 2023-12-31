CREATE_PRODUCT_COMING_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products_coming (
        id SERIAL PRIMARY KEY,
        name_ VARCHAR(255),
        info_product VARCHAR(255),
        date_coming VARCHAR(255),
        price DECIMAL(10, 2),
        city VARCHAR(50), 
        category VARCHAR(50),
        articul TEXT,
        quantity INTEGER,
        photo TEXT,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

PRODUCT_COMING_INSERT_QUERY = """
    INSERT INTO products_coming
        (name_, info_product, date_coming, price, city, category, articul, quantity, photo, creation_time)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, CURRENT_TIMESTAMP)
    ON CONFLICT DO NOTHING;
"""

CREATE_PRODUCT_CARE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products_care (
        id SERIAL PRIMARY KEY,
        date_care VARCHAR(255),
        name_customer VARCHAR(255),
        phone_customer VARCHAR(50),
        name_salesman VARCHAR(255),
        phone_salesman VARCHAR(50),
        price DECIMAL(10, 2),
        discount INTEGER,
        total_price INTEGER,
        city VARCHAR(50), 
        articul TEXT,
        quantity INTEGER,
        photo TEXT,
        name_ VARCHAR(255),
        info_product VARCHAR(255),
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

PRODUCT_CARE_INSERT_QUERY = """
    INSERT INTO products_care
        (date_care, name_customer, phone_customer, name_salesman,
         phone_salesman, price, discount, total_price, city, articul, quantity, photo, name_, info_product,
        creation_time)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, CURRENT_TIMESTAMP)
    ON CONFLICT DO NOTHING;
"""

CREATE_BOOKING_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS booking (
        id SERIAL PRIMARY KEY,
        name_product VARCHAR(255),
        start_of_armor VARCHAR(255),
        end_of_armor VARCHAR(255),
        name_customer VARCHAR(255),
        phone_customer VARCHAR(50),
        name_salesman VARCHAR(255),
        phone_salesman VARCHAR(50),
        price DECIMAL(10, 2),
        discount INTEGER,
        total_price INTEGER,
        city VARCHAR(50),
        photo TEXT,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

BOOKING_INSERT_QUERY = """
    INSERT INTO booking
        (name_product, start_of_armor, end_of_armor, name_customer, phone_customer, name_salesman, phone_salesman, price, discount, total_price, city, photo,
        creation_time)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, CURRENT_TIMESTAMP)
    ON CONFLICT DO NOTHING;
"""

CREATE_STAFF_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS staff (
        id SERIAL PRIMARY KEY,
        full_name_staff VARCHAR(255),
        phone_staff VARCHAR(50) UNIQUE,
        info_staff VARCHAR(255),
        schedule_staff VARCHAR(255),
        city_staff VARCHAR(50),
        photo TEXT,
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

STAFF_INSERT_QUERY = """
    INSERT INTO staff
        (full_name_staff, phone_staff, info_staff, schedule_staff, city_staff, photo, creation_time)
    VALUES ($1, $2, $3, $4, $5, $6, CURRENT_TIMESTAMP)
    ON CONFLICT (phone_staff) DO NOTHING;
"""

CREATE_BEING_LATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS being_late (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255),
        date_ VARCHAR(255),
        time_ VARCHAR(255),
        city VARCHAR(50),
        creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

BEING_LATE_INSERT_QUERY = """
    INSERT INTO being_late
        (full_name, date_, time_, city, creation_time)
    VALUES ($1, $2, $3, $4, CURRENT_TIMESTAMP)
    ON CONFLICT DO NOTHING;
"""
