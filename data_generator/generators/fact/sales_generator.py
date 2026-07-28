import random
import pandas as pd

from datetime import datetime

from data_generator.constants.fact_constants.sales import (
    get_sales_status,
    get_sales_quantity,
    get_discount,
    generate_invoice_number
)

from data_generator.utils.file_utils import (
    get_dimension_file,
    get_fact_file
)

from data_generator.utils.id_utils import (
    generate_code
)


# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset():

    customer_df = pd.read_csv(
        get_dimension_file("dim_customer.csv")
    )

    employee_df = pd.read_csv(
        get_dimension_file("dim_employee.csv")
    )

    store_df = pd.read_csv(
        get_dimension_file("dim_store.csv")
    )

    payment_df = pd.read_csv(
        get_dimension_file("dim_payment.csv")
    )

    promotion_df = pd.read_csv(
        get_dimension_file("dim_promotion.csv")
    )

    product_df = pd.read_csv(
        get_dimension_file("dim_product.csv")
    )

    category_df = pd.read_csv(
        get_dimension_file("dim_category.csv")
    )

    date_df = pd.read_csv(
        get_dimension_file("dim_date.csv")
    )

    stock_df = pd.read_csv(
        get_fact_file("fact_stock.csv")
    )

    return (
        customer_df,
        employee_df,
        store_df,
        payment_df,
        promotion_df,
        product_df,
        category_df,
        date_df,
        stock_df
    )


# ==========================================================
# Random Active Customer
# ==========================================================

def get_customer(customer_df):

    customer_df = customer_df[
        customer_df["is_active"] == True
    ]

    return customer_df.sample(1).iloc[0]


# ==========================================================
# Random Store
# ==========================================================

def get_store(store_df):

    store_df = store_df[
        store_df["is_active"] == True
    ]

    return store_df.sample(1).iloc[0]


# ==========================================================
# Employee Based on Store
# ==========================================================

def get_employee(
    employee_df,
    store_key
):

    employee = employee_df[

        (employee_df["store_key"] == store_key)

        &

        (employee_df["is_active"] == True)

    ]

    if len(employee) == 0:
        return None

    return employee.sample(1).iloc[0]


# ==========================================================
# Payment
# ==========================================================

def get_payment(payment_df):

    payment_df = payment_df[
        payment_df["is_active"] == True
    ]

    return payment_df.sample(1).iloc[0]


# ==========================================================
# Promotion
# ==========================================================

def get_promotion(
    promotion_df,
    sales_date
):

    promotion_df = promotion_df.copy()

    promotion_df["start_date"] = pd.to_datetime(
        promotion_df["start_date"]
    )

    promotion_df["end_date"] = pd.to_datetime(
        promotion_df["end_date"]
    )

    active = promotion_df[

        (promotion_df["is_active"] == True)

        &

        (promotion_df["start_date"] <= sales_date)

        &

        (promotion_df["end_date"] >= sales_date)

    ]

    if len(active) == 0:

        return None

    return active.sample(1).iloc[0]


# ==========================================================
# Random Sales Date
# ==========================================================

def get_sales_date(date_df):

    working_day = date_df[

        date_df["full_date"]
        <= datetime.today().strftime("%Y-%m-%d")

    ]

    row = working_day.sample(1).iloc[0]

    return row


# ==========================================================
# Available Stock
# ==========================================================

def get_stock(stock_df):

    available = stock_df[

        stock_df["available_stock"] > 0

    ]

    if len(available) == 0:

        return None

    return available.sample(1).iloc[0]


# ==========================================================
# Product
# ==========================================================

def get_product(
    product_df,
    product_key
):

    return product_df[

        product_df["product_key"] == product_key

    ].iloc[0]


# ==========================================================
# Category
# ==========================================================

def get_category(
    category_df,
    category_key
):

    return category_df[

        category_df["category_key"] == category_key

    ].iloc[0]

# ==========================================================
# Generate Sales
# ==========================================================

