import random

# ==========================================================
# Return Reason
# ==========================================================

RETURN_REASONS = [

    "Damaged Product",

    "Wrong Item Sent",

    "Defective Product",

    "Expired Product",

    "Customer Changed Mind",

    "Late Delivery",

    "Quality Issue",

    "Incorrect Size",

    "Duplicate Order"

]

RETURN_REASON_WEIGHT = [

    20,
    10,
    18,
    5,
    22,
    5,
    10,
    7,
    3

]

# ==========================================================
# Return Status
# ==========================================================

RETURN_STATUS = [

    "Completed",

    "Pending",

    "Rejected"

]

RETURN_STATUS_WEIGHT = [

    92,

    6,

    2

]

# ==========================================================
# Refund Method
# ==========================================================

REFUND_METHODS = [

    "Cash",

    "Bank Transfer",

    "Store Credit",

    "E-Wallet",

    "Voucher"

]

REFUND_METHOD_WEIGHT = [

    15,

    25,

    15,

    35,

    10

]

# ==========================================================
# Return Quantity
# ==========================================================

def get_return_quantity(

    sales_quantity

):

    if sales_quantity <= 1:

        return 1

    return random.randint(

        1,

        sales_quantity

    )

# ==========================================================
# Return Reason
# ==========================================================

def get_return_reason():

    return random.choices(

        RETURN_REASONS,

        weights=RETURN_REASON_WEIGHT,

        k=1

    )[0]

# ==========================================================
# Return Status
# ==========================================================

def get_return_status():

    return random.choices(

        RETURN_STATUS,

        weights=RETURN_STATUS_WEIGHT,

        k=1

    )[0]

# ==========================================================
# Refund Method
# ==========================================================

def get_refund_method():

    return random.choices(

        REFUND_METHODS,

        weights=REFUND_METHOD_WEIGHT,

        k=1

    )[0]

# ==========================================================
# Refund Amount
# ==========================================================

def calculate_refund_amount(

    taxable_amount,

    tax_amount

):

    return int(

        taxable_amount

        +

        tax_amount

    )