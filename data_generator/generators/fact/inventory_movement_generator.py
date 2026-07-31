import pandas as pd

from data_generator.utils.file_utils import (

    get_fact_file

)

from data_generator.utils.id_utils import (

    generate_code

)


# ==========================================================
# Movement Type
# ==========================================================

MOVEMENT_TYPE = {

    "PURCHASE": "IN",

    "INVENTORY": "IN",

    "SALES": "OUT",

    "RETURN": "IN"

}


# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset():

    purchase_df = pd.read_csv(
        get_fact_file("fact_purchase.csv")
    )

    inventory_df = pd.read_csv(
        get_fact_file("fact_inventory.csv")
    )

    sales_df = pd.read_csv(
        get_fact_file("fact_sales_header.csv")
    )

    sales_detail_df = pd.read_csv(
        get_fact_file("fact_sales_detail.csv")
    )

    return_df = pd.read_csv(
        get_fact_file("fact_return.csv")
    )

    return (
        purchase_df,
        inventory_df,
        sales_df,
        sales_detail_df,
        return_df
    )


# ==========================================================
# Inventory Movement Record
# ==========================================================

def build_movement(

    movement_key,

    movement_date_key,

    product_key,

    store_key,

    stock_key,

    reference_type,

    reference_key,

    movement_type,

    quantity

):

    return {

        "movement_key":

            movement_key,

        "movement_code":

            generate_code(

                "MOV",

                movement_key

            ),

        "movement_date_key":

            movement_date_key,

        "product_key":

            product_key,

        "store_key":

            store_key,

        "stock_key":

            stock_key,

        "reference_type":

            reference_type,

        "reference_key":

            reference_key,

        "movement_type":

            movement_type,

        "quantity":

            quantity

    }


# ==========================================================
# Get Store from Purchase
# ==========================================================

def get_purchase_store(

    purchase_df,

    purchase_key

):

    row = purchase_df[

        purchase_df["purchase_key"]

        ==

        purchase_key

    ]

    if len(row) == 0:

        return None

    return int(

        row.iloc[0]["store_key"]

    )

# ==========================================================
# Purchase Movement
# ==========================================================

def generate_purchase_movements(

    purchase_df,

    movement_key

):

    rows = []

    for _, row in purchase_df.iterrows():

        rows.append(

            build_movement(

                movement_key=movement_key,

                movement_date_key=row["purchase_date_key"],

                product_key=row["product_key"],

                store_key=row["store_key"],

                stock_key=None,

                reference_type="PURCHASE",

                reference_key=row["purchase_key"],

                movement_type=MOVEMENT_TYPE["PURCHASE"],

                quantity=int(

                    row["quantity"]

                )

            )

        )

        movement_key += 1

    return rows, movement_key


# ==========================================================
# Inventory Movement
# ==========================================================

def generate_inventory_movements(

    purchase_df,
    inventory_df,
    movement_key

):

    rows = []

    inventory_df = inventory_df[

        inventory_df["inventory_status"]

        !=

        "Rejected"

    ]

    for _, row in inventory_df.iterrows():

        store_key = get_purchase_store(

            purchase_df,

            row["purchase_key"]

        )

        if store_key is None:

            continue

        rows.append(

            build_movement(

                movement_key=movement_key,

                movement_date_key=row["inventory_date_key"],

                product_key=row["product_key"],

                store_key=store_key,

                stock_key=None,

                reference_type="INVENTORY",

                reference_key=row["inventory_key"],

                movement_type=MOVEMENT_TYPE["INVENTORY"],

                quantity=int(

                    row["accepted_quantity"]

                )

            )

        )

        movement_key += 1

    return rows, movement_key


# ==========================================================
# Sales Movement
# ==========================================================


def generate_sales_movements(

    sales_df,

    sales_detail_df,

    movement_key

):

    rows = []

    for _, row in sales_detail_df.iterrows():

        sale = sales_df[

            sales_df["sales_key"]

            ==

            row["sales_key"]

        ].iloc[0]

        rows.append(

            build_movement(

                movement_key=movement_key,

                movement_date_key=sale["sales_date_key"],

                product_key=row["product_key"],

                store_key=sale["store_key"],

                stock_key=row["stock_key"],

                reference_type="SALES",

                reference_key=row["sales_detail_key"],

                movement_type=MOVEMENT_TYPE["SALES"],

                quantity=int(

                    row["quantity"]

                )

            )

        )

        movement_key += 1

    return rows, movement_key

