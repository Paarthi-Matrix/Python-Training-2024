import datetime

from tabulate import tabulate

from constants.biznex_constants import (
    CUSTOMER_QUOTATION_NUMBER, FORM_ITEMS,
    USER_DICT_EMAIL, USER_DICT_NAME,
    USER_DICT_PHONE_NUMBER, USER_DICT_USER_ID,
    VENDOR_MENU, VENDOR_ID, STATUS,
    TOTAL_PRICE, NO_ACTIVE_QUOTATION,
    YOUR_ACTIVE_QUOTATIONS, SELECT_ONE_QUOTATION,
    ENTER_TOTAL_PRICE, VALID_TOTAL_PRICE_ERROR, STATUS_SENT, CUSTOMER_QUOTATION_HEADERS, USER_DICT_COMPANY_NAME,
    DELIVERY_DATE, DELIVERY_ADDRESS, ENTER_PO_NUMBER, PO_STATUS_UPDATE_PROMPT, PO_STATUS, PO_STATUS_ITEM_SHIPPED,
    PO_STATUS_CANCELLED, PO_STATUS_PROCESSING, PO_STATUS_OUT_FOR_DELIVERY, PO_STATUS_DELIVERED)
from controller.p2p_controller import get_purchase_order_by_po_number
from resources.logging_config import logger
from service.customer_service import set_vendor_quotations
from service.p2p_service import get_po_by_id, update_purchase_order
from service.user_service import get_by_user_id
from service.vendor_service import get_quotation, get_all_quotations
from utils.user_input_validation import is_valid_number


def vendor_management(user):
    """
        Manages vendor operations based on user input from a menu.

        Parameters:
            user (dict): Dictionary containing user information, including user ID.

        This function presents a menu to the vendor and processes the user's choice
        to perform actions such as viewing active quotation requests, issuing quotations,
        or returning to the main menu. It handles invalid choices and logs appropriate messages.
    """
    choice = ""
    while True:
        print(VENDOR_MENU)
        try:
            choice = int(input("Enter your choice"))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                view_active_quotation_request(user)
            case 2:
                issue_quotation(user)
            case 3:
                edit_po_status(user)
            case 4:
                get_purchase_order(user)
            case 5:
                return
            case _:
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 5")


def view_active_quotation_request(user):
    """
       Displays active quotation requests for the specified vendor.

       Parameters:
           user (dict): Dictionary containing user information, including user ID.

       This function retrieves and prints active quotations for the vendor specified by
       the user ID from the `user` dictionary.
    """
    (print_active_customer_quotations(get_active_quotations(user[USER_DICT_USER_ID])))


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


