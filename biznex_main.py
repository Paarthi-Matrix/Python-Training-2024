import datetime
import json
import os

from tabulate import tabulate

from constants.constants import (
    CONFORMATION_PROMPT, CUSTOMER_CATEGORY_NAME,
    CUSTOMER_VENDOR_CHOICE, END_GREETING_MESSAGE,
    ENTER_COMPANY_NAME, ENTER_COMPANY_TYPE,
    ENTER_DOB,
    ENTER_GENDER, ENTER_PASSWORD,
    ENTER_YOUR_EMAIL, ENTER_YOUR_FULL_NAME,
    ENTER_YOUR_PHONE_NUMBER,
    FILE_NOT_FOUND, FILE_PATH,
    INPUT_PLACEHOLDER_MESSAGE, INVALID_CONFIRMATION,
    INVALID_MESSAGE_FOR_USER_CATEGORY,
    MAIN_MENU_TEXT, NO_USER_FOUND,
    PREVIEW_ENTRIES, REGISTRATION_SUCCESS_PROMPT,
    SELECT_OPTION_1_TO_2, USER_DETAILS_HEADERS,
    USER_DICT_COMPANY_NAME, USER_DICT_COMPANY_SERVICE,
    USER_DICT_COMPANY_TYPE, USER_DICT_DOB,
    USER_DICT_EMAIL, USER_DICT_GENDER,
    USER_DICT_IS_DELETE, USER_DICT_NAME,
    USER_DICT_PHONE_NUMBER, USER_DICT_USER_CATEGORY, USER_DICT_USER_PASSWORD,
    VALID_PASSWORD_PROMPT, VENDOR_CATEGORY_NAME,
    YES, NO, INVALID_CHOICE_OF_MAIN, USER_DETAILS_COUNT, INVALID_ENTRIES, UNAUTHORIZED_USER,
    INVALID_CREDENTIAL_MESSAGE, UNEXPECTED_ERROR, CUSTOMER_MENU, ENTER_YOUR_CHOICE, WAREHOUSE_MANAGEMENT,
    VENDOR_P2P_MANAGEMENT, VENDOR_MENU, ENTER_USER_EMAIL, ANONYMOUS_CATEGORY, ENTER_YOUR_WAREHOUSE_ID, ITEM_NAME,
    LOOP_LIMIT, ITEM_NAME_PROMPT, ITEM_QUANTITY, INVALID_ITEM_QUANTITY, ITEM_STATUS_AVAILABLE, ITEM_STATUS,
    CRITICAL_LEVEL_PROMPT, ITEM_CRITICAL_LEVEL, INVALID_CRITICAL_LEVEL,
    ITEM_NUMBER_PROMPT, QUANTITY_TO_BE_CHANGES, USER_DICT_USER_ID, INVALID_DELTA, ITEM_UPDATED,
    WAREHOUSE_ITEM_ZERO_LOGGER, BAD_REQUEST_CODE, OK_STATUS, UN_PROCESSABLE_ENTITY, NOT_FOUND_CODE,
    VENDOR_ID, STATUS, STATUS_SENT, ENTER_ITEMS, DONE, QUANTITY_NOT_ZERO,
    FORM_ITEMS, ENTER_DELIVERY_DATE, DELIVERY_DATE, PAST_DELIVERY_DATE, ADDRESS, ENTER_DELIVERY_ADDRESS, VENDOR_EMAIL,
    ENTER_VENDOR_MAIL_ID, NO_ACTIVE_QUOTATION, YOUR_ACTIVE_QUOTATIONS, SELECT_ONE_QUOTATION, CUSTOMER_QUOTATION_NUMBER,
    ENTER_TOTAL_PRICE, TOTAL_PRICE, VALID_TOTAL_PRICE_ERROR, ENTER_CUSTOMER_QUOTATION_ID, ENTER_VENDOR_QUOTATION_ID,
    CUSTOMER_ID, VENDOR_QUOTATION_ID, CUSTOMER_QUOTATION_ID, STATUS_INACTIVE, PO_STATUS, ENTER_PAYMENT_METHOD,
    VALID_PAYMENT_METHODS, PAYMENT_METHOD, INVALID_PAYMENT_METHOD, ENTER_PO_NUMBER, STATUS_PROCESSING,
    CUSTOMER_QUOTATION_EDIT, PURCHASE_ORDER_EDIT, VENDOR_QUOTATION_NOT_FOUND,
    STATUS_VIEWED, VENDOR_QUOTATION_HEADERS, DATE, CUSTOMER_QUOTATION_ITEM_HEADERS, PO_STATUS_UPDATE_PROMPT,
    PO_STATUS_ITEM_SHIPPED, PO_STATUS_CANCELLED, PO_STATUS_PROCESSING, PO_STATUS_OUT_FOR_DELIVERY, PO_STATUS_DELIVERED,
)
from controller.customer import (
    view_warehouse, add_item_to_warehouse, delete_item_from_warehouse, update_quantity, \
    request_quotation, View_vendor_quotation, edit_quotation,
    edit_purchase_order, view_all_vendor_quotations,
    update_material_quantities)
