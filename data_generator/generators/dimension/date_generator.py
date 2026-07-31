from datetime import datetime

import pandas as pd

from data_generator.utils.file_utils import get_output_file


def generate_date_dimension(
    start_date="2020-01-01",
    end_date="2030-12-31"
):

    dates = pd.date_range(start_date, end_date)

    rows = []

    for date in dates:

        rows.append({

            "date_key":
                int(date.strftime("%Y%m%d")),

            "full_date":
                date.date(),

            "day":
                date.day,

            "day_name":
                date.strftime("%A"),

            "day_of_week":
                date.dayofweek + 1,

            "week_of_year":
                date.isocalendar().week,

            "month":
                date.month,

            "month_name":
                date.strftime("%B"),

            "quarter":
                f"Q{date.quarter}",

            "semester":
                1 if date.month <= 6 else 2,

            "year":
                date.year,

            "is_weekend":
                date.dayofweek >= 5,

            "is_holiday":
                False,

            "holiday_name":
                None

        })

    return pd.DataFrame(rows)


def validate_date(df):

    if df.empty:
        raise ValueError("Date dataset kosong.")

    if df["date_key"].duplicated().any():
        raise ValueError("Duplicate date_key")

    print("Validation passed.")


def main():

    df = generate_date_dimension()

    validate_date(df)

    output = get_output_file(
        "dim_date.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print("=" * 60)

    print("Date Generator")

    print("=" * 60)

    print(df.head())

    print()

    print(f"Total Date : {len(df)}")

    print(f"Output : {output}")


if __name__ == "__main__":
    main()