def get_active_quotations(vendor_id):
    """
       Retrieves all active quotations for a specified vendor.

       Parameters:
           vendor_id (str): The ID of the vendor for whom to retrieve quotations.

       Returns:
           list: A list of dictionaries where each dictionary represents an active
                 quotation associated with the specified vendor.

       This function filters quotations based on the vendor ID and status, returning
       only those that are active.
       """
    quotations = get_all_quotations()
    return [
        {uid: details} for uid, details in quotations.items()
        if details.get("vendor_id") == vendor_id and details.get("status") != "Inactive"
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


def generate_quotation(user):
    """
        Generates a new quotation for the vendor based on active quotations and user input.

        Parameters:
            user (dict): Dictionary containing user information, including user ID.

        Returns:
            dict: A dictionary containing the generated quotation details, including
                  customer quotation number, vendor details, unit prices, total price,
                  and status.

        This function allows the vendor to select an active quotation, enter unit prices
        for items, and provide a total price. It then constructs and returns a new
        quotation with the current date and status set to "Sent". If no active quotations
        are available, it logs a warning and returns None.
    """
    vendor_quotation = {}
    vendor_id = user[USER_DICT_USER_ID]
    active_quotations = get_active_quotations(vendor_id)
    if active_quotations is None:
        logger.warning(NO_ACTIVE_QUOTATION)
        return
    print(YOUR_ACTIVE_QUOTATIONS)
    print_active_customer_quotations(active_quotations)
    print(SELECT_ONE_QUOTATION)

    while True:
        flag = 0
        quotation_id = input("Enter the customer quotation id")
        for quotation in active_quotations:
            if quotation_id in quotation:
                vendor_quotation[CUSTOMER_QUOTATION_NUMBER] = quotation_id
                flag = 1
                break
        if flag == 0:
            logger.error(f"No such active quotation with id {quotation_id} is found")
        else:
            break

    vendor_details = get_by_user_id(vendor_id)
    vendor_quotation[USER_DICT_NAME] = vendor_details[USER_DICT_NAME]
    vendor_quotation[USER_DICT_EMAIL] = vendor_details[USER_DICT_EMAIL]
    vendor_quotation[USER_DICT_PHONE_NUMBER] = vendor_details[USER_DICT_PHONE_NUMBER]
    customer_quotation = get_quotation_by_id(vendor_quotation[CUSTOMER_QUOTATION_NUMBER])
    customer_requested_items = customer_quotation[FORM_ITEMS]
    unit_price = {}
    for item, quantity in customer_requested_items.items():
        while True:
            price = input(f"Enter the unit price for {item}: ")
            if is_valid_number(price):
                unit_price[item] = price
                break
            else:
                logger.error(f"User gave invalid input for unit price of {item}")

    while True:
        total_price = input(ENTER_TOTAL_PRICE)
        if is_valid_number(total_price):
            vendor_quotation[TOTAL_PRICE] = total_price
            break
        else:
            logger.error(VALID_TOTAL_PRICE_ERROR)

    vendor_quotation["date"] = datetime.date.today()
    vendor_quotation[VENDOR_ID] = vendor_id
    vendor_quotation[STATUS] = STATUS_SENT
    return vendor_quotation


def issue_quotation(user):
    """
        Issues a new quotation for the vendor by generating it and updating records.

        Parameters:
            user (dict): Dictionary containing user information, including user ID.

        This function generates a new quotation using the `generate_quotation` function
        and then updates the records by setting the vendor's quotations with
        `set_vendor_quotations`.
    """
    vendor_quotation = generate_quotation(user)
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


def view_purchase_order(user):
    """
    This is used to view the purchase order given by customer
    """
    purchase_order_number = input(ENTER_PO_NUMBER)
    purchase_order = get_purchase_order_by_po_number(purchase_order_number, user[USER_DICT_USER_ID])
    if purchase_order is None:
        logger.error(f"No such purchase order number present in db {purchase_order_number}")
    print(purchase_order)


def edit_po_status(user):
    """
    This function is used to edit the purchase order status

    Parameters:
        user (dict) : User details of the logged in user.
    """
    purchase_order_id = input(ENTER_PO_NUMBER)
    purchase_order = get_purchase_order_by_po_number(purchase_order_id, user[USER_DICT_USER_ID])
    if purchase_order is None:
        logger.error(f"No such purchase order is found with id {purchase_order_id}")
        return
    choice = ""
    flag = True
    while True:
        print(PO_STATUS_UPDATE_PROMPT)
        try:
            choice = int(input("Enter your choice"))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                purchase_order[PO_STATUS] = PO_STATUS_ITEM_SHIPPED
                flag = False
            case 2:
                purchase_order[PO_STATUS] = PO_STATUS_CANCELLED
                flag = False
            case 3:
                purchase_order[PO_STATUS] = PO_STATUS_PROCESSING
                flag = False
            case 4:
                purchase_order[PO_STATUS] = PO_STATUS_OUT_FOR_DELIVERY
                flag = False
            case 5:
                purchase_order[PO_STATUS] = PO_STATUS_DELIVERED
                flag = False
            case 6:
                if not flag:
                    update_purchase_order(purchase_order, purchase_order_id)
                    return
                return
            case _:
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 5")