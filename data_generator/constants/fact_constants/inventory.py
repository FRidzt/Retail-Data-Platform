import random
from datetime import timedelta


WAREHOUSE_ZONE = [
    "A",
    "B",
    "C",
    "D",
    "E"
]


def generate_batch_number(index):

    return f"BAT{index:08d}"


def generate_location():

    zone = random.choice(WAREHOUSE_ZONE)

    rack = random.randint(1, 20)

    shelf = random.randint(1, 6)

    return f"{zone}-{rack:02}-{shelf:02}"


def inspect_delivery(order_qty):
    """
    Simulasi proses QC barang yang datang dari supplier.

    Return:
    received_qty,
    accepted_qty,
    damaged_qty,
    inventory_status
    """

    probability = random.random()

    # ==============================
    # 94% barang diterima sempurna
    # ==============================
    if probability < 0.94:

        received_qty = order_qty

        accepted_qty = order_qty

        damaged_qty = 0

        status = "Received"

    # ==============================
    # 5% sebagian rusak
    # ==============================
    elif probability < 0.99:

        received_qty = order_qty

        damaged_qty = random.randint(
            1,
            max(1, int(order_qty * 0.10))
        )

        accepted_qty = (
            received_qty
            - damaged_qty
        )

        status = "Partial"

    # ==============================
    # 1% ditolak seluruhnya
    # ==============================
    else:

        received_qty = order_qty

        accepted_qty = 0

        damaged_qty = order_qty

        status = "Rejected"

    return (
        received_qty,
        accepted_qty,
        damaged_qty,
        status
    )


def generate_expiry_date(received_date, category):

    expiry_category = {

        "Food": 365,

        "Beverage": 365,

        "Health": 730,

        "Beauty": 730,

        "Pet Supplies": 540,

        "Baby Products": 540

    }

    if category not in expiry_category:
        return None

    return (
        received_date
        + timedelta(
            days=expiry_category[category]
        )
    ).date()