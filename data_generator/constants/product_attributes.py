import random

# ==========================================================
# PRODUCT UNIT
# ==========================================================

PRODUCT_UNITS = [
    "pcs",
    "box",
    "pack",
    "bottle",
    "kg",
    "set"
]

CATEGORY_UNIT = {

    "Electronics": ["pcs"],

    "Computer": ["pcs"],

    "Smartphone": ["pcs"],

    "Home Appliances": ["pcs"],

    "Furniture": ["pcs"],

    "Kitchen": ["pcs", "set"],

    "Food": ["pcs", "pack", "box", "kg"],

    "Beverage": ["bottle", "box", "pack"],

    "Health": ["box", "bottle"],

    "Beauty": ["bottle", "pcs"],

    "Fashion Men": ["pcs"],

    "Fashion Women": ["pcs"],

    "Fashion Kids": ["pcs"],

    "Sports": ["pcs"],

    "Outdoor": ["pcs"],

    "Books": ["pcs"],

    "Stationery": ["pcs", "box"],

    "Automotive": ["pcs"],

    "Pet Supplies": ["pcs", "pack", "kg"],

    "Baby Products": ["pcs", "pack"],

    "Gaming": ["pcs"],

    "Music": ["pcs"],

    "Accessories": ["pcs"],

    "Office": ["pcs"],

    "Toys": ["pcs", "box"]

}

# ==========================================================
# COLOR
# ==========================================================

PRODUCT_COLORS = [
    "Black",
    "White",
    "Silver",
    "Gray",
    "Blue",
    "Red",
    "Green",
    "Pink",
    "Purple",
    "Gold"
]

COLOR_CATEGORY = [

    "Electronics",
    "Computer",
    "Smartphone",
    "Furniture",

    "Fashion Men",
    "Fashion Women",
    "Fashion Kids",

    "Sports",
    "Outdoor",

    "Gaming",
    "Accessories",

]

# ==========================================================
# SIZE
# ==========================================================

PRODUCT_SIZES = [
    "XS",
    "S",
    "M",
    "L",
    "XL",
    "XXL"
]

SIZE_CATEGORY = {

    "Fashion Men": PRODUCT_SIZES,

    "Fashion Women": PRODUCT_SIZES,

    "Fashion Kids": PRODUCT_SIZES,

    "Sports": PRODUCT_SIZES,

    "Furniture": [
        "Small",
        "Medium",
        "Large"
    ],

    "Outdoor": [
        "20L",
        "30L",
        "50L"
    ]

}

# ==========================================================
# STORAGE
# ==========================================================

STORAGE_OPTIONS = [
    "64GB",
    "128GB",
    "256GB",
    "512GB",
    "1TB"
]

STORAGE_CATEGORY = [

    "Computer",
    "Smartphone",
    "Gaming"

]

# ==========================================================
# WEIGHT (GRAM)
# ==========================================================

WEIGHT_RANGE = {

    "Electronics": (500, 5000),

    "Computer": (1000, 3500),

    "Smartphone": (150, 300),

    "Home Appliances": (2000, 15000),

    "Furniture": (5000, 60000),

    "Kitchen": (300, 5000),

    "Food": (100, 1000),

    "Beverage": (250, 2000),

    "Health": (50, 500),

    "Beauty": (50, 500),

    "Fashion Men": (100, 1000),

    "Fashion Women": (100, 800),

    "Fashion Kids": (50, 500),

    "Sports": (200, 3000),

    "Outdoor": (500, 6000),

    "Books": (150, 1500),

    "Stationery": (20, 300),

    "Automotive": (500, 8000),

    "Pet Supplies": (100, 5000),

    "Baby Products": (100, 3000),

    "Gaming": (200, 4000),

    "Music": (500, 15000),

    "Accessories": (50, 1000),

    "Office": (200, 4000),

    "Toys": (100, 5000)

}

# ==========================================================
# HELPER
# ==========================================================


def get_random_unit(category):

    return random.choice(CATEGORY_UNIT[category])

def get_random_color(category):

    if category not in COLOR_CATEGORY:
        return None

    return random.choice(PRODUCT_COLORS)


def get_random_size(category):

    if category not in SIZE_CATEGORY:
        return None

    return random.choice(
        SIZE_CATEGORY[category]
    )


def get_random_storage(category):

    if category not in STORAGE_CATEGORY:
        return None

    return random.choice(
        STORAGE_OPTIONS
    )


def get_weight(category):

    minimum, maximum = WEIGHT_RANGE.get(
        category,
        (100, 1000)
    )

    return random.randint(
        minimum,
        maximum
    )