def generate_sales(
    total_sales=50000
):

    (
        customer_df,
        employee_df,
        store_df,
        payment_df,
        promotion_df,
        product_df,
        category_df,
        date_df,
        stock_df

    ) = load_dataset()

    sales_rows = []

    sales_key = 1

    for _ in range(total_sales):

        # ==========================================
        # Sales Date
        # ==========================================

        sales_date = get_sales_date(
            date_df
        )

        sales_datetime = pd.to_datetime(
            sales_date["full_date"]
        )

        # ==========================================
        # Stock
        # ==========================================

        stock = get_stock(
            stock_df
        )

        if stock is None:
            break

        product = get_product(

            product_df,

            stock["product_key"]

        )

        category = get_category(

            category_df,

            product["category_key"]

        )

        # ==========================================
        # Store
        # ==========================================

        store = store_df[
            store_df["store_key"]
            ==
            stock["store_key"]
        ].iloc[0]

        # ==========================================
        # Employee
        # ==========================================

        employee = get_employee(

            employee_df,

            store["store_key"]

        )

        if employee is None:
            continue

        # ==========================================
        # Customer
        # ==========================================

        customer = get_customer(
            customer_df
        )

        # ==========================================
        # Payment
        # ==========================================

        payment = get_payment(
            payment_df
        )

        # ==========================================
        # Promotion
        # ==========================================

        promotion = get_promotion(

            promotion_df,

            sales_datetime

        )

        # ==========================================
        # Quantity
        # ==========================================

        quantity = get_sales_quantity(

            category["category_name"]

        )

        quantity = min(

            quantity,

            int(
                stock["available_stock"]
            )

        )

        if quantity <= 0:
            continue

        # ==========================================
        # Price
        # ==========================================

        unit_price = int(
            product["selling_price"]
        )

        cost_price = int(
            product["cost_price"]
        )

        tax_percent = int(
            product["tax_percent"]
        )

        gross_amount = (

            quantity

            *

            unit_price

        )

        # ==========================================
        # Discount
        # ==========================================

        if promotion is not None and random.random() < 0.35:

            promotion_key = int(

                promotion["promotion_key"]

            )

            discount_percent = int(

                promotion["discount_percent"]

            )

        else:

            promotion_key = None

            discount_percent = get_discount()

        discount_amount = int(

            gross_amount

            *

            discount_percent

            /100

        )

        if promotion is not None:

            discount_amount = min(

                discount_amount,

                int(
                    promotion["maximum_discount"]
                )

            )

        taxable_amount = (

            gross_amount

            -

            discount_amount

        )

        tax_amount = int(

            taxable_amount

            *

            tax_percent

            / 100

        )

        net_sales = (

            taxable_amount

            +

            tax_amount

        )

        cogs = (

            quantity

            *

            cost_price

        )

        gross_profit = (

            taxable_amount

            -

            cogs

        )

        sales_status = get_sales_status()

        invoice_number = generate_invoice_number(

            sales_datetime,

            sales_key

        )

        # ==========================================
        # Save Transaction
        # ==========================================

        sales_rows.append({

            "sales_key":
                sales_key,

            "sales_code":
                generate_code(
                    "SAL",
                    sales_key
                ),

            "sales_date_key":
                sales_date["date_key"],

            "customer_key":
                customer["customer_key"],

            "employee_key":
                employee["employee_key"],

            "store_key":
                store["store_key"],

            "payment_key":
                payment["payment_key"],

            "promotion_key":
                promotion_key,

            "product_key":
                product["product_key"],

            "stock_key":
                stock["stock_key"],

            "quantity":
                quantity,

            "unit_price":
                unit_price,

            "gross_amount":
                gross_amount,

            "discount_percent":
                discount_percent,

            "discount_amount":
                discount_amount,

            "tax_percent":
                tax_percent,

            "tax_amount":
                tax_amount,

            "net_sales":
                net_sales,

            "cost_price":
                cost_price,

            "cogs":
                cogs,

            "gross_profit":
                gross_profit,

            "sales_status":
                sales_status,

            "invoice_number":
                invoice_number

        })

        # ==========================================
        # Update Available Stock (Memory Only)
        # ==========================================

        stock_df.loc[

            stock_df["stock_key"]

            ==

            stock["stock_key"],

            "available_stock"

        ] -= quantity

        sales_key += 1

    # ==========================================
    # Return DataFrame
    # ==========================================

    return pd.DataFrame(
        sales_rows
    )

# ==========================================================
# Validation
# ==========================================================

def validate_sales(df):

    if df.empty:
        raise ValueError(
            "Sales dataset kosong."
        )

    if df["sales_key"].duplicated().any():
        raise ValueError(
            "Duplicate sales_key."
        )

    if df["sales_code"].duplicated().any():
        raise ValueError(
            "Duplicate sales_code."
        )

    if df["invoice_number"].duplicated().any():
        raise ValueError(
            "Duplicate invoice_number."
        )

    if (df["quantity"] <= 0).any():
        raise ValueError(
            "Quantity harus lebih dari 0."
        )

    if (df["unit_price"] <= 0).any():
        raise ValueError(
            "Unit price tidak valid."
        )

    if (df["net_sales"] < 0).any():
        raise ValueError(
            "Net sales tidak boleh negatif."
        )

    print("Validation passed.")


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("Sales Generator")
    print("=" * 60)

    df = generate_sales(
        total_sales=50000
    )

    validate_sales(df)

    output = get_fact_file(
        "fact_sales.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print()
    print(df.head())
    print()

    print("=" * 60)

    print(
        f"Total Sales       : {len(df):,}"
    )

    print(
        f"Revenue           : {df['net_sales'].sum():,}"
    )

    print(
        f"Gross Profit      : {df['gross_profit'].sum():,}"
    )

    print(
        f"Average Revenue   : {df['net_sales'].mean():,.2f}"
    )

    print(
        f"Output            : {output}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()