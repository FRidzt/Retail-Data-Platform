import pandas as pd

from data_generator.constants.payment import PAYMENT_METHODS
from data_generator.utils.file_utils import get_output_file
from data_generator.utils.id_utils import generate_code


def generate_payment():

    payments = []

    payment_key = 1

    for method, providers in PAYMENT_METHODS.items():

        for provider in providers:

            payments.append({

                "payment_key": payment_key,

                "payment_code": generate_code(
                    "PAY",
                    payment_key
                ),

                "payment_method": method,

                "provider": provider,

                "is_active": True

            })

            payment_key += 1

    return pd.DataFrame(payments)


def validate_payment(df):

    if df.empty:
        raise ValueError("Payment dataset kosong.")

    if df["payment_code"].duplicated().any():
        raise ValueError("Duplicate payment_code.")

    print("Validation passed.")


def main():

    df = generate_payment()

    validate_payment(df)

    output = get_output_file(
        "dim_payment.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print("=" * 60)
    print("Payment Generator")
    print("=" * 60)
    print(df.head())
    print()
    print(f"Total Payment : {len(df)}")
    print(f"Output : {output}")


if __name__ == "__main__":
    main()
    