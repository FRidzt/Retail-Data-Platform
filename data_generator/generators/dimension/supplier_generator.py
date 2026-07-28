import random

import pandas as pd
from faker import Faker

from data_generator.constants.dimension_constants.location import LOCATIONS
from data_generator.constants.dimension_constants.supplier import (
    SUPPLIER_BUSINESS,
    SUPPLIER_COMPANY_PREFIX
)

from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code

fake = Faker("id_ID")


def generate_supplier(total_supplier=150):

    suppliers = []

    for i in range(1, total_supplier + 1):

        city, province = random.choice(LOCATIONS)

        company = (
            f"{random.choice(SUPPLIER_COMPANY_PREFIX)} "
            f"{fake.company()} "
            f"{random.choice(SUPPLIER_BUSINESS)}"
        )

        suppliers.append({

            "supplier_key": i,

            "supplier_code": generate_code("SUP", i),

            "supplier_name": company,

            "contact_person": fake.name(),

            "email": fake.company_email(),

            "phone": fake.phone_number(),

            "city": city,

            "province": province,

            "address": fake.address().replace("\n", ", "),

            "is_active": True

        })

    return pd.DataFrame(suppliers)

def main():
    df = generate_supplier(150)

    output_file = get_output_file("dim_supplier.csv")

    df.to_csv(output_file, index=False)

    print(df.head())
    print(f"\nDataset berhasil disimpan di:\n{output_file}")


if __name__ == "__main__":
    main()