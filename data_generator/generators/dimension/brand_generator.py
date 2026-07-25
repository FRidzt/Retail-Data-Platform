import pandas as pd

from data_generator.constants.product import (
    BRANDS,
    PRODUCT_CATEGORIES
)
from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code


def generate_brand():

    rows = []

    brand_key = 1

    for category_key, category_name in enumerate(PRODUCT_CATEGORIES, start=1):

        for brand in BRANDS.get(category_name, []):

            rows.append({

                "brand_key": brand_key,

                "brand_code": generate_code("BRD", brand_key),

                "brand_name": brand,

                "category_key": category_key,

                "category_name": category_name,

                "is_active": True

            })

            brand_key += 1

    return pd.DataFrame(rows)


def main():

    df = generate_brand()

    output = get_output_file("dim_brand.csv")

    df.to_csv(output, index=False)

    print(df.head(20))

    print(f"\nTotal Brand : {len(df)}")

    print(f"Saved : {output}")


if __name__ == "__main__":
    main()