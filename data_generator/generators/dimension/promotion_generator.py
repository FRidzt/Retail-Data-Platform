import random

import pandas as pd
from faker import Faker

from data_generator.constants.promotion import (
    PROMOTION_NAMES,
    PROMOTION_TYPES
)

from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code

fake = Faker("id_ID")


def generate_promotion(total_promotion=50):

    promotions = []

    for i in range(1, total_promotion + 1):

        start = fake.date_between(
            start_date="-2y",
            end_date="today"
        )

        end = fake.date_between(
            start_date=start,
            end_date="+30d"
        )

        discount = random.choice(
            [5, 10, 15, 20, 25, 30, 40, 50]
        )

        minimum = random.choice(
            [
                0,
                50000,
                100000,
                200000,
                300000,
                500000
            ]
        )

        promotions.append({

            "promotion_key": i,

            "promotion_code": generate_code(
                "PRO",
                i
            ),

            "promotion_name":
                f"{random.choice(PROMOTION_NAMES)} {i}",

            "promotion_type":
                random.choice(PROMOTION_TYPES),

            "discount_percent":
                discount,

            "minimum_purchase":
                minimum,

            "maximum_discount":
                random.choice(
                    [
                        10000,
                        25000,
                        50000,
                        75000,
                        100000,
                        150000
                    ]
                ),

            "start_date":
                start,

            "end_date":
                end,

            "is_active":
                random.choice(
                    [
                        True,
                        True,
                        True,
                        False
                    ]
                )

        })

    return pd.DataFrame(promotions)


def validate_promotion(df):

    if df.empty:
        raise ValueError("Promotion dataset kosong.")

    if df["promotion_code"].duplicated().any():
        raise ValueError("Duplicate promotion_code.")

    print("Validation passed.")


def main():

    df = generate_promotion()

    validate_promotion(df)

    output = get_output_file(
        "dim_promotion.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print("=" * 60)

    print("Promotion Generator")

    print("=" * 60)

    print(df.head())

    print()

    print(f"Total Promotion : {len(df)}")

    print(f"Output : {output}")


if __name__ == "__main__":
    main()