from controller.procure_to_payment import issue_purchase_order, get_purchase_order_by_po_number
from controller.vendor import view_purchase_order, view_active_quotation_request, issue_quotation, edit_po_status, \
    get_purchase_order, get_active_quotations, print_active_customer_quotations, get_quotation_by_id
from resources.config import logger
from service.customer import create_ware_house, get_vendor_quotation_by_id
from controller.user import (
    get_users,
    load,
    login_user,
    delete
)
from service.user import get_by_email
from service.vendor import get_quotation, update_customer_quotation
from utils.common_utils import get_valid_payment_method, get_valid_email, get_valid_phone_number, \
    get_valid_delivery_date
from utils.user_input_validation import is_valid_number, is_valid_future_date


def start_application():
    """
    Starts the main application loop, displaying the main menu and handling user input.
    """
    while True:
        print(MAIN_MENU_TEXT)
        choice = 0
        try:
            choice = int(input(INPUT_PLACEHOLDER_MESSAGE))
        except ValueError as e:
            print(INVALID_CHOICE_OF_MAIN)
            continue

        match choice:
            case 1:
                register()
            case 2:
                login()
            case 3:
                get_all_users()
            case 4:
                delete_user()
            case 5:
                print(END_GREETING_MESSAGE)
                return
            case _:
                print(INVALID_CHOICE_OF_MAIN)
                continue


def get_user_details(category):
    """
    This function is used to get the user details form the user

    Parameters:
        category (str) : Category given by the user.

    Returns:
        user_details (dict) : Dictionary that contains user details given my the user.
    """
    user_details = {
        USER_DICT_NAME: input(ENTER_YOUR_FULL_NAME).strip(),
        USER_DICT_PHONE_NUMBER: input(ENTER_YOUR_PHONE_NUMBER).strip(),
        USER_DICT_EMAIL: input(ENTER_YOUR_EMAIL).strip(),
        USER_DICT_GENDER: input(ENTER_GENDER).strip(),
        USER_DICT_DOB: input(ENTER_DOB).strip(),
        USER_DICT_COMPANY_NAME: input(ENTER_COMPANY_NAME).strip(),
        USER_DICT_COMPANY_TYPE: input(ENTER_COMPANY_TYPE).strip(),
        USER_DICT_COMPANY_SERVICE: input(USER_DICT_COMPANY_SERVICE).strip(),
        USER_DICT_USER_PASSWORD: input(VALID_PASSWORD_PROMPT).strip(),
        USER_DICT_USER_CATEGORY: category, USER_DICT_IS_DELETE: False}
    return user_details


