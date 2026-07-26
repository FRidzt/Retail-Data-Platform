import pandas as pd

from data_generator.constants.product import BRANDS
from data_generator.utils.file_utils import (
    get_dimension_file,
    get_output_file
)
from data_generator.utils.id_utils import generate_code


def generate_brand():

    category_df = pd.read_csv(
        get_dimension_file("dim_category.csv")
    )

    brands = []

    brand_key = 1

    for _, category in category_df.iterrows():

        category_name = category["category_name"]
        category_key = category["category_key"]

        if category_name not in BRANDS:
            continue

        for brand in BRANDS[category_name]:

            brands.append({

                "brand_key": brand_key,

                "brand_code": generate_code(
                    "BRD",
                    brand_key
                ),

                "brand_name": brand,

                "category_key": category_key,

                "category_name": category_name

            })

            brand_key += 1

    return pd.DataFrame(brands)


def validate_brand(df):

    if df.empty:
        raise ValueError("Brand dataset kosong.")

    if df["brand_key"].duplicated().any():
        raise ValueError("Duplicate brand_key.")

    if df["brand_code"].duplicated().any():
        raise ValueError("Duplicate brand_code.")

    print("Validation passed.")


def main():

    df = generate_brand()

    validate_brand(df)

    output = get_output_file(
        "dim_brand.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print("=" * 60)
    print("Brand Generator")
    print("=" * 60)
    print(df.head())
    print()
    print(f"Total Brand : {len(df)}")
    print(f"Output      : {output}")


if __name__ == "__main__":
    main()