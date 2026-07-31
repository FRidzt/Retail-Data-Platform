-- ==========================================================
-- Retail Data Warehouse
-- Create Fact Tables
-- ==========================================================

SET search_path TO bronze;

-- ==========================================================
-- Fact Purchase
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_purchase (

    purchase_key            INTEGER PRIMARY KEY,

    purchase_code           VARCHAR(20) UNIQUE,

    purchase_date_key       INTEGER NOT NULL,

    supplier_key            INTEGER NOT NULL,

    employee_key            INTEGER NOT NULL,

    store_key               INTEGER NOT NULL,

    payment_key             INTEGER NOT NULL,

    product_key             INTEGER NOT NULL,

    quantity                INTEGER NOT NULL,

    unit_cost               NUMERIC(18,2),

    subtotal                NUMERIC(18,2),

    discount_percent        NUMERIC(5,2),

    discount_amount         NUMERIC(18,2),

    tax_percent             NUMERIC(5,2),

    tax_amount              NUMERIC(18,2),

    total_amount            NUMERIC(18,2),

    purchase_status         VARCHAR(30),

    supplier_invoice_no     VARCHAR(100),

    expected_delivery_date  DATE,

    CONSTRAINT fk_purchase_date
        FOREIGN KEY (purchase_date_key)
        REFERENCES dim_date(date_key),

    CONSTRAINT fk_purchase_supplier
        FOREIGN KEY (supplier_key)
        REFERENCES dim_supplier(supplier_key),

    CONSTRAINT fk_purchase_employee
        FOREIGN KEY (employee_key)
        REFERENCES dim_employee(employee_key),

    CONSTRAINT fk_purchase_store
        FOREIGN KEY (store_key)
        REFERENCES dim_store(store_key),

    CONSTRAINT fk_purchase_payment
        FOREIGN KEY (payment_key)
        REFERENCES dim_payment(payment_key),

    CONSTRAINT fk_purchase_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key)

);

-- ==========================================================
-- Fact Inventory
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_inventory (

    inventory_key           INTEGER PRIMARY KEY,

    inventory_code          VARCHAR(20) UNIQUE,

    purchase_key            INTEGER NOT NULL,

    inventory_date_key      INTEGER NOT NULL,

    product_key             INTEGER NOT NULL,

    store_key               INTEGER NOT NULL,

    received_quantity       INTEGER,

    accepted_quantity       INTEGER,

    damaged_quantity        INTEGER,

    inventory_status        VARCHAR(30),

    batch_number            VARCHAR(50),

    warehouse_location      VARCHAR(50),

    expiry_date             DATE,

    CONSTRAINT fk_inventory_purchase
        FOREIGN KEY (purchase_key)
        REFERENCES fact_purchase(purchase_key),

    CONSTRAINT fk_inventory_date
        FOREIGN KEY (inventory_date_key)
        REFERENCES dim_date(date_key),

    CONSTRAINT fk_inventory_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_inventory_store
        FOREIGN KEY (store_key)
        REFERENCES dim_store(store_key)

);

-- ==========================================================
-- Fact Stock
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_stock (

    stock_key               INTEGER PRIMARY KEY,

    stock_code              VARCHAR(20) UNIQUE,

    product_key             INTEGER NOT NULL,

    store_key               INTEGER NOT NULL,

    stock_date_key          INTEGER NOT NULL,

    total_stock             INTEGER,

    available_stock         INTEGER,

    damaged_stock           INTEGER,

    reorder_point           INTEGER,

    reorder_quantity        INTEGER,

    stock_status            VARCHAR(30),

    last_stock_opname       DATE,

    CONSTRAINT fk_stock_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_stock_store
        FOREIGN KEY (store_key)
        REFERENCES dim_store(store_key),

    CONSTRAINT fk_stock_date
        FOREIGN KEY (stock_date_key)
        REFERENCES dim_date(date_key)

);

