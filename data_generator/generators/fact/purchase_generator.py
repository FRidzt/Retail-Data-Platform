import random

import pandas as pd

from data_generator.constants.fact_constants.purchase import (
    PURCHASE_PAYMENT_METHOD,
    get_cost_multiplier,
    get_discount,
    get_purchase_status,
    get_quantity,
    generate_supplier_invoice,
    generate_delivery_date
)

from data_generator.utils.file_utils import (
    get_dimension_file,
    get_fact_file
)

from data_generator.utils.id_utils import generate_code


def generate_purchase(total_purchase=30000):

    supplier_df = pd.read_csv(
        get_dimension_file("dim_supplier.csv")
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

    product_df = pd.read_csv(
        get_dimension_file("dim_product.csv")
    )

    category_df = pd.read_csv(
        get_dimension_file("dim_category.csv")
    )

    date_df = pd.read_csv(
        get_dimension_file("dim_date.csv")
    )


    purchases = []

    for i in range(1, total_purchase + 1):

        supplier = supplier_df.sample(1).iloc[0]

        employee = employee_df.sample(1).iloc[0]

        store = store_df.sample(1).iloc[0]

        payment = payment_df.sample(1).iloc[0]

        product = product_df.sample(1).iloc[0]

        date = date_df.sample(1).iloc[0]

        category_key = product["category_key"]

        category = category_df[
            category_df["category_key"] == category_key
        ].iloc[0]

        category_name = category["category_name"]

        qty = get_quantity(category_name)

        multiplier = get_cost_multiplier()

        unit_cost = int(
            product["cost_price"] * multiplier
        )

        subtotal = qty * unit_cost

        discount_percent = get_discount()

        discount_amount = int(
            subtotal * discount_percent / 100
        )

        tax_percent = product["tax_percent"]

        tax_amount = int(
            (subtotal - discount_amount)
            * tax_percent
            / 100
        )

        total_amount = (
            subtotal
            - discount_amount
            + tax_amount
        )

        date = date_df.sample(1).iloc[0]

        purchase_date = pd.to_datetime(
            date["full_date"]
        )
        
        delivery_date = generate_delivery_date(
           purchase_date
        )

        purchases.append({

            "purchase_key": i,

            "purchase_code": generate_code(
                "PUR",
                i
            ),

            "purchase_date_key":
                date["date_key"],

            "supplier_key":
                supplier["supplier_key"],

            "employee_key":
                employee["employee_key"],

            "store_key":
                store["store_key"],

            "payment_key":
                payment["payment_key"],

            "product_key":
                product["product_key"],

            "quantity":
                qty,

            "unit_cost":
                unit_cost,

            "subtotal":
                subtotal,

            "discount_percent":
                discount_percent,

            "discount_amount":
                discount_amount,

            "tax_percent":
                tax_percent,

            "tax_amount":
                tax_amount,

            "total_amount":
                total_amount,

            "purchase_status":
                get_purchase_status(),
            
            "supplier_invoice_no":
                generate_supplier_invoice(
                    i,
                    purchase_date),
            
            "expected_delivery_date":
            delivery_date.date(),

        })

    return pd.DataFrame(purchases)


def validate_purchase(df):

    if df.empty:
        raise ValueError(
            "Purchase dataset kosong."
        )

    if df["purchase_key"].duplicated().any():
        raise ValueError(
            "Duplicate purchase_key."
        )

    if df["purchase_code"].duplicated().any():
        raise ValueError(
            "Duplicate purchase_code."
        )

    print("Validation passed.")


def main():

    print("=" * 60)
    print("Purchase Generator")
    print("=" * 60)

    df = generate_purchase(30000)

    validate_purchase(df)

    output = get_fact_file(
        "fact_purchase.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print(df.head())

    print()

    print(f"Total Purchase : {len(df)}")
    print(f"Output         : {output}")


if __name__ == "__main__":
    main()