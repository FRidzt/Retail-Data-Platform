from loaders.fact_loader import FactLoader


FACT_TABLES = [

    "fact_purchase",

    "fact_inventory",

    "fact_stock",

    "fact_sales_header",

    "fact_sales_detail",

    "fact_return",

    "fact_inventory_movement"

]


def load_all_facts():

    loader = FactLoader()

    print("=" * 60)
    print("Loading Fact Tables")
    print("=" * 60)

    for table in FACT_TABLES:

        loader.load_table(table)

    loader.close()

    print("\n✓ All Fact Loaded")