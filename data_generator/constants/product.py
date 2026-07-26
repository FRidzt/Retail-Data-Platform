import random

# ==========================================================
# CATEGORY
# ==========================================================

PRODUCT_CATEGORIES = [

    "Electronics",
    "Computer",
    "Smartphone",
    "Home Appliances",
    "Furniture",

    "Kitchen",
    "Food",
    "Beverage",
    "Health",
    "Beauty",

    "Fashion Men",
    "Fashion Women",
    "Fashion Kids",
    "Sports",
    "Outdoor",

    "Books",
    "Stationery",
    "Automotive",
    "Pet Supplies",
    "Baby Products",

    "Gaming",
    "Music",
    "Accessories",
    "Office",
    "Toys"
]

# ==========================================================
# BRAND
# ==========================================================

BRANDS = {

    "Electronics": [
        "Samsung",
        "LG",
        "Sony",
        "Panasonic",
        "Sharp"
    ],

    "Computer": [
        "Dell",
        "HP",
        "Lenovo",
        "ASUS",
        "Acer"
    ],

    "Smartphone": [
        "Apple",
        "Samsung",
        "Xiaomi",
        "OPPO",
        "vivo"
    ],

    "Home Appliances": [
        "Philips",
        "Electrolux",
        "Midea",
        "TCL"
    ],

    "Furniture": [
        "IKEA",
        "Informa",
        "Olympic"
    ],

    "Kitchen": [
        "Tupperware",
        "LocknLock",
        "Maspion"
    ],

    "Food": [
        "Indofood",
        "Mayora",
        "GarudaFood"
    ],

    "Beverage": [
        "Coca-Cola",
        "Pepsi",
        "Nestle"
    ],

    "Health": [
        "Blackmores",
        "Entrasol",
        "Kalbe"
    ],

    "Beauty": [
        "Wardah",
        "Make Over",
        "Emina",
        "L'Oreal"
    ],

    "Fashion Men": [
        "Nike",
        "Adidas",
        "Uniqlo"
    ],

    "Fashion Women": [
        "Zara",
        "H&M",
        "Uniqlo"
    ],

    "Fashion Kids": [
        "Carter's",
        "Mothercare"
    ],

    "Sports": [
        "Nike",
        "Adidas",
        "Puma"
    ],

    "Outdoor": [
        "Eiger",
        "Consina",
        "The North Face"
    ],

    "Books": [
        "Gramedia",
        "Erlangga"
    ],

    "Stationery": [
        "Faber Castell",
        "Joyko"
    ],

    "Automotive": [
        "Bosch",
        "Shell",
        "Castrol"
    ],

    "Pet Supplies": [
        "Whiskas",
        "Royal Canin"
    ],

    "Baby Products": [
        "Pampers",
        "MamyPoko",
        "Cussons Baby"
    ],

    "Gaming": [
        "Razer",
        "Logitech",
        "SteelSeries"
    ],

    "Music": [
        "Yamaha",
        "Roland",
        "Casio"
    ],

    "Accessories": [
        "Anker",
        "Baseus",
        "UGREEN"
    ],

    "Office": [
        "Bantex",
        "Deli"
    ],

    "Toys": [
        "LEGO",
        "Mattel",
        "Hasbro"
    ]
}

# ==========================================================
# PRODUCT MODEL
# ==========================================================

