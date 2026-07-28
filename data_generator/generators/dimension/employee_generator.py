import random

import pandas as pd
from faker import Faker

from data_generator.constants.dimension_constants.customer import GENDERS
from data_generator.constants.dimension_constants.employee import (
    EMPLOYEE_POSITIONS,
    SALARY_RANGE,
)
from data_generator.utils.file_utils import (
    get_dimension_file,
    get_output_file,
)
from data_generator.utils.id_utils import generate_code

fake = Faker("id_ID")


def generate_employee():

    store_df = pd.read_csv(
        get_dimension_file("dim_store.csv")
    )

    employees = []

    employee_id = 1

    for _, store in store_df.iterrows():

        store_key = store["store_key"]

        for position, total in EMPLOYEE_POSITIONS.items():

            for _ in range(total):

                salary = random.randint(
                    SALARY_RANGE[position][0],
                    SALARY_RANGE[position][1]
                )

                employees.append({

                    "employee_key": employee_id,

                    "employee_code": generate_code(
                        "EMP",
                        employee_id
                    ),

                    "employee_name": fake.name(),

                    "gender": random.choice(
                        GENDERS
                    ),

                    "position": position,

                    "salary": salary,

                    "hire_date": fake.date_between(
                        start_date="-8y",
                        end_date="-30d"
                    ),

                    "email": fake.email(),

                    "phone": fake.phone_number(),

                    "store_key": store_key,

                    "is_active": random.choices(
                        [True, False],
                        weights=[97, 3]
                    )[0]

                })

                employee_id += 1

    return pd.DataFrame(employees)


def validate_employee(df):

    if df.empty:
        raise ValueError("Employee dataset is empty.")

    if df["employee_code"].duplicated().any():
        raise ValueError("Duplicate employee_code detected.")

    if df["employee_key"].duplicated().any():
        raise ValueError("Duplicate employee_key detected.")

    print("Validation passed.")


def main():

    df = generate_employee()

    validate_employee(df)

    output_file = get_output_file(
        "dim_employee.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print("=" * 60)
    print("Employee Generator")
    print("=" * 60)
    print(df.head())
    print()
    print(f"Total Employee : {len(df)}")
    print(f"Output         : {output_file}")


if __name__ == "__main__":
    main()