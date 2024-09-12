import datetime

from constants.biznex_constants import (
    ADDRESS, CRITICAL_LEVEL_PROMPT, CUSTOMER_MENU,
    CUSTOMER_QUOTATION_EDIT, CUSTOMER_QUOTATION_ITEM_HEADERS, DELIVERY_DATE,
    DONE, ENTER_CUSTOMER_QUOTATION_ID, ENTER_DELIVERY_ADDRESS,
    ENTER_DELIVERY_DATE, ENTER_ITEMS, ENTER_PAYMENT_METHOD,
    ENTER_PHONE_NUMBER, ENTER_PO_NUMBER, ENTER_VENDOR_QUOTATION_ID,
    ENTER_YOUR_CHOICE, ENTER_YOUR_EMAIL, ENTER_YOUR_USER_ID,
    ENTER_YOUR_VENDOR_ID, ENTER_YOUR_WAREHOUSE_ID, FORM_ITEMS,
    INVALID_CRITICAL_LEVEL, INVALID_CRITICAL_LEVEL_LOGGER, INVALID_ITEM_QUANTITY,
    INVALID_NUMBER_ERROR, INVALID_PAYMENT_METHOD, ITEM_CRITICAL_LEVEL,
    ITEM_DELETION_PROMPT, ITEM_NAME, ITEM_NAME_PROMPT,
    ITEM_NUMBER_PROMPT, ITEM_QUANTITY, ITEM_STATUS,
    ITEM_STATUS_AVAILABLE, PAST_DELIVERY_DATE, PAYMENT_METHOD,
    PO_STATUS, QUANTITY_NOT_ZERO,
    QUANTITY_TO_BE_CHANGES, STATUS, STATUS_SENT,
    SUCCESSFUL_QUOTATION_UPDATE, TOTAL_PRICE, USER_DICT_COMPANY_NAME,
    USER_DICT_EMAIL, USER_DICT_NAME, USER_DICT_PHONE_NUMBER,
    USER_DICT_USER_ID, VENDOR_ID, VENDOR_P2P_MANAGEMENT,
    VENDOR_QUOTATION_ID, VALID_PAYMENT_METHODS, WAREHOUSE_ITEM_ZERO_LOGGER,
    WAREHOUSE_MANAGEMENT, CUSTOMER_QUOTATION_ID, STATUS_PROCESSING, CUSTOMER_ID, PURCHASE_ORDER_EDIT, STATUS_INACTIVE,
    VENDOR_QUOTATION_HEADERS, DATE
)
from custom_exceptions.warehouse_exception import WarehouseException
from p2p_controller import generate_purchase_order, get_purchase_order_by_po_number
from resources.logging_config import logger
from service.customer_service import (
    add_item, change_item_quantity, create_ware_house, delete_item,
    get_vendor_quotations_by_customer_id, get_warehouse_by_id,
    get_vendor_quotation_by_id, is_warehouse_available
)
from service.p2p_service import update_purchase_order
from service.user_service import get_by_user_id
from service.vendor_service import get_quotation, set_quotations, update_customer_quotation
from tabulate import tabulate
from utils.common_utils import generate_random_string
from utils.user_input_validation import (
    email_validation, is_valid_future_date,
    is_valid_number, phone_number_validation
)


def customer_menu(user):
    """
    Prints the menu options and get the options from the user to perform the actions accordingly

    Parameters:
        user (dict) : Used to access the content only ment for that user.

    """
    choice = ""
    while True:
        print(CUSTOMER_MENU)
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                warehouse_management(user)
            case 2:
                vendor_and_p2p_management(user)
            case 3:
                return
            case _:
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 3")


def warehouse_management(user):  # todo use the user parameter for security
    """
        Manages warehouse operations for a given user.

        This function provides a menu-driven interface for managing a warehouse, including
        viewing, adding, deleting, and updating items, as well as creating a new warehouse.
        The user is prompted to enter choices, and the appropriate action is taken based on the input.

        Parameters:
            user (dict): The user dictionary containing user details.

    """
    warehouse_id = create_ware_house()
    logger.info(f"Created an empty warehouse for user with warehouse id {warehouse_id}")
    choice = ""
    while True:
        print(WAREHOUSE_MANAGEMENT)
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")  # todo send the trace back
            continue

        match choice:
            case 1:
                view_warehouse()
            case 2:
                add_item_to_warehouse()
            case 3:
                delete_item_from_warehouse()
            case 4:
                update_quantity()
            case 5:
                warehouse_id = create_ware_house()
                logger.info(f"Created an empty warehouse for user with warehouse id {warehouse_id}")
            case 6:
                return
            case _:
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 5")


