from constants.constants import CUSTOMER_ID, VENDOR_QUOTATION_ID, PO_STATUS, STATUS_INACTIVE, VENDOR_ID
from utils.common_utils import generate_random_string

purchase_orders = {}


def create_purchase_order(purchase_order):
    """
        Creates a new purchase order and assigns it a unique purchase order number.

        Parameters:
            purchase_order (dict): The purchase order details to be added.

        Returns:
            str: The unique purchase order number generated for the new purchase order.
    """
    purchase_order_number = ""
    while True:
        purchase_order_number = generate_random_string()
        if purchase_order_number not in purchase_orders:
            break
    purchase_orders[purchase_order_number] = purchase_order
    return purchase_order_number


def get_by_po_number(po_number, user_id):
    """
        Retrieves a purchase order based on the purchase order number and user ID.

        Parameters:
            po_number (str): The purchase order number.
            user_id (str): The user ID of the customer.

        Returns:
            dict or None: The matching purchase order dictionary if found; otherwise, None.
    """
    purchase_order = purchase_orders.get(po_number)
    if (purchase_order is None
            or purchase_order[CUSTOMER_ID] != user_id
            or purchase_order[VENDOR_ID] != user_id):
        return None
    else:
        return purchase_order


def get_by_vendor_quotation_id(vendor_quotation_id):
    """
        Retrieves all active purchase orders for a given vendor quotation ID.

        Parameters:
            vendor_quotation_id (str): The ID of the vendor quotation.

        Returns:
            list: A list of dictionaries containing the purchase order IDs and purchase order details.
    """
    return [
        {po_id, purchase_order} for po_id, purchase_order in purchase_orders
        if purchase_order[VENDOR_QUOTATION_ID] == vendor_quotation_id
           and (purchase_order[PO_STATUS] != STATUS_INACTIVE)
    ]


def get_po_by_id(vendor_id):
    """
        Retrieves a purchase order for a given vendor ID that is not marked as inactive.

        Parameters:
            vendor_id (str): The vendor ID.

        Returns:
            dict or None: The matching purchase order dictionary if found; otherwise, None.
    """
    for po_id, purchase_order in purchase_orders.items():
        if (vendor_id in purchase_order) and (purchase_order[PO_STATUS] != STATUS_INACTIVE):
            return {po_id, purchase_order}


def update_purchase_order(edited_purchase_order, purchase_order_number):
    """
    This function updates the old purchase order with new purchase order details
    :param edited_purchase_order:
    :param purchase_order_number:
    :return:
    """
    purchase_orders[purchase_order_number] = edited_purchase_order


