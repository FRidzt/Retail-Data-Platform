import random

import pandas as pd

from data_generator.constants.product import (
    CATEGORY_MARGIN,
    CATEGORY_PRICE_RANGE,
    PRODUCT_STATUS_WEIGHT,
    PRODUCT_TAX,
    get_product_models
)

from data_generator.constants.product_attributes import (
    CATEGORY_UNIT,
    get_random_color,
    get_random_size,
    get_random_storage,
    get_random_unit,
    get_weight
)

from data_generator.utils.file_utils import (
    get_dimension_file,
    get_output_file
)

from data_generator.utils.id_utils import generate_code


def generate_product(total_product=1000):

    category_df = pd.read_csv(
        get_dimension_file("dim_category.csv")
    )

    brand_df = pd.read_csv(
        get_dimension_file("dim_brand.csv")
    )

    products = []

    for i in range(1, total_product + 1):

        # ==========================================
        # Category
        # ==========================================

        category = category_df.sample(1).iloc[0]

        category_key = category["category_key"]
        category_name = category["category_name"]

        # ==========================================
        # Brand
        # ==========================================

        brand_candidates = brand_df[
            brand_df["category_key"] == category_key
        ]

        brand = brand_candidates.sample(1).iloc[0]

        brand_key = brand["brand_key"]
        brand_name = brand["brand_name"]

        model = random.choice(
            get_product_models(brand_name)
            )

        # ==========================================
        # Product Name
        # ==========================================

        product_name = f"{brand_name} {model}"

        color = get_random_color(category_name)

        if color:
            product_name += f" {color}"

        size = get_random_size(category_name)

        storage = get_random_storage(category_name)

        if storage:
            product_name += f" {storage}"

        # ==========================================
        # Physical Attributes
        # ==========================================

        unit = get_random_unit(category_name)

        weight = get_weight(category_name)

        # ==========================================
        # Price
        # ==========================================

        min_price, max_price = CATEGORY_PRICE_RANGE[
            category_name
        ]

        selling_price = random.randint(
            min_price,
            max_price
        )

        margin_min, margin_max = CATEGORY_MARGIN[
            category_name
        ]

        margin = random.uniform(
            margin_min,
            margin_max
        )

        cost_price = int(
            selling_price / (1 + margin)
        )

        cost_price = round(cost_price, -2)
        selling_price = round(selling_price, -2)

        # ==========================================
        # Status
        # ==========================================

        is_active = random.choices(
            [True, False],
            weights=PRODUCT_STATUS_WEIGHT,
            k=1
        )[0]

        status = (
            "Active"
            if is_active
            else "Discontinued"
        )

        # ==========================================
        # Save Record
        # ==========================================

        products.append({

            "product_key": i,

            "product_code": generate_code(
                "PRD",
                i
            ),

            "product_name": product_name,

            "category_key": category_key,

            "brand_key": brand_key,

            "unit": unit,

            "color": color,

            "size": size,

            "storage": storage,

            "weight_gram": weight,

            "cost_price": cost_price,

            "selling_price": selling_price,

            "tax_percent": PRODUCT_TAX[
                category_name
            ],

            "status": status,

            "is_active": is_active

        })

    return pd.DataFrame(products)


def main():

    print("=" * 60)
    print("Product Generator")
    print("=" * 60)

    df = generate_product(1000)

    output = get_output_file(
        "dim_product.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print(df.head())

    print()

    print(f"Total Product : {len(df)}")

    print(f"Output        : {output}")


if __name__ == "__main__":
    main()