def vendor_and_p2p_management(user):
    """
    Handles the Vendor and Peer-to-Peer (P2P) management menu,
    allowing users to perform various operations such as
    requesting quotations, viewing vendor quotations, issuing purchase orders, and editing quotations.

    Parameters:
        user (dict): A dictionary containing information about the current user.

    """
    choice = ""
    while True:
        print(VENDOR_P2P_MANAGEMENT)
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                request_quotation()
            case 2:
                View_vendor_quotation()
            case 3:
                issue_purchase_order(user)
            case 4:
                view_purchase_order(user)
            case 5:
                edit_quotation(user)
            case 6:
                edit_purchase_order(user)
            case 7:
                view_all_vendor_quotations()
            case 8:
                return
            case _:
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 6   ")


def view_warehouse():
    warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
    warehouse = get_warehouse_by_id(warehouse_id)

    if warehouse is None:
        logger.error(f"No such ware house with warehouse id {warehouse_id} is available")
    else:
        logger.debug(f"Showing ware house {warehouse_id}")
        display_data_in_table(warehouse)


def add_item_to_warehouse():
    """
        Adds a new item to a specified warehouse.

        The function prompts the user for details about the new item, including its name, quantity, and critical stock level.
        It then validates the inputs and adds the item to the specified warehouse if it exists.

        Steps:
            1. Requests the warehouse ID and verifies its existence.
            2. Prompts the user to input the item name.
            3. Continuously prompts the user for the item quantity until a valid number is provided.
            4. Sets the item status to 'Available' by default.
            5. Continuously prompts the user for the critical stock level until a valid number is provided
               and ensures it is between 1 and the item quantity.
            6. Generates a unique item ID and adds the item to the warehouse.

        """
    new_item = {}
    warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
    if not is_warehouse_available(warehouse_id):
        logger.error(f"No such warehouse with id {warehouse_id} found ")
        return
    item_details = {ITEM_NAME: input(ITEM_NAME_PROMPT)}
    while True:
        item_quantity = input(ITEM_QUANTITY)
        if is_valid_number(item_quantity):
            item_details[ITEM_QUANTITY] = int(item_quantity)
            break
        else:
            logger.error(f"User entered invalid item quantity {item_quantity}")
            print(INVALID_ITEM_QUANTITY)

    item_details[ITEM_STATUS] = ITEM_STATUS_AVAILABLE

    while True:
        critical_level = input(CRITICAL_LEVEL_PROMPT)
        if is_valid_number(critical_level) and (0 < int(critical_level) < item_details[ITEM_QUANTITY]):
            item_details[ITEM_CRITICAL_LEVEL] = int(critical_level)
            break
        else:
            logger.error(INVALID_CRITICAL_LEVEL_LOGGER)
            print(INVALID_CRITICAL_LEVEL)

    item_id = generate_random_string()
    new_item[item_id] = item_details
    add_item(warehouse_id, new_item)


def delete_item_from_warehouse():
    """
        Deletes an item from a specified warehouse.

        The function prompts the user for the warehouse ID and item number,
        verifies the existence of the warehouse, and attempts to delete the specified item.
        If the warehouse or item does not exist, appropriate error messages are logged.
    """
    warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
    if not is_warehouse_available(warehouse_id):
        logger.error(f"No such warehouse with the given id {warehouse_id} is present ")
        return
    item_number = input(ITEM_NUMBER_PROMPT)
    if delete_item(warehouse_id, item_number):
        logger.info(ITEM_DELETION_PROMPT)
    else:
        logger.error(f"No such item with item number {item_number} is found in warehouse")


