from tabulate import tabulate

from constant.constant import (
    USER_DICT_EMAIL, USER_DICT_NAME,
    USER_DICT_PHONE_NUMBER, USER_DICT_USER_ID, VENDOR_ID, STATUS,
    CUSTOMER_QUOTATION_HEADERS, USER_DICT_COMPANY_NAME,
    DELIVERY_DATE, DELIVERY_ADDRESS, PO_STATUS,  STATUS_INACTIVE,
    VENDOR_EMAIL)
from controller.procure_to_payment import get_purchase_order_by_po_number
from resources.config import logger
from service.customer import set_vendor_quotations
from service.procure_to_payment import get_po_by_id, update_purchase_order, get_by_po_number
from service.vendor import get_quotation, get_all_quotations


def view_active_quotation_request(user):
    """
       Displays active quotation requests for the specified vendor.

       Parameters:
           user (dict): Dictionary containing user information, including user ID.

       This function retrieves and prints active quotations for the vendor specified by
       the user ID from the `user` dictionary.
    """
    print_active_customer_quotations(get_active_quotations(user[USER_DICT_EMAIL]))


def print_quotation_by_id():
    """
       Prints the details of a quotation based on the provided quotation ID.

       This function prompts the user for a quotation ID, retrieves the quotation details
       from the database, and prints them. If the quotation ID is not found, an error
       message is logged.
    """
    quotation_id = input("Enter the quotation id to continue")
    quotation = get_quotation(quotation_id)
    if quotation is None:
        logger.error(f"No such quotation id {quotation_id} found in the database")
    else:
        print(quotation)


def get_active_quotations(vendor_email):
    """
       Retrieves all active quotations for a specified vendor.

       Parameters:
           vendor_email (str): The email ID of the vendor for whom to retrieve quotations.

       Returns:
           list: A list of dictionaries where each dictionary represents an active
                 quotation associated with the specified vendor.

       This function filters quotations based on the vendor ID and status, returning
       only those that are active.
       """
    quotations = get_all_quotations()
    return [
        {uid: details} for uid, details in quotations.items()
        if details.get(VENDOR_EMAIL) == vendor_email and details.get(STATUS) != STATUS_INACTIVE
    ]


def get_quotation_by_id(quotation_id):
    """
       Retrieves a quotation based on the provided quotation ID.

       Parameters:
           quotation_id (str): The ID of the quotation to retrieve.

       Returns:
           dict: The quotation details if found, otherwise None.

       This function fetches a quotation from the database using the provided ID.
    """
    return get_quotation(quotation_id)


def issue_quotation(vendor_quotation):
    """
        Issues a new quotation for the vendor by generating it and updating records.

        Parameters:
            vendor_quotation (dict): Dictionary containing user information, including user ID.

        This function generates a new quotation using the `generate_quotation` function
        and then updates the records by setting the vendor's quotations with
        `set_vendor_quotations`.
    """
    set_vendor_quotations(vendor_quotation)


def get_purchase_order(user):
    """
    This function is used to get the purchase order
    """
    purchase_order = get_po_by_id(user[USER_DICT_USER_ID])
    print(purchase_order)


def print_active_customer_quotations(quotations_list):
    headers = CUSTOMER_QUOTATION_HEADERS
    table_data = []
    for quotation in quotations_list:
        for customer_quotation_id, details in quotation.items():
            items_string = ', '.join([f"{item}: {quantity}" for item, quantity in details['items'].items()])
            row = [
                customer_quotation_id,
                details.get(VENDOR_ID, ''),
                details.get(USER_DICT_NAME, ''),
                details.get(USER_DICT_EMAIL, ''),
                details.get(USER_DICT_PHONE_NUMBER, ''),
                details.get(USER_DICT_COMPANY_NAME, ''),
                details.get(STATUS, ''),
                items_string,
                details.get(DELIVERY_DATE, ''),
                details.get(DELIVERY_ADDRESS, '')
            ]
            table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt='grid'))


def view_purchase_order(user, purchase_order_number):
    """
    This is used to view the purchase order given by customer
    """
    purchase_order = get_by_po_number(purchase_order_number, user[USER_DICT_USER_ID])
    if purchase_order is None:
        logger.error(f"No such purchase order number present in db {purchase_order_number}")
    print(purchase_order)


def edit_po_status(user, purchase_order_id, po_status):
    """
    This function is used to edit the purchase order status

    Parameters:
        user (dict) : User details of the logged-in user.
        purchase_order_id (str)
        po_status (str) : Status of purchase order
    """
    purchase_order = get_purchase_order_by_po_number(purchase_order_id, user[USER_DICT_USER_ID])
    if purchase_order is None:
        logger.error(f"No such purchase order is found with id {purchase_order_id}")
        return
    purchase_order[PO_STATUS] = po_status
    update_purchase_order(purchase_order, purchase_order_id)