PRODUCT_MODELS = {

    "Samsung": [
        "Galaxy S25",
        "Galaxy S25+",
        "Galaxy S25 Ultra",
        "Galaxy A56",
        "Galaxy A36",
        "Galaxy Tab S10",
        "Galaxy Watch7"
    ],

    "LG": [
        "Smart TV 55",
        "UltraWide Monitor",
        "DualCool AC",
        "NeoChef Microwave"
    ],

    "Sony": [
        "PlayStation 5",
        "WH-1000XM5",
        "Bravia X90L",
        "Alpha A7 IV"
    ],

    "Panasonic": [
        "Rice Cooker SR",
        "Lumix G100",
        "Air Conditioner XPU"
    ],

    "Sharp": [
        "Aquos TV",
        "Plasmacluster AC",
        "Microwave R728"
    ],

    "Dell": [
        "Latitude 7450",
        "Inspiron 15",
        "XPS 13",
        "Alienware M18"
    ],

    "HP": [
        "EliteBook 840",
        "Victus 16",
        "Pavilion 15",
        "LaserJet Pro"
    ],

    "Lenovo": [
        "ThinkPad X1",
        "IdeaPad Slim 5",
        "Legion Pro 5",
        "Yoga 7"
    ],

    "ASUS": [
        "Zenbook 14",
        "ROG Strix G16",
        "Vivobook 15",
        "TUF A15"
    ],

    "Acer": [
        "Swift Go",
        "Aspire 5",
        "Predator Helios"
    ],

    "Apple": [
        "iPhone 16",
        "iPhone 16 Pro",
        "MacBook Air M4",
        "iPad Air",
        "AirPods Pro"
    ],

    "Xiaomi": [
        "Redmi Note 14",
        "Xiaomi 15",
        "Pad 7"
    ],

    "OPPO": [
        "Find X8",
        "Reno 13",
        "A5 Pro"
    ],

    "vivo": [
        "V50",
        "Y300",
        "X200"
    ],

    "Philips": [
        "Air Fryer XL",
        "Rice Cooker HD",
        "Blender HR"
    ],

    "Electrolux": [
        "Front Load Washer",
        "Vacuum Cleaner",
        "Refrigerator Ultimate"
    ],

    "Midea": [
        "Air Conditioner",
        "Microwave Oven",
        "Water Dispenser"
    ],

    "TCL": [
        "QLED TV",
        "Smart AC",
        "Washing Machine"
    ],

    "IKEA": [
        "MALM Bed",
        "LACK Table",
        "BILLY Bookcase"
    ],

    "Informa": [
        "Dining Chair",
        "Office Desk",
        "Wardrobe"
    ],

    "Olympic": [
        "Kitchen Cabinet",
        "Shoe Rack",
        "TV Cabinet"
    ],

    "Tupperware": [
        "Eco Bottle",
        "Lunch Box",
        "Storage Set"
    ],

    "LocknLock": [
        "Glass Container",
        "Water Bottle",
        "Food Keeper"
    ],

    "Maspion": [
        "Cooking Pot",
        "Frying Pan",
        "Pressure Cooker"
    ],

    "Indofood": [
        "Indomie Goreng",
        "Indomie Soto",
        "Pop Mie",
        "Supermi"
    ],

    "Mayora": [
        "Kopiko",
        "Beng Beng",
        "Roma Biscuit"
    ],

    "GarudaFood": [
        "Kacang Garuda",
        "Gery",
        "Pilus"
    ],

    "Coca-Cola": [
        "Coca-Cola 330ml",
        "Sprite 390ml",
        "Fanta Orange"
    ],

    "Pepsi": [
        "Pepsi Cola",
        "7UP",
        "Mirinda"
    ],

    "Nestle": [
        "Milo",
        "Nescafe",
        "KitKat"
    ],

    "Wardah": [
        "Lightening Serum",
        "Perfect Bright",
        "Hydrating Toner"
    ],

    "Make Over": [
        "Powerstay Foundation",
        "Lip Cream",
        "Eyeliner"
    ],

    "Emina": [
        "Bright Stuff",
        "Lip Tint",
        "Sun Protection"
    ],

    "L'Oreal": [
        "Revitalift",
        "Elseve Shampoo",
        "Infallible Foundation"
    ],

    "Mattel":[
        "Barbie",
        "Hot Wheels",
        "UNO"
    ],

    "Hasbro":[
        "Monopoly",
        "Nerf Elite",
        "Play-Doh"
    ],

    "LEGO":[
        "Classic",
        "City",
        "Technic"
    ],

    "Nike":[
        "Air Max",
        "Pegasus",
        "Revolution"
    ],

    "Puma":[
        "RS-X",
        "Future Rider",
        "Velocity Nitro"
    ],

    "Kalbe": [
        "Fatigon",
        "Promag",
        "Hydro Coco"
    ],

    "Blackmores": [
        "Vitamin C",
        "Multivitamin",
        "Fish Oil"
    ],

    "Entrasol": [
        "Gold",
        "Active",
        "Platinum"
    ],

    "Nike": [
        "Air Max",
        "Pegasus",
        "Revolution",
        "Court Vision",
        "Mercurial"
    ],

    "Adidas": [
        "Ultraboost",
        "Superstar",
        "Stan Smith",
        "Duramo",
        "Predator"
    ],

    "Puma": [
        "RS-X",
        "Velocity Nitro",
        "Future Rider",
        "Suede Classic"
    ],

    "Uniqlo": [
        "AIRism T-Shirt",
        "Oxford Shirt",
        "Ultra Light Down",
        "Chino Pants"
    ],

    "Zara": [
        "Slim Blazer",
        "Midi Dress",
        "Leather Jacket"
    ],

    "H&M": [
        "Basic Hoodie",
        "Regular Jeans",
        "Cotton Shirt"
    ],

    "Carter's": [
        "Baby Romper",
        "Baby Pajamas",
        "Baby Set"
    ],

    "Mothercare": [
        "Baby Onesie",
        "Baby Blanket",
        "Baby Shoes"
    ],

    "Eiger": [
        "Daypack",
        "Carrier 45L",
        "Adventure Jacket"
    ],

    "Consina": [
        "Carrier 60L",
        "Sleeping Bag",
        "Tracking Pole"
    ],

    "The North Face": [
        "Borealis",
        "Base Camp Duffel",
        "Summit Jacket"
    ],

    "Gramedia": [
        "Novel",
        "Dictionary",
        "Workbook"
    ],

    "Erlangga": [
        "Math Book",
        "Science Book",
        "English Book"
    ],

    "Faber Castell": [
        "2B Pencil",
        "Color Pencil",
        "Marker"
    ],

    "Joyko": [
        "Notebook",
        "Stapler",
        "Ballpoint"
    ],

    "Bosch": [
        "Spark Plug",
        "Brake Pad",
        "Battery"
    ],

    "Shell": [
        "Helix HX7",
        "Advance AX7",
        "Brake Fluid"
    ],

    "Castrol": [
        "Magnatec",
        "Power1",
        "EDGE"
    ],

    "Whiskas": [
        "Adult Tuna",
        "Kitten Ocean Fish",
        "Wet Food"
    ],

    "Royal Canin": [
        "Indoor",
        "Persian",
        "Mini Adult"
    ],

    "Pampers": [
        "Premium Care",
        "Baby Dry",
        "Pants"
    ],

    "MamyPoko": [
        "Extra Dry",
        "Pants Standard",
        "Royal Soft"
    ],

    "Cussons Baby": [
        "Baby Lotion",
        "Baby Powder",
        "Baby Oil"
    ],

    "Razer": [
        "DeathAdder",
        "BlackWidow",
        "Kraken"
    ],

    "Logitech": [
        "G102",
        "G Pro X",
        "MX Master 3"
    ],

    "SteelSeries": [
        "Apex Pro",
        "Arctis Nova",
        "Rival 3"
    ],

    "Yamaha": [
        "PSR-E373",
        "F310",
        "P-145"
    ],

    "Roland": [
        "FP-30X",
        "GO Keys",
        "TD-07"
    ],

    "Casio": [
        "CT-X700",
        "PX-S1100",
        "WK-6600"
    ],

    "Anker": [
        "PowerCore 10000",
        "Nano Charger",
        "Soundcore R50i"
    ],

    "Baseus": [
        "GaN Charger",
        "USB-C Hub",
        "Power Bank"
    ],

    "UGREEN": [
        "USB Hub",
        "HDMI Cable",
        "65W Charger"
    ],

    "Bantex": [
        "Lever Arch File",
        "Binder",
        "Document Tray"
    ],

    "Deli": [
        "Stapler",
        "Calculator",
        "Paper Cutter"
    ],

    "LEGO": [
        "Classic",
        "City",
        "Technic",
        "Creator"
    ],

    "Mattel": [
        "Barbie",
        "UNO",
        "Hot Wheels",
        "Thomas & Friends"
    ],

    "Hasbro": [
        "Monopoly",
        "Nerf Elite",
        "Play-Doh",
        "Transformers"
    ]

}

