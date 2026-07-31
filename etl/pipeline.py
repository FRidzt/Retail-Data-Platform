from etl.bronze.load_dimension import load_all_dimensions
from etl.bronze.load_fact import load_all_facts


def main():

    print("=" * 70)
    print("Retail Data Warehouse ETL")
    print("=" * 70)

    load_all_dimensions()

    load_all_facts()

    print("\nETL Finished Successfully")


if __name__ == "__main__":
    main()