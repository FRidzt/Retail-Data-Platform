import pandas as pd

from data_generator.constants.fact_constants.stock import (
    calculate_available_stock,
    get_reorder_point,
    get_reorder_quantity,
    get_stock_status,
    generate_last_stock_opname
)

from data_generator.utils.file_utils import (
    get_dimension_file,
    get_fact_file
)

from data_generator.utils.id_utils import (
    generate_code
)


def generate_stock():

    # ======================================================
    # Load Dataset
    # ======================================================

    inventory_df = pd.read_csv(
        get_fact_file("fact_inventory.csv")
    )

    product_df = pd.read_csv(
        get_dimension_file("dim_product.csv")
    )

    category_df = pd.read_csv(
        get_dimension_file("dim_category.csv")
    )

    # ======================================================
    # Hanya inventory yang berhasil diterima
    # ======================================================

    inventory_df = inventory_df[
        inventory_df["inventory_status"] != "Rejected"
    ]

    # ======================================================
    # Gabungkan stok per produk dan store
    # ======================================================

    grouped = (
        inventory_df
        .groupby(
            [
                "product_key",
                "store_key"
            ],
            as_index=False
        )
        .agg(
            {
                "accepted_quantity": "sum",
                "damaged_quantity": "sum",
                "inventory_date_key": "max"
            }
        )
    )

    stock_rows = []

    stock_key = 1

    # ======================================================
    # Generate Stock
    # ======================================================

    for _, row in grouped.iterrows():

        accepted_qty = int(
            row["accepted_quantity"]
        )

        damaged_qty = int(
            row["damaged_quantity"]
        )

        product = product_df[
            product_df["product_key"]
            == row["product_key"]
        ].iloc[0]

        category = category_df[
            category_df["category_key"]
            == product["category_key"]
        ].iloc[0]

        category_name = category["category_name"]

        total_stock = accepted_qty

        available_stock = calculate_available_stock(
            accepted_qty,
            damaged_qty
        )

        reorder_point = get_reorder_point(
            category_name
        )

        reorder_quantity = get_reorder_quantity(
            category_name
        )

        safety_stock = reorder_quantity

        stock_status = get_stock_status(
            available_stock,
            reorder_point,
            safety_stock
        )

        stock_rows.append({

            "stock_key":
                stock_key,

            "stock_code":
                generate_code(
                    "STK",
                    stock_key
                ),

            "product_key":
                row["product_key"],

            "store_key":
                row["store_key"],

            "stock_date_key":
                row["inventory_date_key"],

            "total_stock":
                total_stock,

            "available_stock":
                available_stock,

            "damaged_stock":
                damaged_qty,

            "reorder_point":
                reorder_point,

            "reorder_quantity":
                reorder_quantity,

            "stock_status":
                stock_status,

            "last_stock_opname":
                generate_last_stock_opname(
                    pd.to_datetime(
                        str(
                            row["inventory_date_key"]
                        )
                    )
                )

        })

        stock_key += 1

    return pd.DataFrame(
        stock_rows
    )


def validate_stock(df):

    if df.empty:
        raise ValueError(
            "Stock dataset kosong."
        )

    if df["stock_key"].duplicated().any():
        raise ValueError(
            "Duplicate stock_key."
        )

    if df["stock_code"].duplicated().any():
        raise ValueError(
            "Duplicate stock_code."
        )

    print("Validation passed.")


def main():

    print("=" * 60)
    print("Stock Generator")
    print("=" * 60)

    df = generate_stock()

    validate_stock(df)

    output = get_fact_file(
        "fact_stock.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print(df.head())

    print()

    print(f"Total Stock : {len(df)}")
    print(f"Output      : {output}")


if __name__ == "__main__":
    main()