# ==========================================================
# PRICE
# ==========================================================

CATEGORY_PRICE_RANGE = {

    "Electronics": (300000, 10000000),
    "Computer": (5000000, 25000000),
    "Smartphone": (1500000, 18000000),
    "Home Appliances": (300000, 8000000),
    "Furniture": (200000, 7000000),

    "Kitchen": (10000, 1000000),
    "Food": (3000, 100000),
    "Beverage": (3000, 50000),
    "Health": (10000, 500000),
    "Beauty": (15000, 750000),

    "Fashion Men": (50000, 3000000),
    "Fashion Women": (50000, 3000000),
    "Fashion Kids": (30000, 1500000),
    "Sports": (50000, 5000000),
    "Outdoor": (100000, 5000000),

    "Books": (15000, 250000),
    "Stationery": (5000, 100000),
    "Automotive": (50000, 5000000),
    "Pet Supplies": (10000, 1000000),
    "Baby Products": (10000, 2000000),

    "Gaming": (50000, 15000000),
    "Music": (50000, 12000000),
    "Accessories": (10000, 3000000),
    "Office": (10000, 500000),
    "Toys": (10000, 2000000)

}

# Margin untuk menghitung cost_price

CATEGORY_MARGIN = {

    "Electronics": (0.15, 0.30),
    "Computer": (0.10, 0.20),
    "Smartphone": (0.08, 0.18),
    "Home Appliances": (0.15, 0.25),
    "Furniture": (0.20, 0.35),

    "Kitchen": (0.25, 0.45),
    "Food": (0.10, 0.20),
    "Beverage": (0.15, 0.25),
    "Health": (0.20, 0.40),
    "Beauty": (0.30, 0.60),

    "Fashion Men": (0.35, 0.60),
    "Fashion Women": (0.35, 0.60),
    "Fashion Kids": (0.30, 0.50),

    "Sports": (0.20, 0.40),
    "Outdoor": (0.25, 0.45),

    "Books": (0.20, 0.35),
    "Stationery": (0.25, 0.45),

    "Automotive": (0.20, 0.35),
    "Pet Supplies": (0.20, 0.40),
    "Baby Products": (0.20, 0.40),

    "Gaming": (0.15, 0.30),
    "Music": (0.15, 0.30),
    "Accessories": (0.30, 0.60),
    "Office": (0.25, 0.45),
    "Toys": (0.30, 0.55)

}

