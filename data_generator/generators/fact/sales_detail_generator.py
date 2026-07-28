import pandas as pd

from datetime import datetime

from data_generator.constants.fact_constants.sales_detail import (

    get_item_count,
    get_sales_quantity,
    validate_quantity,
    calculate_discount,
    calculate_tax,
    calculate_net_sales,
    calculate_cogs,
    calculate_gross_profit

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

    sales_header_df = pd.read_csv(
        get_fact_file(
            "fact_sales.csv"
        )
    )

    stock_df = pd.read_csv(
        get_fact_file(
            "fact_stock.csv"
        )
    )

    product_df = pd.read_csv(
        get_dimension_file(
            "dim_product.csv"
        )
    )

    category_df = pd.read_csv(
        get_dimension_file(
            "dim_category.csv"
        )
    )

    promotion_df = pd.read_csv(
        get_dimension_file(
            "dim_promotion.csv"
        )
    )

    return (

        sales_header_df,
        stock_df,
        product_df,
        category_df,
        promotion_df

    )


# ==========================================================
# Get Product
# ==========================================================

def get_product(

    product_df,
    product_key

):

    return product_df[

        product_df["product_key"]

        ==

        product_key

    ].iloc[0]


# ==========================================================
# Get Category
# ==========================================================

def get_category(

    category_df,
    category_key

):

    return category_df[

        category_df["category_key"]

        ==

        category_key

    ].iloc[0]


# ==========================================================
# Get Promotion
# ==========================================================

def get_promotion(

    promotion_df,
    promotion_key

):

    if pd.isna(
        promotion_key
    ):

        return None

    promotion = promotion_df[

        promotion_df["promotion_key"]

        ==

        int(promotion_key)

    ]

    if promotion.empty:

        return None

    return promotion.iloc[0]


# ==========================================================
# Get Available Stock
# ==========================================================

def get_store_stock(

    stock_df,
    store_key

):

    stock = stock_df[

        (stock_df["store_key"] == store_key)

        &

        (stock_df["available_stock"] > 0)

    ]

    if stock.empty:

        return None

    return stock


# ==========================================================
# Reduce Stock
# ==========================================================

def reduce_stock(

    stock_df,
    stock_key,
    quantity

):

    stock_df.loc[

        stock_df["stock_key"]

        ==

        stock_key,

        "available_stock"

    ] -= quantity


# ==========================================================
# Invoice Item Count
# ==========================================================

def get_invoice_item_count():

    return get_item_count()

# ==========================================================
# Build Sales Detail Row
# ==========================================================

def build_sales_detail(

    sales_row,
    stock_df,
    product_df,
    category_df,
    promotion_df

):

    stock_list = get_store_stock(

        stock_df,

        sales_row["store_key"]

    )

    if stock_list is None:

        return []

    detail_rows = []

    item_count = get_invoice_item_count()

    used_product = set()

    line_number = 1

    for _ in range(item_count):

        available = stock_list[

            ~stock_list["product_key"].isin(
                used_product
            )

        ]

        if available.empty:

            break

        stock = available.sample(1).iloc[0]

        product = get_product(

            product_df,

            stock["product_key"]

        )

        category = get_category(

            category_df,

            product["category_key"]

        )

        promotion = get_promotion(

            promotion_df,

            sales_row["promotion_key"]

        )

        quantity = get_sales_quantity(

            category["category_name"]

        )

        quantity = validate_quantity(

            quantity,

            int(
                stock["available_stock"]
            )

        )

        if quantity <= 0:

            continue

        used_product.add(

            stock["product_key"]

        )

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

        discount_percent, discount_amount = calculate_discount(

            gross_amount,

            promotion

        )

        taxable_amount = (

            gross_amount

            -

            discount_amount

        )

        tax_amount = calculate_tax(

            taxable_amount,

            tax_percent

        )

        net_sales = calculate_net_sales(

            gross_amount,

            discount_amount,

            tax_amount

        )

        cogs = calculate_cogs(

            quantity,

            cost_price

        )

        gross_profit = calculate_gross_profit(

            net_sales,

            cogs

        )

        detail_rows.append({

            "sales_detail_key": None,

            "sales_detail_code": None,

            "sales_key":
                sales_row["sales_key"],

            "line_number":
                line_number,

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
                gross_profit

        })

        reduce_stock(

            stock_df,

            stock["stock_key"],

            quantity

        )

        line_number += 1

    return detail_rows

# ==========================================================
# Generate Sales Detail
# ==========================================================

def generate_sales_detail():

    (

        sales_header_df,
        stock_df,
        product_df,
        category_df,
        promotion_df

    ) = load_dataset()

    detail_rows = []

    sales_detail_key = 1

    sales_header_df = sales_header_df.sort_values(

        "sales_key"

    )

    for _, sales in sales_header_df.iterrows():

        # ==========================================
        # Skip Cancelled Transaction
        # ==========================================

        if sales["sales_status"] == "Cancelled":

            continue

        # ==========================================
        # Generate Detail Items
        # ==========================================

        rows = build_sales_detail(

            sales,

            stock_df,

            product_df,

            category_df,

            promotion_df

        )

        if len(rows) == 0:

            continue

        # ==========================================
        # Assign Running Key & Code
        # ==========================================

        for row in rows:

            row["sales_detail_key"] = sales_detail_key

            row["sales_detail_code"] = generate_code(

                "SDT",

                sales_detail_key

            )

            detail_rows.append(

                row

            )

            sales_detail_key += 1

    # ==========================================
    # Convert DataFrame
    # ==========================================

    detail_df = pd.DataFrame(

        detail_rows

    )

    # ==========================================
    # Column Order
    # ==========================================

    detail_df = detail_df[[

        "sales_detail_key",

        "sales_detail_code",

        "sales_key",

        "line_number",

        "product_key",

        "stock_key",

        "quantity",

        "unit_price",

        "gross_amount",

        "discount_percent",

        "discount_amount",

        "tax_percent",

        "tax_amount",

        "net_sales",

        "cost_price",

        "cogs",

        "gross_profit"

    ]]

    return detail_df

# ==========================================================
# Validation
# ==========================================================

def validate_sales_detail(df):

    if df.empty:

        raise ValueError(

            "Sales Detail dataset kosong."

        )

    if df["sales_detail_key"].duplicated().any():

        raise ValueError(

            "Duplicate sales_detail_key."

        )

    if df["sales_detail_code"].duplicated().any():

        raise ValueError(

            "Duplicate sales_detail_code."

        )

    if (df["quantity"] <= 0).any():

        raise ValueError(

            "Quantity harus lebih besar dari 0."

        )

    if (df["unit_price"] <= 0).any():

        raise ValueError(

            "Unit price tidak valid."

        )

    if (df["gross_amount"] <= 0).any():

        raise ValueError(

            "Gross amount tidak valid."

        )

    if (df["discount_amount"] < 0).any():

        raise ValueError(

            "Discount amount tidak valid."

        )

    if (df["tax_amount"] < 0).any():

        raise ValueError(

            "Tax amount tidak valid."

        )

    if (df["net_sales"] < 0).any():

        raise ValueError(

            "Net sales tidak valid."

        )

    if (df["cogs"] < 0).any():

        raise ValueError(

            "COGS tidak valid."

        )

    print(

        "Validation passed."

    )


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)

    print("Sales Detail Generator")

    print("=" * 60)

    df = generate_sales_detail()

    validate_sales_detail(

        df

    )

    output = get_fact_file(

        "fact_sales_detail.csv"

    )

    df.to_csv(

        output,

        index=False

    )

    print()

    print(

        df.head()

    )

    print()

    print("=" * 60)

    print(

        f"Total Detail Rows : {len(df):,}"

    )

    print(

        f"Total Revenue     : {df['net_sales'].sum():,}"

    )

    print(

        f"Total COGS        : {df['cogs'].sum():,}"

    )

    print(

        f"Total GrossProfit : {df['gross_profit'].sum():,}"

    )

    print(

        f"Average Qty       : {df['quantity'].mean():.2f}"

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