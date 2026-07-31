-- ==========================================================
-- Retail Data Warehouse
-- Create Dimension Tables
-- ==========================================================

SET search_path TO bronze;

-- ==========================================================
-- Dimension Date
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_date (

    date_key INTEGER PRIMARY KEY,

    full_date DATE NOT NULL,

    day SMALLINT NOT NULL,

    day_name VARCHAR(20),

    day_of_week SMALLINT,

    week_of_year SMALLINT,

    month SMALLINT,

    month_name VARCHAR(20),

    quarter VARCHAR(2),

    semester SMALLINT,

    year SMALLINT,

    is_weekend BOOLEAN,

    is_holiday BOOLEAN,

    holiday_name VARCHAR(100)

);

-- ==========================================================
-- Dimension Category
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_category (

    category_key INTEGER PRIMARY KEY,

    category_code VARCHAR(20) NOT NULL,

    category_name VARCHAR(100) NOT NULL,

    is_active BOOLEAN

);

-- ==========================================================
-- Dimension Brand
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_brand (

    brand_key INTEGER PRIMARY KEY,

    brand_code VARCHAR(20),

    brand_name VARCHAR(100),

    category_key INTEGER,

    category_name VARCHAR(100)

);

-- ==========================================================
-- Dimension Store
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_store (

    store_key INTEGER PRIMARY KEY,

    store_code VARCHAR(20) UNIQUE,

    store_name VARCHAR(200),

    store_type VARCHAR(50),

    city VARCHAR(100),

    province VARCHAR(100),

    address TEXT,

    phone VARCHAR(50),

    opening_date DATE,

    manager_name VARCHAR(150),

    is_active BOOLEAN

);

-- ==========================================================
-- Dimension Supplier
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_supplier (

    supplier_key INTEGER PRIMARY KEY,

    supplier_code VARCHAR(20) UNIQUE,

    supplier_name VARCHAR(200),

    contact_person VARCHAR(150),

    email VARCHAR(150),

    phone VARCHAR(50),

    city VARCHAR(100),

    province VARCHAR(100),

    address TEXT,

    is_active BOOLEAN

);

-- ==========================================================
-- Dimension Customer
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_customer (

    customer_key INTEGER PRIMARY KEY,

    customer_code VARCHAR(20) UNIQUE,

    first_name VARCHAR(100),

    last_name VARCHAR(100),

    gender VARCHAR(20),

    birth_date DATE,

    email VARCHAR(150),

    phone VARCHAR(50),

    city VARCHAR(100),

    province VARCHAR(100),

    membership VARCHAR(30),

    segment VARCHAR(30),

    register_date DATE,

    is_active BOOLEAN

);

-- ==========================================================
-- Dimension Employee
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_employee (

    employee_key INTEGER PRIMARY KEY,

    employee_code VARCHAR(20) UNIQUE,

    employee_name VARCHAR(150),

    gender VARCHAR(20),

    position VARCHAR(100),

    salary NUMERIC(18,2),

    hire_date DATE,

    email VARCHAR(150),

    phone VARCHAR(50),

    store_key INTEGER,

    is_active BOOLEAN,

    CONSTRAINT fk_employee_store
        FOREIGN KEY (store_key)
        REFERENCES dim_store(store_key)

);

-- ==========================================================
-- Dimension Payment
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_payment (

    payment_key INTEGER PRIMARY KEY,

    payment_code VARCHAR(20) UNIQUE,

    payment_method VARCHAR(50),

    provider VARCHAR(100),

    is_active BOOLEAN

);

-- ==========================================================
-- Dimension Promotion
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_promotion (

    promotion_key INTEGER PRIMARY KEY,

    promotion_code VARCHAR(20) UNIQUE,

    promotion_name VARCHAR(150),

    promotion_type VARCHAR(50),

    discount_percent NUMERIC(5,2),

    minimum_purchase NUMERIC(18,2),

    maximum_discount NUMERIC(18,2),

    start_date DATE,

    end_date DATE,

    is_active BOOLEAN

);

-- ==========================================================
-- Dimension Product
-- ==========================================================

CREATE TABLE IF NOT EXISTS dim_product (

    product_key INTEGER PRIMARY KEY,

    product_code VARCHAR(20) UNIQUE,

    product_name VARCHAR(200),

    category_key INTEGER,

    brand_key INTEGER,

    unit VARCHAR(30),

    color VARCHAR(50),

    size VARCHAR(50),

    storage VARCHAR(50),

    weight_gram INTEGER,

    cost_price NUMERIC(18,2),

    selling_price NUMERIC(18,2),

    tax_percent NUMERIC(5,2),

    status VARCHAR(30),

    is_active BOOLEAN,

    CONSTRAINT fk_product_category
        FOREIGN KEY (category_key)
        REFERENCES dim_category(category_key),

    CONSTRAINT fk_product_brand
        FOREIGN KEY (brand_key)
        REFERENCES dim_brand(brand_key)

);