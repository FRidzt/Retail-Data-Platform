import pandas as pd

from data_generator.constants.fact_constants.inventory import (
    generate_batch_number,
    generate_location,
    generate_expiry_date,
    inspect_delivery
)

from data_generator.utils.file_utils import (
    get_dimension_file,
    get_fact_file
)

from data_generator.utils.id_utils import generate_code


def generate_inventory():

    purchase_df = pd.read_csv(
        get_fact_file("fact_purchase.csv")
    )

    product_df = pd.read_csv(
        get_dimension_file("dim_product.csv")
    )

    category_df = pd.read_csv(
        get_dimension_file("dim_category.csv")
    )

    completed_purchase = purchase_df[
        purchase_df["purchase_status"] == "Completed"
    ]

    inventories = []

    inventory_key = 1

    for _, purchase in completed_purchase.iterrows():

        product = product_df[
            product_df["product_key"]
            == purchase["product_key"]
        ].iloc[0]

        category = category_df[
            category_df["category_key"]
            == product["category_key"]
        ].iloc[0]

        category_name = category["category_name"]

        received_date = pd.to_datetime(
            purchase["expected_delivery_date"]
        )

        # ============================
        # Quantity
        # ============================

        (
            received_qty,
            accepted_qty,
            damaged_qty,
            inventory_status
        ) = inspect_delivery(
            purchase["quantity"]
        )

        # ============================
        # Expiry
        # ============================

        expiry_date = generate_expiry_date(
            received_date,
            category_name
        )

        inventories.append({

            "inventory_key":
                inventory_key,

            "inventory_code":
                generate_code(
                    "INV",
                    inventory_key
                ),

            "purchase_key":
                purchase["purchase_key"],

            "inventory_date_key":
                int(
                    received_date.strftime("%Y%m%d")
                ),

            "product_key":
                purchase["product_key"],

            "store_key":
                purchase["store_key"],

            "received_quantity":
                received_qty,

            "accepted_quantity":
                accepted_qty,

            "damaged_quantity":
                damaged_qty,

            "inventory_status":
                inventory_status,

            "batch_number":
                generate_batch_number(
                    inventory_key
                ),

            "warehouse_location":
                generate_location(),

            "expiry_date":
                expiry_date

        })

        inventory_key += 1

    return pd.DataFrame(inventories)


def validate_inventory(df):

    if df.empty:
        raise ValueError(
            "Inventory dataset kosong."
        )

    if df["inventory_key"].duplicated().any():
        raise ValueError(
            "Duplicate inventory_key."
        )

    if df["inventory_code"].duplicated().any():
        raise ValueError(
            "Duplicate inventory_code."
        )

    print("Validation passed.")


def main():

    print("=" * 60)
    print("Inventory Generator")
    print("=" * 60)

    df = generate_inventory()

    validate_inventory(df)

    output = get_fact_file(
        "fact_inventory.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print(df.head())

    print()

    print(f"Total Inventory : {len(df)}")
    print(f"Output          : {output}")


if __name__ == "__main__":
    main()