-- ==========================================================
-- Fact Sales Header
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_sales_header (

    sales_key               INTEGER PRIMARY KEY,

    sales_code              VARCHAR(20) UNIQUE,

    sales_date_key          INTEGER NOT NULL,

    customer_key            INTEGER,

    employee_key            INTEGER NOT NULL,

    store_key               INTEGER NOT NULL,

    payment_key             INTEGER NOT NULL,

    promotion_key           INTEGER,

    sales_status            VARCHAR(30),

    invoice_number          VARCHAR(50),

    CONSTRAINT fk_sales_date
        FOREIGN KEY (sales_date_key)
        REFERENCES dim_date(date_key),

    CONSTRAINT fk_sales_customer
        FOREIGN KEY (customer_key)
        REFERENCES dim_customer(customer_key),

    CONSTRAINT fk_sales_employee
        FOREIGN KEY (employee_key)
        REFERENCES dim_employee(employee_key),

    CONSTRAINT fk_sales_store
        FOREIGN KEY (store_key)
        REFERENCES dim_store(store_key),

    CONSTRAINT fk_sales_payment
        FOREIGN KEY (payment_key)
        REFERENCES dim_payment(payment_key),

    CONSTRAINT fk_sales_promotion
        FOREIGN KEY (promotion_key)
        REFERENCES dim_promotion(promotion_key)

);

-- ==========================================================
-- Fact Sales Detail
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_sales_detail (

    sales_detail_key        INTEGER PRIMARY KEY,

    sales_detail_code       VARCHAR(20) UNIQUE,

    sales_key               INTEGER NOT NULL,

    line_number             SMALLINT NOT NULL,

    product_key             INTEGER NOT NULL,

    stock_key               INTEGER NOT NULL,

    quantity                INTEGER NOT NULL,

    unit_price              NUMERIC(18,2),

    gross_amount            NUMERIC(18,2),

    discount_percent        NUMERIC(5,2),

    discount_amount         NUMERIC(18,2),

    tax_percent             NUMERIC(5,2),

    tax_amount              NUMERIC(18,2),

    net_sales               NUMERIC(18,2),

    cost_price              NUMERIC(18,2),

    cogs                    NUMERIC(18,2),

    gross_profit            NUMERIC(18,2),

    CONSTRAINT fk_sales_detail_header
        FOREIGN KEY (sales_key)
        REFERENCES fact_sales_header(sales_key),

    CONSTRAINT fk_sales_detail_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_sales_detail_stock
        FOREIGN KEY (stock_key)
        REFERENCES fact_stock(stock_key)

);

-- ==========================================================
-- Fact Return
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_return (

    return_key              INTEGER PRIMARY KEY,

    return_code             VARCHAR(20) UNIQUE,

    sales_key               INTEGER NOT NULL,

    sales_detail_key        INTEGER NOT NULL,

    product_key             INTEGER NOT NULL,

    stock_key               INTEGER NOT NULL,

    return_date_key         INTEGER NOT NULL,

    return_quantity         INTEGER NOT NULL,

    unit_price              NUMERIC(18,2),

    gross_return            NUMERIC(18,2),

    discount_amount         NUMERIC(18,2),

    tax_amount              NUMERIC(18,2),

    refund_amount           NUMERIC(18,2),

    cost_price              NUMERIC(18,2),

    return_reason           VARCHAR(100),

    refund_method           VARCHAR(50),

    return_status           VARCHAR(30),

    CONSTRAINT fk_return_sales
        FOREIGN KEY (sales_key)
        REFERENCES fact_sales_header(sales_key),

    CONSTRAINT fk_return_sales_detail
        FOREIGN KEY (sales_detail_key)
        REFERENCES fact_sales_detail(sales_detail_key),

    CONSTRAINT fk_return_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_return_stock
        FOREIGN KEY (stock_key)
        REFERENCES fact_stock(stock_key),

    CONSTRAINT fk_return_date
        FOREIGN KEY (return_date_key)
        REFERENCES dim_date(date_key)

);

-- ==========================================================
-- Fact Inventory Movement
-- ==========================================================

CREATE TABLE IF NOT EXISTS fact_inventory_movement (

    movement_key            INTEGER PRIMARY KEY,

    movement_code           VARCHAR(20) UNIQUE,

    movement_date_key       INTEGER NOT NULL,

    product_key             INTEGER NOT NULL,

    store_key               INTEGER NOT NULL,

    stock_key               INTEGER,

    reference_type          VARCHAR(30) NOT NULL,

    reference_key           INTEGER NOT NULL,

    movement_type           VARCHAR(20) NOT NULL,

    quantity                INTEGER NOT NULL,

    CONSTRAINT fk_movement_date
        FOREIGN KEY (movement_date_key)
        REFERENCES dim_date(date_key),

    CONSTRAINT fk_movement_product
        FOREIGN KEY (product_key)
        REFERENCES dim_product(product_key),

    CONSTRAINT fk_movement_store
        FOREIGN KEY (store_key)
        REFERENCES dim_store(store_key),

    CONSTRAINT fk_movement_stock
        FOREIGN KEY (stock_key)
        REFERENCES fact_stock(stock_key)

);