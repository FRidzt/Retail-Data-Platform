-- ==========================================================
-- Retail Data Warehouse
-- Create Indexes
-- ==========================================================

SET search_path TO bronze;

-- ==========================================================
-- Dimension Tables
-- ==========================================================

CREATE INDEX idx_brand_category
ON dim_brand(category_key);

CREATE INDEX idx_product_category
ON dim_product(category_key);

CREATE INDEX idx_product_brand
ON dim_product(brand_key);

CREATE INDEX idx_employee_store
ON dim_employee(store_key);

-- ==========================================================
-- Fact Purchase
-- ==========================================================

CREATE INDEX idx_purchase_date
ON fact_purchase(purchase_date_key);

CREATE INDEX idx_purchase_supplier
ON fact_purchase(supplier_key);

CREATE INDEX idx_purchase_employee
ON fact_purchase(employee_key);

CREATE INDEX idx_purchase_store
ON fact_purchase(store_key);

CREATE INDEX idx_purchase_payment
ON fact_purchase(payment_key);

CREATE INDEX idx_purchase_product
ON fact_purchase(product_key);

-- ==========================================================
-- Fact Inventory
-- ==========================================================

CREATE INDEX idx_inventory_purchase
ON fact_inventory(purchase_key);

CREATE INDEX idx_inventory_date
ON fact_inventory(inventory_date_key);

CREATE INDEX idx_inventory_product
ON fact_inventory(product_key);

CREATE INDEX idx_inventory_store
ON fact_inventory(store_key);

-- ==========================================================
-- Fact Stock
-- ==========================================================

CREATE INDEX idx_stock_product
ON fact_stock(product_key);

CREATE INDEX idx_stock_store
ON fact_stock(store_key);

CREATE INDEX idx_stock_date
ON fact_stock(stock_date_key);

-- ==========================================================
-- Fact Sales Header
-- ==========================================================

CREATE INDEX idx_sales_date
ON fact_sales_header(sales_date_key);

CREATE INDEX idx_sales_customer
ON fact_sales_header(customer_key);

CREATE INDEX idx_sales_employee
ON fact_sales_header(employee_key);

CREATE INDEX idx_sales_store
ON fact_sales_header(store_key);

CREATE INDEX idx_sales_payment
ON fact_sales_header(payment_key);

CREATE INDEX idx_sales_promotion
ON fact_sales_header(promotion_key);

-- ==========================================================
-- Fact Sales Detail
-- ==========================================================

CREATE INDEX idx_sales_detail_sales
ON fact_sales_detail(sales_key);

CREATE INDEX idx_sales_detail_product
ON fact_sales_detail(product_key);

CREATE INDEX idx_sales_detail_stock
ON fact_sales_detail(stock_key);

-- ==========================================================
-- Fact Return
-- ==========================================================

CREATE INDEX idx_return_sales
ON fact_return(sales_key);

CREATE INDEX idx_return_sales_detail
ON fact_return(sales_detail_key);

CREATE INDEX idx_return_product
ON fact_return(product_key);

CREATE INDEX idx_return_stock
ON fact_return(stock_key);

CREATE INDEX idx_return_date
ON fact_return(return_date_key);