def update_quantity():
    """
        Updates the quantity of an item in a specified warehouse.

        This function allows the user to update the quantity of a particular item in a warehouse
        by specifying the warehouse ID, item number, and a delta value (which can be positive or negative).
        It performs input validation, checks for the existence of the warehouse and item, and handles errors
        gracefully, logging appropriate messages based on the outcome.
    """
    warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
    if not is_warehouse_available(warehouse_id):
        logger.error(f"No such warehouse with the given id {warehouse_id} is present ")
        return
    item_number = input(ITEM_NUMBER_PROMPT)
    delta = input(QUANTITY_TO_BE_CHANGES)
    if not is_valid_number(delta):
        logger.error(f"User gave invalid number {delta}")
        print(f"{delta} is not a valid number. Must be a negative or positive number")
    delta = int(delta)
    try:
        if change_item_quantity(warehouse_id, item_number, delta):
            logger.info(f"Item quantity changed for item numer {item_number}")
        else:
            logger.error(f"No such item number {item_number} found in warehouse")
    except WarehouseException as e:
        logger.exception(e.message)
        print(WAREHOUSE_ITEM_ZERO_LOGGER)


def get_quotation_form():
    """
    Collects and returns the necessary details for a quotation request from the user.

    Returns:
        dict: A dictionary containing user ID, items with quantities, delivery date, and address.
    """
    quotation_form = {}
    while True:
        vendor_id = input(ENTER_YOUR_VENDOR_ID)
        if get_by_user_id(vendor_id) is None:
            logger.error(f"No such vendor found with id {vendor_id}")
        else:
            logger.debug(f"Fetched user id {vendor_id}")
            quotation_form[VENDOR_ID] = vendor_id
            break

    while True:
        user_id = input(ENTER_YOUR_USER_ID).strip()
        user = get_by_user_id(user_id)
        if user is None:
            logger.error(f"No such user_id {user_id} is present in database ")
        else:
            quotation_form[USER_DICT_NAME] = user[USER_DICT_NAME]
            quotation_form[USER_DICT_EMAIL] = user[USER_DICT_EMAIL]
            quotation_form[USER_DICT_PHONE_NUMBER] = user[USER_DICT_PHONE_NUMBER]
            quotation_form[USER_DICT_COMPANY_NAME] = user[USER_DICT_COMPANY_NAME]
            quotation_form[STATUS] = STATUS_SENT
            break

    items = {}
    while True:
        item_name = input(ENTER_ITEMS).strip()
        if item_name.lower() == DONE:
            break
        quantity = input(f"Enter quantity for {item_name}: ").strip()
        if not quantity.isdigit() or (int(quantity) == 0):
            print(QUANTITY_NOT_ZERO)
            continue
        items[item_name] = int(quantity)

    quotation_form[FORM_ITEMS] = items

    while True:
        delivery_date = input(ENTER_DELIVERY_DATE).strip()
        if is_valid_future_date(delivery_date):
            quotation_form[DELIVERY_DATE] = delivery_date
            break
        else:
            logger.error(PAST_DELIVERY_DATE)
            logger.error(f"User gave past date {delivery_date}")

    quotation_form[ADDRESS] = input(ENTER_DELIVERY_ADDRESS).strip()

    logger.debug("Quotation Form Details Collected:")
    print(quotation_form)
    return quotation_form


def request_quotation():
    """
    This function is responsible for requesting quotation from vendor
    """
    quotation_form = get_quotation_form()
    quotation_id = set_quotations(quotation_form)
    logger.info(f"Users quotation was successfully sent. Their quotation_id is {quotation_id}")


def View_vendor_quotation():
    """
    This function used to view the vendor quotation given to the customer
    """
    customer_quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
    vendor_quotation = get_vendor_quotations_by_customer_id(customer_quotation_id)
    if vendor_quotation is None:
        logger.error(f"No quotation with such vendor quotation {customer_quotation_id} is found")
        return
    else:
        print_vendor_quotations(vendor_quotation)