# ==========================================================
# STATUS
# ==========================================================

PRODUCT_STATUS = [
    "Active",
    "Discontinued"
]

PRODUCT_STATUS_WEIGHT = [95, 5]

# ==========================================================
# TAX
# ==========================================================

PRODUCT_TAX = {

    "Electronics": 11,
    "Computer": 11,
    "Smartphone": 11,
    "Home Appliances": 11,
    "Furniture": 11,
    "Kitchen": 11,
    "Food": 0,
    "Beverage": 11,
    "Health": 11,
    "Beauty": 11,
    "Fashion Men": 11,
    "Fashion Women": 11,
    "Fashion Kids": 11,
    "Sports": 11,
    "Outdoor": 11,
    "Books": 0,
    "Stationery": 11,
    "Automotive": 11,
    "Pet Supplies": 11,
    "Baby Products": 11,
    "Gaming": 11,
    "Music": 11,
    "Accessories": 11,
    "Office": 11,
    "Toys": 11
}

# ==========================================================
# HELPER
# ==========================================================

def get_price_range(category):
    return CATEGORY_PRICE_RANGE.get(category, (10000, 500000))


def get_margin(category):
    return CATEGORY_MARGIN.get(category, (0.20, 0.35))


def get_tax(category):
    return PRODUCT_TAX.get(category, 11)


def get_random_brand(category):
    return random.choice(BRANDS[category])


def get_product_models(brand):
    return PRODUCT_MODELS.get(brand, [brand])