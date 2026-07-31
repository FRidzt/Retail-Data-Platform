import random

import pandas as pd

from datetime import datetime

from data_generator.constants.fact_constants.return_data import (

    get_return_reason,
    get_return_status,
    get_refund_method,
    get_return_quantity,
    calculate_refund_amount

)

from data_generator.utils.file_utils import (

    get_fact_file,
    get_dimension_file

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
            "fact_sales_header.csv"
        )
    )

    sales_detail_df = pd.read_csv(
        get_fact_file(
            "fact_sales_detail.csv"
        )
    )

    stock_df = pd.read_csv(
        get_fact_file(
            "fact_stock.csv"
        )
    )

    date_df = pd.read_csv(
    get_dimension_file(
        "dim_date.csv"
    )
)

    return (

        sales_header_df,

        sales_detail_df,

        stock_df,

        date_df

    )


# ==========================================================
# Completed Sales Only
# ==========================================================

def get_completed_sales(

    sales_df

):

    return sales_df[

        sales_df["sales_status"]

        ==

        "Completed"

    ]


# ==========================================================
# Eligible Return Detail
# ==========================================================

def get_sales_detail(

    sales_detail_df,

    sales_key

):

    return sales_detail_df[

        sales_detail_df["sales_key"]

        ==

        sales_key

    ]


# ==========================================================
# Random Return Date
# ==========================================================

def generate_return_date(

    sales_date

):

    sales_date = pd.to_datetime(

        str(sales_date)

    )

    return sales_date + pd.Timedelta(

        days=random.randint(1, 30)

    )


# ==========================================================
# Return Code
# ==========================================================

def generate_return_code(

    return_key

):

    return generate_code(

        "RET",

        return_key

    )


# ==========================================================
# Determine Returned Transactions
# ==========================================================

def sample_return_sales(

    sales_df,

    return_ratio=0.03

):

    completed = get_completed_sales(

        sales_df

    )

    total = max(

        1,

        int(

            len(completed)

            *

            return_ratio

        )

    )

    return completed.sample(

        n=total,

        random_state=42

    )

# ==========================================================
# Build Return Item
# ==========================================================

def build_return_item(

    detail,

    return_key,

    return_date_key

):

    quantity = int(

        detail["quantity"]

    )

    unit_price = int(

        detail["unit_price"]

    )

    cost_price = int(

        detail["cost_price"]

    )

    tax_percent = int(

        detail["tax_percent"]

    )

    return_qty = get_return_quantity(

        quantity

    )

    if return_qty <= 0:

        return None

    reason = get_return_reason()

    status = get_return_status()

    refund_method = get_refund_method()

    gross_return = (

        return_qty

        *

        unit_price

    )

    discount_ratio = 0

    if detail["gross_amount"] > 0:

        discount_ratio = (

            detail["discount_amount"]

            /

            detail["gross_amount"]

        )

    discount_amount = int(

        gross_return

        *

        discount_ratio

    )

    taxable_amount = (

        gross_return

        -

        discount_amount

    )

    tax_amount = int(

        taxable_amount

        *

        tax_percent

        / 100

    )

    refund_amount = calculate_refund_amount(

        taxable_amount,

        tax_amount

    )

    return {

        "return_key":

            return_key,

        "return_code":

            generate_return_code(

                return_key

            ),

        "sales_key":

            detail["sales_key"],

        "sales_detail_key":

            detail["sales_detail_key"],

        "product_key":

            detail["product_key"],

        "stock_key":

            detail["stock_key"],

        "return_date_key":

            return_date_key,

        "return_quantity":

            return_qty,

        "unit_price":

            unit_price,

        "gross_return":

            gross_return,

        "discount_amount":

            discount_amount,

        "tax_amount":

            tax_amount,

        "refund_amount":

            refund_amount,

        "cost_price":

            cost_price,

        "return_reason":

            reason,

        "refund_method":

            refund_method,

        "return_status":

            status

    }


# ==========================================================
# Build One Invoice Returns
# ==========================================================

def build_invoice_returns(

    details,

    return_key,

    return_date_key

):

    rows = []

    for _, detail in details.iterrows():

        if random.random() > 0.35:

            continue

        row = build_return_item(

            detail,

            return_key,

            return_date_key

        )

        if row is not None:

            rows.append(

                row

            )

            return_key += 1

    return (

        rows,

        return_key

    )

# ==========================================================
# Generate Return
# ==========================================================

def generate_return(

    return_ratio=0.03

):

    (

        sales_header_df,

        sales_detail_df,

        stock_df,
        
        date_df

    ) = load_dataset()

    return_rows = []

    return_key = 1

    selected_sales = sample_return_sales(

        sales_header_df,

        return_ratio

    )

    for _, sale in selected_sales.iterrows():

        sales_key = int(

            sale["sales_key"]

        )

        details = get_sales_detail(

            sales_detail_df,

            sales_key

        )

        if details.empty:

            continue

        # ==========================================
        # Return Date
        # ==========================================

        return_date = generate_return_date(

            sale["sales_date_key"]

        )

        return_date_key = int(

            return_date.strftime("%Y%m%d")

        )

        # ==========================================
        # Build Return Rows
        # ==========================================

        rows, return_key = build_invoice_returns(

            details,

            return_key,

            return_date_key

        )

        # ==========================================
        # Update Stock & Save Completed Return
        # ==========================================

        for row in rows:

            if row["return_status"] == "Completed":

                stock_key = int(

                    row["stock_key"]

                )

                qty = int(

                    row["return_quantity"]

                )

                stock_df.loc[

                    stock_df["stock_key"] == stock_key,

                    "available_stock"

                ] += qty

            return_rows.append(row)

    return (

        pd.DataFrame(return_rows),

        stock_df

    )

# ==========================================================
# Validation
# ==========================================================

def validate_return(df):

    if df.empty:

        raise ValueError(
            "Return dataset kosong."
        )

    if df["return_key"].duplicated().any():

        raise ValueError(
            "Duplicate return_key."
        )

    if df["return_code"].duplicated().any():

        raise ValueError(
            "Duplicate return_code."
        )

    if (df["return_quantity"] <= 0).any():

        raise ValueError(
            "Return quantity harus lebih dari 0."
        )

    if (df["refund_amount"] < 0).any():

        raise ValueError(
            "Refund amount tidak boleh negatif."
        )

    print("Validation passed.")


# ==========================================================
# Save Dataset
# ==========================================================

def save_dataset(

    return_df,

    stock_df

):

    return_output = get_fact_file(

        "fact_return.csv"

    )

    stock_output = get_fact_file(

        "fact_stock.csv"

    )

    return_df.to_csv(

        return_output,

        index=False

    )

    stock_df.to_csv(

        stock_output,

        index=False

    )

    return (

        return_output,

        stock_output

    )


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("Return Generator")
    print("=" * 60)

    return_df, stock_df = generate_return(

        return_ratio=0.03

    )

    validate_return(

        return_df

    )

    return_output, stock_output = save_dataset(

        return_df,

        stock_df

    )

    print()

    print(return_df.head())

    print()

    print("=" * 60)

    print(

        f"Total Return           : {len(return_df):,}"

    )

    print(

        f"Total Refund Amount    : {return_df['refund_amount'].sum():,}"

    )

    print(

        f"Average Refund         : {return_df['refund_amount'].mean():,.2f}"

    )

    print()

    print(

        f"Return Output          : {return_output}"

    )

    print(

        f"Updated Stock Output   : {stock_output}"

    )

    print("=" * 60)


if __name__ == "__main__":
    main()