def issue_purchase_order(user):
    """
    This function is used to issue a purchase order to specified vendor
    """
    purchase_order = {}
    vendor_quotation_id = input(ENTER_VENDOR_QUOTATION_ID)
    customer_quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
    vendor_quotation = get_vendor_quotation_by_id(vendor_quotation_id, customer_quotation_id)
    if vendor_quotation is None:
        logger.error(f"No quotation with such vendor quotation id {vendor_quotation_id} is found")
        return
    vendor_id = get_quotation(customer_quotation_id)
    if vendor_id is None:
        logger.error(f"No quotation with such customer quotation id {vendor_quotation_id} is found")
        return
    purchase_order[CUSTOMER_ID] = user[USER_DICT_USER_ID]
    purchase_order[VENDOR_ID] = vendor_id
    purchase_order[VENDOR_QUOTATION_ID] = vendor_quotation_id
    purchase_order[CUSTOMER_QUOTATION_ID] = customer_quotation_id
    purchase_order[ADDRESS] = input(ENTER_DELIVERY_ADDRESS)
    purchase_order[TOTAL_PRICE] = vendor_quotation[TOTAL_PRICE]
    purchase_order[PO_STATUS] = STATUS_INACTIVE
    purchase_order[STATUS] = STATUS_SENT

    while True:
        payment_method = input(ENTER_PAYMENT_METHOD).strip().lower()
        if payment_method in VALID_PAYMENT_METHODS:
            print(f"Payment method accepted: {payment_method}")
            purchase_order[PAYMENT_METHOD] = payment_method
            break
        else:
            logger.error(INVALID_PAYMENT_METHOD)
    po_number = generate_purchase_order(purchase_order)
    logger.info(f"Purchase order was successfully issued by customer {user[USER_DICT_USER_ID]}")
    print(f"Your purchase order number is {po_number}")
    return


def view_purchase_order(user):
    """
    This is used to view the purchase order given by customer
    """
    purchase_order_number = input(ENTER_PO_NUMBER)
    purchase_order = get_purchase_order_by_po_number(purchase_order_number, user[USER_DICT_USER_ID])
    if purchase_order is None:
        logger.error(f"No such purchase order number present in db {purchase_order_number}")
    print(purchase_order)


def edit_purchase_order(user):
    purchase_order_number = input(ENTER_PO_NUMBER)
    edited_purchase_order = get_purchase_order_by_po_number(purchase_order_number, user[USER_DICT_USER_ID])
    print("your po is ")
    print(edited_purchase_order)
    if edited_purchase_order is None:
        logger.error(f"No such purchase order number present in db {purchase_order_number}")
        return
    elif edited_purchase_order[STATUS] != STATUS_SENT:
        if edited_purchase_order[STATUS] == STATUS_PROCESSING:
            logger.error(f"User {user[USER_DICT_USER_ID]} attempts to edit the purchase order that is already viewed by "
                         f"the customer")
            return
        else:
            logger.error(f"User {user[USER_DICT_USER_ID]} attempts to edit the purchase order that is Inactive")
            return

    while True:
        print(PURCHASE_ORDER_EDIT)
        choice = ""
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue
        flag = False
        match choice:
            case 1:
                edited_purchase_order[ADDRESS] = input(ENTER_DELIVERY_ADDRESS)
            case 2:
                logger.info(f"User {user[USER_DICT_USER_ID]} changed the status changed to inactive")
                edited_purchase_order[STATUS] = STATUS_INACTIVE
            case 3:
                edited_purchase_order[PAYMENT_METHOD] = get_valid_payment_method()
            case 4:
                if flag:
                    logger.info(f"Purchase order updated successfully by user {user[USER_DICT_USER_ID]}")
                    update_purchase_order(edited_purchase_order, purchase_order_number)
                    return
                return
            case _:
                logger.error("Invalid input")


def edit_quotation(user):
    quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
    edited_quotation = get_quotation(quotation_id)
    if edited_quotation is None:
        logger.error(f"No such quotation id {quotation_id} found in the database")
        return
    elif edited_quotation[STATUS] != STATUS_SENT:
        if edited_quotation[STATUS] == STATUS_PROCESSING:
            logger.error(f"User {user[USER_DICT_USER_ID]} attempts to edit the quotation that is already viewed by "
                         f"the customer")
            return
        else:
            logger.error(f"User {user[USER_DICT_USER_ID]} attempts to edit the quotation that is Inactive")
            return

    while True:
        print(CUSTOMER_QUOTATION_EDIT)
        choice = ""
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue
        flag = False
        match choice:
            case 1:
                edited_quotation[USER_DICT_EMAIL] = get_valid_email()
                flag = True
            case 2:
                edited_quotation[USER_DICT_PHONE_NUMBER] = get_valid_phone_number()
                flag = True
            case 3:
                logger.info(f"User {user[USER_DICT_USER_ID]} changed the status changed to inactive")
                edited_quotation[STATUS] = STATUS_INACTIVE
                flag = True
            case 4:
                edited_quotation[DELIVERY_DATE] = get_valid_delivery_date()
                flag = True
            case 5:
                edited_quotation[ADDRESS] = input(ENTER_DELIVERY_ADDRESS)
                flag = True
            case 6:
                edited_quotation[FORM_ITEMS] = update_material_quantities(edited_quotation[FORM_ITEMS])
                flag = True
            case 7:
                if flag:
                    logger.info(SUCCESSFUL_QUOTATION_UPDATE)
                    update_customer_quotation(quotation_id, edited_quotation)
                    return
                return
            case _:
                logger.error("Invalid Input")