def register():
    """
    Registers a new user (CUSTOMER or VENDOR) by collecting their details and confirming.
    Validations for input fields are done.
    For more in formation on input validation see :class:`user_input_validation`
    in the module mod:`utils`
    """
    while True:
        print(CUSTOMER_VENDOR_CHOICE)
        choice = ""
        category = ANONYMOUS_CATEGORY
        try:
            choice = int(input(SELECT_OPTION_1_TO_2))
        except ValueError as e:
            print(INVALID_MESSAGE_FOR_USER_CATEGORY)
            continue

        match choice:
            case 1:
                category = CUSTOMER_CATEGORY_NAME
                break
            case 2:
                category = VENDOR_CATEGORY_NAME
                break
            case 3:
                return
            case _:
                print(INVALID_MESSAGE_FOR_USER_CATEGORY)
                continue

    customer_details = get_user_details(category)
    print(PREVIEW_ENTRIES)

    for key, value in customer_details.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    flag = True
    while True:
        confirm = input(CONFORMATION_PROMPT).strip().lower()
        if confirm in [YES, NO]:
            if confirm == YES:
                result = load(customer_details, False)
                if len(result) < USER_DETAILS_COUNT:
                    print(INVALID_ENTRIES)
                    print(result)
                    flag = False
                break
            else:
                result = load(get_user_details(category), False)
                if len(result) < USER_DETAILS_COUNT:
                    print(INVALID_ENTRIES)
                    print(result)
                    flag = False
                break
        else:
            print(INVALID_CONFIRMATION)
            continue

    if flag:  # todo naming
        print(REGISTRATION_SUCCESS_PROMPT)


def login():
    """
    Handles user login by collecting login credentials and authenticating the user.
    """
    login_credential = {
        USER_DICT_EMAIL: input(ENTER_USER_EMAIL).strip(),
        USER_DICT_USER_PASSWORD: input(ENTER_PASSWORD).strip()
    }
    if login_credential[USER_DICT_EMAIL] is None or login_credential[USER_DICT_USER_PASSWORD] is None:
        print(INVALID_CREDENTIAL_MESSAGE)
        return
    user = login_user(login_credential)
    if user is None:
        print(INVALID_CREDENTIAL_MESSAGE)
    elif user[USER_DICT_USER_CATEGORY] == CUSTOMER_CATEGORY_NAME:
        customer_menu(user)
    elif user[USER_DICT_USER_CATEGORY] == VENDOR_CATEGORY_NAME:
        vendor_management(user)
    else:
        logger.error(UNAUTHORIZED_USER)
        print(UNEXPECTED_ERROR)


def get_all_users():
    """
       Retrieves all users and displays their data.

       This function fetches all user records by calling the `get_users` function
       and then displays the user data using the `display_user_data` function.
    """
    users = get_users()
    display_user_data(users)


def delete_user():
    user_id = input(ENTER_USER_EMAIL)
    if delete(user_id):
        print(f"User {user_id} deleted successfully")
    else:
        print(f"User id {user_id} is not found in database")


def display_user_data(data):
    """
    Displays user data in a tabular format.

    Parameters:
        data (dict): A dictionary containing user information with the user ID as the key.
    """
    table_data = []
    for user_id, user_info in data.items():
        row = [
            user_id,
            user_info.get(USER_DICT_NAME, ''),
            user_info.get(USER_DICT_PHONE_NUMBER, ''),
            user_info.get(USER_DICT_EMAIL, ''),
            user_info.get(USER_DICT_GENDER, ''),
            user_info.get(USER_DICT_DOB, ''),
            user_info.get(USER_DICT_COMPANY_NAME, ''),
            user_info.get(USER_DICT_COMPANY_TYPE, ''),
            user_info.get(USER_DICT_COMPANY_SERVICE, ''),
            user_info.get(USER_DICT_USER_CATEGORY, ''),
            user_info.get(USER_DICT_IS_DELETE, ''),
        ]
        table_data.append(row)

    print(tabulate(table_data, USER_DETAILS_HEADERS, tablefmt="grid"))


def print_data(user_details, is_header=True):
    """
    Prints the data in tabular formate on to the console
    """
    try:
        headers = list(user_details[next(iter(user_details))].keys())
    except StopIteration:
        logger.error(NO_USER_FOUND)
        return

    print(" | ".join(f"{header.replace('_', ' ').title():<30}" for header in headers))
    print("=" * (len(headers) * 30))

    for user_id, details in user_details.items():
        print(" | ".join(f"{str(details[header]):<30}" for header in headers))


