import random
from faker import Faker
import pandas as pd

from data_generator.config.constants import (
    CITIES,
    CUSTOMER_SEGMENTS,
    GENDERS,
    MEMBERSHIP_LEVELS,
)
from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code

fake = Faker("id_ID")


def generate_customer(total_customer=1000):
    customers = []

    for i in range(1, total_customer + 1):

        city, province = random.choice(CITIES)

        customer = {
            "customer_key": i,
            "customer_code": generate_code("CUS", i),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(GENDERS),
            "birth_date": fake.date_of_birth(
                minimum_age=18,
                maximum_age=65
            ),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "city": city,
            "province": province,
            "membership": random.choices(
                MEMBERSHIP_LEVELS,
                weights=[45, 30, 20, 5]
            )[0],
            "segment": random.choices(
                CUSTOMER_SEGMENTS,
                weights=[20, 40, 30, 10]
            )[0],
            "register_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            ),
            "is_active": random.choice([True, True, True, False])
        }

        customers.append(customer)

    return pd.DataFrame(customers)


def main():
    df = generate_customer(1000)

    output_file = get_output_file("dim_customer.csv")

    df.to_csv(output_file, index=False)

    print(df.head())
    print(f"\nDataset berhasil disimpan di:\n{output_file}")


if __name__ == "__main__":
    main()