def update_material_quantities(material_quantities):
    """
    Updates the values in the provided dictionary by prompting the user for new values.

    Parameters:
        material_quantities (dict): Dictionary containing materials and their quantities.

    Returns:
        material_quantities (dict) : items with updated value
    """
    for material, old_value in material_quantities.items():
        while True:
            new_value = input(f"Enter new quantity for {material} (current: {old_value}): ").strip()
            if is_valid_number(new_value):
                material_quantities[material] = new_value
                break
            else:
                logger.error(INVALID_NUMBER_ERROR)

    return material_quantities


def view_all_vendor_quotations():
    """
    Used to view all the quotations given by vendor
    """
    customer_quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
    vendor_quotation = get_vendor_quotations_by_customer_id(customer_quotation_id)
    if vendor_quotation is None:
        logger.error(f"No such customer quotation {customer_quotation_id} is available")
        return
    print(vendor_quotation)


def display_data_in_table(data):
    """
    Displays the given data in a tabular format.

    Parameters:
        data (list of dict): List containing item information as dictionaries.
    """
    table_data = []

    for item_dict in data:
        for item_id, item_info in item_dict.items():
            row = [item_id, item_info['item_name'], item_info['item_quantity'], item_info['item_status'],
                   item_info['critical_level']]
            table_data.append(row)

    print(tabulate(table_data, CUSTOMER_QUOTATION_ITEM_HEADERS, tablefmt="grid"))


def get_valid_email():
    """
       Prompts the user to enter an email address and validates it using the email validation function.

       Returns:
           str: The validated email address.
    """
    while True:
        edited_email = input(ENTER_YOUR_EMAIL).strip()
        if email_validation(edited_email):
            return edited_email
        else:
            logger.warning(f"User gave invalid email address {edited_email}")


def get_valid_phone_number():
    """
        Prompts the user to enter a phone number and validates it using the phone number validation function.

        Returns:
            str: The validated phone number.
    """
    while True:
        edited_phone_number = input(ENTER_PHONE_NUMBER).strip()
        if phone_number_validation(edited_phone_number):
            return edited_phone_number
        else:
            logger.warning(f"User gave invalid phone number {edited_phone_number}")


def get_valid_delivery_date():
    """
        Prompts the user to enter a delivery date and validates it to ensure it is a future date.

        Returns:
            str: The validated delivery date.
    """
    while True:
        edited_delivery_date = input(ENTER_DELIVERY_DATE).strip()
        if is_valid_future_date(edited_delivery_date):
            return edited_delivery_date
        else:
            logger.error(f"User gave past date {edited_delivery_date}")


def get_valid_payment_method():
    while True:
        payment_method = input(ENTER_PAYMENT_METHOD).strip().lower()
        if payment_method in VALID_PAYMENT_METHODS:
            print(f"Payment method accepted: {payment_method}")
            return payment_method
        else:
            logger.error(INVALID_PAYMENT_METHOD)


def print_vendor_quotations(vendor_quotations):
    """
    This function is used to print the given vendor quotations in tabular column formate
    This function uses tabulate a third party library.
    """
    headers = VENDOR_QUOTATION_HEADERS
    table_data = []
    for customer_quotation_id, details in vendor_quotations.items():
        row = [
            customer_quotation_id,
            details.get(CUSTOMER_QUOTATION_ID, ''),
            details.get(USER_DICT_NAME, ''),
            details.get(USER_DICT_EMAIL, ''),
            details.get(USER_DICT_PHONE_NUMBER, ''),
            details.get(TOTAL_PRICE, ''),
            details.get(DATE, '').strftime('%d/%m/%Y') if isinstance(details.get('date'), datetime.date) else details.get('date', ''),
            details.get(VENDOR_ID, ''),
            details.get(STATUS, '')
        ]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

