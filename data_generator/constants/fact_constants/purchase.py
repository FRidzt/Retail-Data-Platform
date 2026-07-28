import random

# ======================================================
# Purchase Status
# ======================================================

PURCHASE_STATUS = [
    "Completed",
    "Pending",
    "Cancelled"
]

PURCHASE_STATUS_WEIGHT = [
    90,
    8,
    2
]

# ======================================================
# Purchase Quantity per Category
# ======================================================

PURCHASE_QTY = {

    "Electronics": (5, 30),
    "Computer": (3, 20),
    "Smartphone": (10, 80),
    "Home Appliances": (5, 40),
    "Furniture": (2, 20),

    "Kitchen": (20, 150),
    "Food": (100, 500),
    "Beverage": (100, 600),

    "Health": (50, 300),
    "Beauty": (50, 250),

    "Fashion Men": (20, 200),
    "Fashion Women": (20, 200),
    "Fashion Kids": (20, 150),

    "Sports": (15, 120),
    "Outdoor": (10, 80),

    "Books": (20, 150),
    "Stationery": (50, 300),

    "Automotive": (10, 100),
    "Pet Supplies": (20, 200),
    "Baby Products": (20, 150),

    "Gaming": (5, 40),
    "Music": (5, 30),

    "Accessories": (50, 500),
    "Office": (30, 300),
    "Toys": (20, 200)

}

# ======================================================
# Purchase Discount
# ======================================================

PURCHASE_DISCOUNT_RANGE = (0, 15)

# ======================================================
# Supplier Cost Variation
# ======================================================

PURCHASE_COST_VARIATION = (
    0.97,
    1.03
)

# ======================================================
# Payment Method
# ======================================================

PURCHASE_PAYMENT_METHOD = [
    "Cash",
    "Bank Transfer",
    "Credit"
]

# ======================================================
# Helper Functions
# ======================================================

def get_purchase_status():

    return random.choices(
        PURCHASE_STATUS,
        weights=PURCHASE_STATUS_WEIGHT,
        k=1
    )[0]


def get_discount():

    return random.randint(
        PURCHASE_DISCOUNT_RANGE[0],
        PURCHASE_DISCOUNT_RANGE[1]
    )


def get_quantity(category):

    minimum, maximum = PURCHASE_QTY[category]

    return random.randint(
        minimum,
        maximum
    )


def get_cost_multiplier():

    return round(
        random.uniform(
            PURCHASE_COST_VARIATION[0],
            PURCHASE_COST_VARIATION[1]
        ),
        2
    )


from datetime import datetime, timedelta


def generate_supplier_invoice(index, purchase_date):

    return (
        f"INV-SUP-"
        f"{purchase_date.strftime('%Y%m')}"
        f"-{index:06d}"
    )


def generate_delivery_date(purchase_date):

    return purchase_date + timedelta(
        days=random.randint(2, 14)
    )