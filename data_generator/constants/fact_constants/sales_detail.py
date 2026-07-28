import random

# ==========================================================
# Item per Invoice Distribution
# ==========================================================

ITEM_PER_INVOICE = {
    1: 25,
    2: 30,
    3: 20,
    4: 12,
    5: 8,
    6: 3,
    7: 1,
    8: 1
}


def get_item_count():

    return random.choices(

        list(ITEM_PER_INVOICE.keys()),

        weights=list(ITEM_PER_INVOICE.values()),

        k=1

    )[0]


# ==========================================================
# Quantity per Category
# ==========================================================

SALES_QTY = {

    "Electronics": (1, 2),

    "Computer": (1, 1),

    "Smartphone": (1, 2),

    "Home Appliances": (1, 2),

    "Furniture": (1, 1),

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

    "Stationery": (2, 15),

    "Automotive": (1, 3),

    "Pet Supplies": (1, 5),

    "Baby Products": (1, 5),

    "Gaming": (1, 2),

    "Music": (1, 2),

    "Accessories": (1, 8),

    "Office": (1, 5),

    "Toys": (1, 5)

}


def get_sales_quantity(category):

    minimum, maximum = SALES_QTY.get(

        category,

        (1, 3)

    )

    return random.randint(

        minimum,

        maximum

    )


# ==========================================================
# Random Discount (Without Promotion)
# ==========================================================

DISCOUNT_WEIGHT = {

    0: 80,

    5: 15,

    10: 4,

    15: 1

}


def get_discount_percent():

    return random.choices(

        list(DISCOUNT_WEIGHT.keys()),

        weights=list(DISCOUNT_WEIGHT.values()),

        k=1

    )[0]


# ==========================================================
# Promotion Discount
# ==========================================================

def calculate_discount(

    gross_amount,

    promotion

):

    if promotion is None:

        discount_percent = get_discount_percent()

        discount_amount = int(

            gross_amount

            * discount_percent

            / 100

        )

        return (

            discount_percent,

            discount_amount

        )

    minimum_purchase = int(

        promotion["minimum_purchase"]

    )

    if gross_amount < minimum_purchase:

        return (

            0,

            0

        )

    discount_percent = int(

        promotion["discount_percent"]

    )

    maximum_discount = int(

        promotion["maximum_discount"]

    )

    discount_amount = int(

        gross_amount

        * discount_percent

        / 100

    )

    discount_amount = min(

        discount_amount,

        maximum_discount

    )

    return (

        discount_percent,

        discount_amount

    )


# ==========================================================
# Tax
# ==========================================================

def calculate_tax(

    taxable_amount,

    tax_percent

):

    if tax_percent <= 0:

        return 0

    return int(

        taxable_amount

        * tax_percent

        / 100

    )


# ==========================================================
# Net Sales
# ==========================================================

def calculate_net_sales(

    gross_amount,

    discount_amount,

    tax_amount

):

    return (

        gross_amount

        - discount_amount

        + tax_amount

    )


# ==========================================================
# COGS
# ==========================================================

def calculate_cogs(

    quantity,

    cost_price

):

    return quantity * cost_price


# ==========================================================
# Gross Profit
# ==========================================================

def calculate_gross_profit(

    net_sales,

    cogs

):

    return net_sales - cogs


# ==========================================================
# Validate Stock
# ==========================================================

def validate_quantity(

    requested_qty,

    available_stock

):

    return min(

        requested_qty,

        available_stock

    )