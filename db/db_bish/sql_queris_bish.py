# =======================================================================================================================

CREATE_PRODUCT_COMING_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products_coming
    (name_ VARCHAR(255),
    info_product VARCHAR(255),
    date_coming VARCHAR(15),
    price DECIMAL(10, 2),
    city VARCHAR(50), 
    photo TEXT,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

PRODUCT_COMING_INSERT_QUERY = """
    INSERT OR IGNORE INTO products_coming
    (name_, info_product, date_coming, price, city, photo, creation_time)
    VALUES (?,?,?,?,?,?,?)
"""


CREATE_PRODUCT_CARE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS products_care
    (name_ VARCHAR(255),
    info_product VARCHAR(255),
    date_care VARCHAR(15),
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
    )
"""

PRODUCT_CARE_INSERT_QUERY = """
    INSERT OR IGNORE INTO products_care
    (name_, info_product, date_care, name_customer, phone_customer, name_salesman, phone_salesman, price, discount, total_price, city, photo, 
    creation_time)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
"""

# =======================================================================================================================

CREATE_BOOKING_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS booking
    (name_product VARCHAR(255),
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
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
"""

BOOKING_INSERT_QUERY = """
    INSERT OR IGNORE INTO booking  
    (name_product, start_of_armor, end_of_armor, name_customer, phone_customer, name_salesman, phone_salesman, price, discount, total_price, city, photo,
    creation_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# =======================================================================================================================

CREATE_STAFF_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS staff
    (full_name_staff VARCHAR(255),
    phone_staff VARCHAR(50) UNIQUE,
    info_staff VARCHAR(255),
    schedule_staff VARCHAR(255),
    city_staff VARCHAR(50),
    photo TEXT,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

STAFF_INSERT_QUERY = """
    INSERT OR IGNORE INTO staff  
    (full_name_staff, phone_staff, info_staff, schedule_staff, city_staff, photo, creation_time)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

# =======================================================================================================================

CREATE_BEING_LATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS being_late
    (full_name VARCHAR(255),
    date_ VARCHAR(50),
    time_ VARCHAR(255),
    city VARCHAR(50),
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""

BEING_LATE_INSERT_QUERY = """
    INSERT OR IGNORE INTO being_late  
    (full_name, date_, time_, city, creation_time)
    VALUES (?,?,?,?,?)
"""


CREATE_SALARY_TABLE_QUERY = """
    
"""

SALARY_INSERT_QUERY = """
    
"""