import random

import pandas as pd
from faker import Faker

from data_generator.constants.dimension_constants.location import LOCATIONS
from data_generator.constants.dimension_constants.store import (
    STORE_PREFIX,
    STORE_TYPES,
    STORE_BRANCH
)

from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code

fake = Faker("id_ID")


def generate_store(total_store=25):

    stores = []

    for i in range(1, total_store + 1):

        city, province = random.choice(LOCATIONS)

        stores.append({

            "store_key": i,

            "store_code": generate_code("STR", i),

            "store_name": (
                f"{random.choice(STORE_PREFIX)} "
                f"{city} "
                f"{random.choice(STORE_BRANCH)}"),

            "store_type": random.choice(STORE_TYPES),

            "city": city,

            "province": province,

            "address": fake.address().replace("\n", ", "),

            "phone": fake.phone_number(),

            "opening_date": fake.date_between(
                start_date="-10y",
                end_date="-6m"
            ),

            "manager_name": fake.name(),

            "is_active": random.choices(
                [True, False],
                weights=[95, 5]
            )[0]

        })

    return pd.DataFrame(stores)

def validate_store(df):

    if df.empty:
        raise ValueError("Store dataset kosong")

    if df["store_code"].duplicated().any():
        raise ValueError("Duplicate store_code")

    if df["store_name"].duplicated().any():
        print("Warning : duplicate store_name")

def main():

    df = generate_store(25)

    validate_store(df)

    output = get_output_file("dim_store.csv")

    df.to_csv(output, index=False)

    print("=" * 60)
    print("Store Generator")
    print("=" * 60)
    print(df.head())
    print()
    print(f"Total Store : {len(df)}")
    print(f"Output      : {output}")


if __name__ == "__main__":
    main()