def get_user_from_file():
    """
        Yields user details from a JSON file, one user at a time.

        This function reads user details from a file specified by `FILE_PATH`. It checks if the file exists
        and is readable before attempting to open it. For each line in the file, it tries to parse the line
        as JSON and yields the resulting user details. If there is an error decoding the JSON, it logs the
        error and skips to the next line. If the file does not exist or is not readable, or if any other
        unexpected error occurs, it logs the appropriate error message.

        Yields:
            dict: A dictionary containing user details parsed from the JSON file.
    """
    file_path = FILE_PATH  # todo move this to .env
    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        return
    if not os.access(file_path, os.R_OK):
        logger.error(f"File is not readable: {file_path}")
        return
    try:
        with open(file_path, "r") as file:
            for user_details in file:
                try:
                    user = json.loads(user_details.strip())  #todo
                    yield user
                except json.JSONDecodeError as e:
                    logger.error(f"Error decoding JSON: {e}")
                    continue  # Skip invalid JSON lines
    except FileNotFoundError:
        logger.fatal(FILE_NOT_FOUND)
    except Exception as e:
        logger.fatal(f"An unexpected error occurred: {e}")


def load_users():
    for user in get_user_from_file():
        load(user, True)


def get_item_details():
    item_details = {ITEM_NAME: input(ITEM_NAME_PROMPT)}
    count = LOOP_LIMIT
    while count > 0:
        item_quantity = input(ITEM_QUANTITY)
        if is_valid_number(item_quantity):
            item_details[ITEM_QUANTITY] = int(item_quantity)
            break
        else:
            count -= 1
            print(INVALID_ITEM_QUANTITY)

    item_details[ITEM_STATUS] = ITEM_STATUS_AVAILABLE
    count = LOOP_LIMIT
    while count > 0:
        critical_level = input(CRITICAL_LEVEL_PROMPT)
        if is_valid_number(critical_level) and (0 < int(critical_level) < item_details[ITEM_QUANTITY]):
            item_details[ITEM_CRITICAL_LEVEL] = int(critical_level)
            break
        else:
            count -= 1
            print(INVALID_CRITICAL_LEVEL)

    return item_details


def get_quotation_form():
    """
    Collects and returns the necessary details for a quotation request from the user.

    Returns:
        dict: A dictionary containing user ID, items with quantities, delivery date, and address.
    """
    quotation_form = {}
    while True:
        vendor_mail_id = input(ENTER_VENDOR_MAIL_ID).strip()
        if get_by_email(vendor_mail_id) is None:
            print(f"No such vendor found with mail id {vendor_mail_id}")
        else:
            quotation_form[VENDOR_EMAIL] = vendor_mail_id
            break

    while True:
        user_mail = input(ENTER_YOUR_EMAIL).strip()
        user = get_by_email(user_mail)
        if user is None:
            print(f"No such user mail {user_mail} is present in database ")
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
            print(PAST_DELIVERY_DATE)

    quotation_form[ADDRESS] = input(ENTER_DELIVERY_ADDRESS).strip()
    return quotation_form


def generate_vendor_quotation(user):
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
    vendor_email = user[USER_DICT_EMAIL]
    active_quotations = get_active_quotations(vendor_email)
    if active_quotations is None:
        print(NO_ACTIVE_QUOTATION)
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
                quotation[STATUS] = STATUS_VIEWED

                flag = 1
                break
        if flag == 0:
            logger.error(f"No such active quotation with id {quotation_id} is found")
        else:
            break

    vendor_details = get_by_email(vendor_email)
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
                print(f"User gave invalid input for unit price of {item}")

    while True:
        total_price = input(ENTER_TOTAL_PRICE)
        if is_valid_number(total_price):
            vendor_quotation[TOTAL_PRICE] = total_price
            break
        else:
            logger.error(VALID_TOTAL_PRICE_ERROR)

    vendor_quotation["date"] = datetime.date.today()
    vendor_quotation[VENDOR_EMAIL] = vendor_email
    vendor_quotation[STATUS] = STATUS_SENT
    return vendor_quotation


