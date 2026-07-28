import random
import pandas as pd

from datetime import datetime

from data_generator.constants.fact_constants.sales import (
    get_sales_status,
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

    date_df = pd.read_csv(
        get_dimension_file("dim_date.csv")
    )

    return (
        customer_df,
        employee_df,
        store_df,
        payment_df,
        promotion_df,
        date_df
    )


# ==========================================================
# Customer
# ==========================================================

def get_customer(customer_df):

    active = customer_df[
        customer_df["is_active"] == True
    ]

    return active.sample(1).iloc[0]


# ==========================================================
# Store
# ==========================================================

def get_store(store_df):

    active = store_df[
        store_df["is_active"] == True
    ]

    return active.sample(1).iloc[0]


# ==========================================================
# Employee
# ==========================================================

def get_employee(employee_df, store_key):

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

    active = payment_df[
        payment_df["is_active"] == True
    ]

    return active.sample(1).iloc[0]


# ==========================================================
# Promotion
# ==========================================================

def get_promotion(promotion_df, sales_date):

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

    # hanya 30% transaksi menggunakan promo
    if len(active) == 0 or random.random() > 0.30:
        return None

    return active.sample(1).iloc[0]


# ==========================================================
# Sales Date
# ==========================================================

def get_sales_date(date_df):

    available = date_df[
        date_df["full_date"]
        <=
        datetime.today().strftime("%Y-%m-%d")
    ]

    return available.sample(1).iloc[0]


# ==========================================================
# Generate Sales Header
# ==========================================================

def generate_sales_header(total_sales=30000):

    (
        customer_df,
        employee_df,
        store_df,
        payment_df,
        promotion_df,
        date_df
    ) = load_dataset()

    rows = []

    sales_key = 1

    for _ in range(total_sales):

        sales_date = get_sales_date(
            date_df
        )

        sales_datetime = pd.to_datetime(
            sales_date["full_date"]
        )

        store = get_store(
            store_df
        )

        employee = get_employee(
            employee_df,
            store["store_key"]
        )

        if employee is None:
            continue

        customer = get_customer(
            customer_df
        )

        payment = get_payment(
            payment_df
        )

        promotion = get_promotion(
            promotion_df,
            sales_datetime
        )

        promotion_key = (
            int(promotion["promotion_key"])
            if promotion is not None
            else None
        )

        rows.append({

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

            "sales_status":
                get_sales_status(),

            "invoice_number":
                generate_invoice_number(
                    sales_datetime,
                    sales_key
                )

        })

        sales_key += 1

    return pd.DataFrame(rows)


# ==========================================================
# Validation
# ==========================================================

def validate_sales_header(df):

    if df.empty:
        raise ValueError(
            "Sales header dataset kosong."
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

    print("Validation passed.")


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("Sales Header Generator")
    print("=" * 60)

    df = generate_sales_header(30000)

    validate_sales_header(df)

    output = get_fact_file(
        "fact_sales_header.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print(df.head())
    print()

    print(
        f"Total Invoice : {len(df):,}"
    )

    print(
        f"Output        : {output}"
    )


if __name__ == "__main__":
    main()