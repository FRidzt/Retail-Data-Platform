from loaders.dimension_loader import DimensionLoader


DIMENSION_TABLES = [

    "dim_date",

    "dim_category",

    "dim_brand",

    "dim_supplier",

    "dim_store",

    "dim_employee",

    "dim_payment",

    "dim_customer",

    "dim_promotion",

    "dim_product"

]


def load_all_dimensions():

    loader = DimensionLoader()

    print("=" * 60)
    print("Loading Dimension Tables")
    print("=" * 60)

    for table in DIMENSION_TABLES:

        loader.load_table(table)

    loader.close()

    print("\n✓ All Dimension Loaded")