def generate_purchase_order(user):
    """
    This function is used to generate a purchase order to specified vendor
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
    return purchase_order


def get_edited_purchase_order(edited_purchase_order):
    count = LOOP_LIMIT
    while count > 0:
        print(PURCHASE_ORDER_EDIT)
        choice = ""
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            count -= 1
            print(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                edited_purchase_order[ADDRESS] = input(ENTER_DELIVERY_ADDRESS)
            case 2:
                print(f"you changed the status changed to inactive")
                edited_purchase_order[STATUS] = STATUS_INACTIVE
            case 3:
                edited_purchase_order[PAYMENT_METHOD] = get_valid_payment_method()
            case 4:
                return edited_purchase_order
            case _:
                count -= 1
                print(INVALID_ENTRIES)


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
    print(f"Created an empty warehouse for you with warehouse id {warehouse_id}")
    choice = ""
    count = LOOP_LIMIT
    while count > 0:
        print(WAREHOUSE_MANAGEMENT)
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            count -= 1
            print(f"Invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
                warehouse = view_warehouse(warehouse_id)
                if warehouse is None:
                    print(f"No such warehouse exists with id {warehouse_id}")
                else:
                    display_data_in_table(warehouse)
            case 2:
                warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
                item_details = get_item_details()
                add_item_to_warehouse(warehouse_id, item_details, user[USER_DICT_USER_ID])
            case 3:
                warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
                item_number = input(ITEM_NUMBER_PROMPT)
                delete_item_from_warehouse(warehouse_id, item_number, user[USER_DICT_USER_ID])
            case 4:
                warehouse_id = input(ENTER_YOUR_WAREHOUSE_ID)
                item_number = input(ITEM_NUMBER_PROMPT)
                delta = input(QUANTITY_TO_BE_CHANGES)
                status_code = update_quantity(warehouse_id, item_number, delta, user[USER_DICT_USER_ID])
                if status_code == BAD_REQUEST_CODE:
                    print(INVALID_DELTA)
                elif status_code == OK_STATUS:
                    print(ITEM_UPDATED)
                elif status_code == NOT_FOUND_CODE:
                    print(f"No such warehouse with the given id {warehouse_id} is present ")
                elif status_code == UN_PROCESSABLE_ENTITY:
                    print(WAREHOUSE_ITEM_ZERO_LOGGER)
            case 5:
                warehouse_id = create_ware_house()
                logger.info(f"Created an empty warehouse for user with warehouse id {warehouse_id}")
            case 6:
                return
            case _:
                count -= 1
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 5")


def get_edited_quotation(edited_quotation):
    count = LOOP_LIMIT
    while count > 0:
        print(CUSTOMER_QUOTATION_EDIT)
        choice = ""
        try:
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            count -= 1
            print(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                edited_quotation[USER_DICT_EMAIL] = get_valid_email()
            case 2:
                edited_quotation[USER_DICT_PHONE_NUMBER] = get_valid_phone_number()
            case 3:
                print(f"You changed the status changed to inactive")
                edited_quotation[STATUS] = STATUS_INACTIVE
            case 4:
                edited_quotation[DELIVERY_DATE] = get_valid_delivery_date()
            case 5:
                edited_quotation[ADDRESS] = input(ENTER_DELIVERY_ADDRESS)
            case 6:
                edited_quotation[FORM_ITEMS] = update_material_quantities(edited_quotation[FORM_ITEMS])
            case 7:
                return edited_quotation
            case _:
                count -= 1
                print(INVALID_ENTRIES)


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
                request_quotation(get_quotation_form())
            case 2:
                customer_quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
                vendor_quotation = View_vendor_quotation(customer_quotation_id)
                if vendor_quotation is None:
                    print(f"No such vendor quotation is available for customer quotation {customer_quotation_id}")
                else:
                    print_vendor_quotations(vendor_quotation)
            case 3:
                purchase_order = generate_purchase_order(user)
                po_number = issue_purchase_order(purchase_order)
                print(f"Purchase order was successfully issued by customer {user[USER_DICT_USER_ID]}")
                print(f"Your purchase order number is {po_number}")
            case 4:
                purchase_order_number = input(ENTER_PO_NUMBER)
                purchase_order = view_purchase_order(user, purchase_order_number)
                if purchase_order is None:
                    print(f"No purchase order available for this purchase order number {purchase_order_number}")
                else:
                    print(purchase_order)
            case 5:
                quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
                edited_quotation = get_quotation(quotation_id)
                if edited_quotation is None:
                    print(f"No such quotation id {quotation_id} found in the database")
                    return
                elif edited_quotation[STATUS] != STATUS_SENT:
                    if edited_quotation[STATUS] == STATUS_PROCESSING:
                        print(
                            f"You {user[USER_DICT_USER_ID]} attempt to edit the quotation that is already viewed by "
                            f"the customer")
                        return
                    else:
                        print(f"User {user[USER_DICT_USER_ID]} attempts to edit the quotation that is Inactive")
                        return

                edited_quotation = get_edited_quotation(edited_quotation)
                edit_quotation(quotation_id, edited_quotation)
            case 6:
                purchase_order_number = input(ENTER_PO_NUMBER)
                edited_purchase_order = get_purchase_order_by_po_number(purchase_order_number, user[USER_DICT_USER_ID])
                if edited_purchase_order is None:
                    logger.error(f"No such purchase order number present in db {purchase_order_number}")
                    return
                elif edited_purchase_order[STATUS] != STATUS_SENT:
                    if edited_purchase_order[STATUS] == STATUS_PROCESSING:
                        logger.error(
                            f"User {user[USER_DICT_USER_ID]} attempts to edit the purchase order that is already "
                            f"viewed by"
                            f"the customer")
                        return
                    else:
                        logger.error(
                            f"User {user[USER_DICT_USER_ID]} attempts to edit the purchase order that is Inactive")
                        return

                edited_purchase_order = get_edited_purchase_order(edited_purchase_order)
                edit_purchase_order(user, edited_purchase_order)
            case 7:
                customer_quotation_id = input(ENTER_CUSTOMER_QUOTATION_ID)
                vendor_quotation = view_all_vendor_quotations(customer_quotation_id)
                if vendor_quotation is None:
                    print(VENDOR_QUOTATION_NOT_FOUND)
                else:
                    print(vendor_quotation)
            case 8:
                return
            case _:
                print(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 6   ")


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
            choice = int(input(ENTER_YOUR_CHOICE))
        except ValueError as e:
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        match choice:
            case 1:
                view_active_quotation_request(user)
            case 2:
                vendor_quotation = generate_vendor_quotation(user)
                issue_quotation(vendor_quotation)
            case 3:
                purchase_order_id = input(ENTER_PO_NUMBER)
                po_status = get_po_status()
                edit_po_status(user, purchase_order_id, po_status)
            case 4:
                get_purchase_order(user)
            case 5:
                return
            case _:
                logger.error(f"User gave invalid input {choice}, Must be only numbers ranging from 1 to 5")


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
            details.get(DATE, '').strftime('%d/%m/%Y') if isinstance(details.get('date'),
                                                                     datetime.date) else details.get('date', ''),
            details.get(VENDOR_ID, ''),
            details.get(STATUS, '')
        ]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt='grid'))


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


def get_po_status():
    choice = ""
    count = LOOP_LIMIT
    while count > 0:
        print(PO_STATUS_UPDATE_PROMPT)
        try:
            choice = int(input("Enter your choice"))
        except ValueError as e:
            count -= 1
            logger.exception(f"User gave a invalid choice {choice}, Must give only numbers")
            continue

        if choice == 1:
            return PO_STATUS_ITEM_SHIPPED
        elif choice == 2:
            return PO_STATUS_CANCELLED
        elif choice == 3:
            return PO_STATUS_PROCESSING
        elif choice == 4:
            return PO_STATUS_OUT_FOR_DELIVERY
        elif choice == 5:
            return PO_STATUS_DELIVERED
        else:
            count -= 1
            print(INVALID_ENTRIES)


if __name__ == "__main__":
    load_users()
    start_application()
