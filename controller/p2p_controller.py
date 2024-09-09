from service.p2p_service import create_purchase_order, get_by_po_number


def generate_purchase_order(purchase_order):
    """
    Creates a new purchase order based on the provided details.

    Parameters:
        purchase_order (dict): Dictionary containing details of the purchase order
                               to be created.

    Returns:
        dict: The newly created purchase order.

    """
    return create_purchase_order(purchase_order)


def get_purchase_order_by_po_number(po_number, user_id):
    """
    Retrieves a purchase order based on the provided purchase order number.

    Parameters:
        po_number (str): The purchase order number to retrieve.

    Returns:
        dict: The details of the purchase order if found, otherwise None.
    """
    return get_by_po_number(po_number, user_id)
