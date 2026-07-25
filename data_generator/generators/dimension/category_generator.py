import pandas as pd

from data_generator.constants.product import PRODUCT_CATEGORIES
from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code


def generate_category():

    categories = []

    for i, category in enumerate(PRODUCT_CATEGORIES, start=1):

        categories.append({

            "category_key": i,

            "category_code": generate_code("CAT", i),

            "category_name": category,

            "is_active": True

        })

    return pd.DataFrame(categories)


def main():

    df = generate_category()

    output = get_output_file(
        "dim_category.csv"
    )

    df.to_csv(output, index=False)

    print(df)

    print(f"\nSaved : {output}")


if __name__ == "__main__":
    main()