# ==========================================================
# Return Movement
# ==========================================================

def generate_return_movements(

    return_df,

    sales_df,

    sales_detail_df,

    movement_key

):

    rows = []

    for _, row in return_df.iterrows():

        if row["return_status"] == "Rejected":

            continue

        sales_detail = sales_detail_df[
            sales_detail_df["sales_detail_key"] == row["sales_detail_key"]
            ].iloc[0]

        sales = sales_df[
            sales_df["sales_key"] == sales_detail["sales_key"]
            ].iloc[0]

        rows.append(

            build_movement(

                movement_key=movement_key,

                movement_date_key=row["return_date_key"],

                product_key=row["product_key"],

                store_key=sales["store_key"],

                stock_key=row["stock_key"],

                reference_type="RETURN",

                reference_key=row["return_key"],

                movement_type=MOVEMENT_TYPE["RETURN"],

                quantity=int(

                    row["return_quantity"]

                )

            )

        )

        movement_key += 1

    return rows, movement_key


# ==========================================================
# Generate Inventory Movement
# ==========================================================

def generate_inventory_movement():

    (
    
    purchase_df,

    inventory_df,

    sales_df,

    sales_detail_df,
    
    return_df

    ) = load_dataset()

    movement_key = 1

    movement_rows = []

    purchase_rows, movement_key = generate_purchase_movements(

    purchase_df,
    movement_key

    )

    movement_rows.extend(
        purchase_rows
    )

    inventory_rows, movement_key = generate_inventory_movements(

    purchase_df,
    inventory_df,
    movement_key

    )

    movement_rows.extend(

        inventory_rows

    )

    sales_rows, movement_key = generate_sales_movements(

        sales_df,

        sales_detail_df,

        movement_key

    )

    movement_rows.extend(

        sales_rows

    )

    return_rows, movement_key = generate_return_movements(

    return_df,

    sales_df,

    sales_detail_df,

    movement_key

)

    movement_rows.extend(

        return_rows

    )

    movement_df = pd.DataFrame(

        movement_rows

    )

    movement_df = movement_df.sort_values(
        [
            "movement_date_key",
            "movement_key"
        ]
    ).reset_index(drop=True)

    movement_df["movement_key"] = (
        movement_df.index + 1
    )

    movement_df["movement_code"] = (
        movement_df["movement_key"]
        .apply(lambda x: generate_code("MOV", x))
    )

    

    return movement_df

# ==========================================================
# Validation
# ==========================================================

def validate_inventory_movement(df):

    if df.empty:

        raise ValueError(

            "Inventory Movement dataset kosong."

        )

    if df["movement_key"].duplicated().any():

        raise ValueError(

            "Duplicate movement_key."

        )

    if df["movement_code"].duplicated().any():

        raise ValueError(

            "Duplicate movement_code."

        )

    if (df["quantity"] <= 0).any():

        raise ValueError(

            "Quantity harus lebih dari 0."

        )

    print(

        "Validation passed."

    )


# ==========================================================
# Summary
# ==========================================================

def print_summary(df):

    print()

    print("=" * 60)

    print("Inventory Movement Summary")

    print("=" * 60)

    print(

        f"Total Movement : {len(df):,}"

    )

    print()

    print(

        df["reference_type"]

        .value_counts()

    )

    print()

    print(

        df["movement_type"]

        .value_counts()

    )

    print()

    print(

        "Total IN :",

        df.loc[

            df["movement_type"] == "IN",

            "quantity"

        ].sum()

    )

    print(

        "Total OUT:",

        df.loc[

            df["movement_type"] == "OUT",

            "quantity"

        ].sum()

    )

    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)

    print(

        "Inventory Movement Generator"

    )

    print("=" * 60)

    df = generate_inventory_movement()

    validate_inventory_movement(df)

    output = get_fact_file(

        "fact_inventory_movement.csv"

    )

    df.to_csv(

        output,

        index=False

    )

    print()

    print(

        df.head(20)

    )

    print_summary(df)

    print()

    print(

        f"Output : {output}"

    )

    print("=" * 60)


if __name__ == "__main__":

    main()