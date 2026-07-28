import random

# ==========================================================
# Sales Status
# ==========================================================

SALES_STATUS = [
    "Completed",
    "Pending",
    "Cancelled"
]

SALES_STATUS_WEIGHT = [
    95,
    4,
    1
]

# ==========================================================
# Quantity per Category
# ==========================================================

SALES_QTY = {

    "Electronics": (1, 3),

    "Computer": (1, 2),

    "Smartphone": (1, 3),

    "Home Appliances": (1, 2),

    "Furniture": (1, 2),

    "Kitchen": (1, 5),

    "Food": (1, 10),

    "Beverage": (1, 12),

    "Health": (1, 5),

    "Beauty": (1, 5),

    "Fashion Men": (1, 4),

    "Fashion Women": (1, 4),

    "Fashion Kids": (1, 4),

    "Sports": (1, 3),

    "Outdoor": (1, 3),

    "Books": (1, 5),

    "Stationery": (1, 10),

    "Automotive": (1, 3),

    "Pet Supplies": (1, 5),

    "Baby Products": (1, 5),

    "Gaming": (1, 2),

    "Music": (1, 2),

    "Accessories": (1, 8),

    "Office": (1, 5),

    "Toys": (1, 5)

}

# ==========================================================
# Discount
# ==========================================================

SALES_DISCOUNT_RANGE = (
    0,
    20
)

# ==========================================================
# Invoice
# ==========================================================

def generate_invoice_number(
    sales_date,
    index
):

    return (
        f"INV-"
        f"{sales_date.strftime('%Y%m')}-"
        f"{index:06d}"
    )

# ==========================================================
# Sales Status
# ==========================================================

def get_sales_status():

    return random.choices(

        SALES_STATUS,

        weights=SALES_STATUS_WEIGHT,

        k=1

    )[0]

# ==========================================================
# Quantity
# ==========================================================

def get_sales_quantity(category):

    minimum, maximum = SALES_QTY[category]

    return random.randint(
        minimum,
        maximum
    )

# ==========================================================
# Discount
# ==========================================================

def get_discount():

    return random.choices(

        population=[
            0,
            5,
            10,
            15,
            20
        ],

        weights=[
            45,
            30,
            15,
            7,
            3
        ],

        k=1

    )[0]