from datetime import timedelta
import random

# ==========================================================
# Reorder Point
# ==========================================================

REORDER_LEVEL = {

    "Electronics": 10,
    "Computer": 5,
    "Smartphone": 10,
    "Home Appliances": 8,
    "Furniture": 3,
    "Kitchen": 20,
    "Food": 100,
    "Beverage": 120,
    "Health": 40,
    "Beauty": 40,
    "Fashion Men": 30,
    "Fashion Women": 30,
    "Fashion Kids": 20,
    "Sports": 15,
    "Outdoor": 10,
    "Books": 20,
    "Stationery": 60,
    "Automotive": 10,
    "Pet Supplies": 20,
    "Baby Products": 20,
    "Gaming": 5,
    "Music": 5,
    "Accessories": 80,
    "Office": 40,
    "Toys": 20

}

# ==========================================================
# Safety Stock
# ==========================================================

SAFETY_STOCK = {

    "Electronics": 20,
    "Computer": 10,
    "Smartphone": 20,
    "Home Appliances": 15,
    "Furniture": 8,
    "Kitchen": 40,
    "Food": 200,
    "Beverage": 250,
    "Health": 80,
    "Beauty": 80,
    "Fashion Men": 50,
    "Fashion Women": 50,
    "Fashion Kids": 40,
    "Sports": 30,
    "Outdoor": 20,
    "Books": 40,
    "Stationery": 100,
    "Automotive": 20,
    "Pet Supplies": 40,
    "Baby Products": 40,
    "Gaming": 10,
    "Music": 10,
    "Accessories": 150,
    "Office": 80,
    "Toys": 40

}


# ==========================================================
# Available Stock
# ==========================================================

def calculate_available_stock(
    accepted_qty,
    damaged_qty
):

    sold = random.randint(
        0,
        max(
            accepted_qty - damaged_qty,
            0
        )
    )

    return (
        accepted_qty
        - damaged_qty
        - sold
    )


# ==========================================================
# Reorder Point
# ==========================================================

def get_reorder_point(category_name):

    return REORDER_LEVEL.get(
        category_name,
        20
    )


# ==========================================================
# Reorder Quantity
# ==========================================================

def get_reorder_quantity(category_name):

    return SAFETY_STOCK.get(
        category_name,
        50
    )


# ==========================================================
# Stock Status
# ==========================================================

def get_stock_status(
    available_stock,
    reorder_point,
    safety_stock
):

    if available_stock <= 0:
        return "Out of Stock"

    if available_stock <= reorder_point:
        return "Low Stock"

    if available_stock >= safety_stock * 2:
        return "Overstock"

    return "Normal"


# ==========================================================
# Last Stock Opname
# ==========================================================

def generate_last_stock_opname(
    inventory_date
):

    inventory_date = (
        inventory_date.to_pydatetime()
        if hasattr(
            inventory_date,
            "to_pydatetime"
        )
        else inventory_date
    )

    return (
        inventory_date
        + timedelta(
            days=random.randint(
                7,
                30
            )
        )
    ).date()