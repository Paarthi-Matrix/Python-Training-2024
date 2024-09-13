from exception.custom_exception import InvalidCredentialException

from helper.constant import (
    DICT_EMAIL, DICT_MOBILE, DICT_NAME, DICT_PASSWORD,
    ERROR_INVALID_AREA, ERROR_INVALID_EMAIL, ERROR_INVALID_MOBILE,
    ERROR_INVALID_NAME, ERROR_INVALID_PASSWORD
)

from resources.logger_configuration import logger

from service.admin import register_admin, read_admins, is_admin_valid, is_admin_registered

from service.customer import (
    get_all_customer, is_customer_present, remove_customer,
    search_customer, update_customer, view_all_complaints
)

from service.driver import (
    check_wastage, get_all_work_reports, register_driver, search_driver
)

from service.recycler import (
    calculate_profit, get_cost_of_garbage, register_recycler
)
from util.common_util import hash_password

from validator.validation import (
    check_valid_input, is_valid_email, is_valid_mobile,
    is_valid_name, is_valid_password
)


def find_customer(customer_identifier):
    """
    Finds and returns a customer based on the provided identifier.

    Args:
        customer_identifier (str): The unique identifier for the customer.

    Returns:
        dict: Details of the customer found using the identifier.
    """
    return search_customer(customer_identifier)


def find_all_customer():
    """
    Retrieves and returns a list of all customers.

    Returns:
        list: A list of all customer details.
    """
    return get_all_customer()


def delete_customer(customer_id):
    """
    Deletes a customer based on the provided customer ID.

    Args:
        customer_id (str): The unique identifier of the customer to be deleted.

    Returns:
        bool: True if the customer was successfully deleted, otherwise False.
    """
    if remove_customer(customer_id) is None:
        return True


def add_admin_detail(name, email, password, mobile):
    """
    Validates and registers a new admin with the provided details.

    Args:
        name (str): The name of the admin.
        email (str): The email address of the admin.
        password (str): The password for the admin account.

    Returns:
        dict or bool: A dictionary of validation errors if any; otherwise, the result of the registration.
    """
    result = {}
    if not check_valid_input(name, is_valid_name):
        result[name] = ERROR_INVALID_NAME
    if not check_valid_input(email, is_valid_email):
        result[email] = ERROR_INVALID_EMAIL
    if not check_valid_input(password, is_valid_password):
        result[password] = ERROR_INVALID_PASSWORD
    if not check_valid_input(mobile, is_valid_mobile):
        result[mobile] = ERROR_INVALID_MOBILE

    if len(result) == 0:
        return register_admin(name, email, hash_password(password), mobile)
    return result


def add_driver(name, email, password, mobile_no, area):
    """
    Validates and registers a new driver with the provided details.

    Args:
        name (str): The name of the driver.
        email (str): The email address of the driver.
        password (str): The password for the driver account.
        mobile_no (str): The mobile number of the driver.
        area (str): The area where the driver operates.

    Returns:
        dict or bool: A dictionary of validation errors if any; otherwise, the result of the registration.
    """
    result = {}
    if not check_valid_input(name, is_valid_name):
        result[name] = ERROR_INVALID_NAME
    if not check_valid_input(email, is_valid_email):
        result[email] = ERROR_INVALID_EMAIL
    if not check_valid_input(password, is_valid_password):
        result[password] = ERROR_INVALID_PASSWORD
    if not check_valid_input(mobile_no, is_valid_mobile):
        result[mobile_no] = ERROR_INVALID_PASSWORD
    if not check_valid_input(area, is_valid_name):
        result[area] = ERROR_INVALID_AREA

    if len(result) == 0:
        return register_driver(name, email, hash_password(password), mobile_no, area)
    return result


def check_customer_present(customer_id):
    """
    Checks if a customer with the given ID is present in the system.

    Args:
        customer_id (str): The unique identifier of the customer.

    Returns:
        bool: True if the customer is present, otherwise False.
    """
    return is_customer_present(customer_id)


def update_customer_detail(customer_id, customer_identifier, to_update):
    """
    Updates a specific detail of a customer based on the provided parameters.

    Args:
        customer_id (str): The unique identifier of the customer to be updated.
        customer_identifier (str): The new value for the detail being updated.
        to_update (str): The specific detail to update (e.g., name, email, password, mobile).

    Returns:
        bool: True if the update was successful.

    Raises:
        InvalidCredentialException: If the provided detail is invalid.
    """
    if to_update == DICT_NAME:
        if check_valid_input(customer_identifier, is_valid_name):
            return update_customer(customer_id, customer_identifier, to_update)
        else:
            logger.warning(ERROR_INVALID_NAME)
            raise InvalidCredentialException(ERROR_INVALID_NAME)
    elif to_update == DICT_EMAIL:
        if check_valid_input(customer_identifier, is_valid_email):
            return update_customer(customer_id, customer_identifier, to_update)
        else:
            logger.warning(ERROR_INVALID_EMAIL)
            raise InvalidCredentialException(ERROR_INVALID_EMAIL)
    elif to_update == DICT_PASSWORD:
        if check_valid_input(customer_identifier, is_valid_password):
            return update_customer(customer_id, customer_identifier, to_update)
        else:
            logger.warning(ERROR_INVALID_PASSWORD)
            raise InvalidCredentialException(ERROR_INVALID_PASSWORD)
    elif to_update == DICT_MOBILE:
        if check_valid_input(customer_identifier, is_valid_mobile):
            return update_customer(customer_id, customer_identifier, to_update)
        else:
            logger.warning(ERROR_INVALID_MOBILE)
            raise InvalidCredentialException(ERROR_INVALID_MOBILE)


def find_driver(area):
    """
    Finds and returns a driver based on the provided area.

    Args:
        area (str): The area where the driver operates.

    Returns:
        dict: Details of the driver found in the specified area.
    """
    return search_driver(area)


def fetch_all_work_reports():
    """
    Retrieves and returns all work reports.

    Returns:
        list: A list of all work reports.
    """
    return get_all_work_reports()


def get_all_complaints():
    """
    Retrieves and returns all customer complaints.

    Returns:
        list: A list of all complaints.
    """
    return view_all_complaints()


def add_recycler(recycler_name, recycler_email, password, mobile_no):
    """
    Validates and registers a new recycler with the provided details.

    Args:
        recycler_name (str): The name of the recycler.
        recycler_email (str): The email address of the recycler.
        password (str): The password for the recycler account.
        mobile_no (str): The mobile number of the recycler.

    Returns:
        dict or bool: A dictionary of validation errors if any; otherwise, the result of the registration.
    """
    result = {}
    if not check_valid_input(recycler_name, is_valid_name):
        result[recycler_name] = ERROR_INVALID_NAME
    if not check_valid_input(recycler_email, is_valid_email):
        result[recycler_email] = ERROR_INVALID_EMAIL
    if not check_valid_input(password, is_valid_password):
        result[password] = ERROR_INVALID_PASSWORD
    if not check_valid_input(mobile_no, is_valid_mobile):
        result[mobile_no] = ERROR_INVALID_PASSWORD

    if len(result) == 0:
        return register_recycler(recycler_name, recycler_email, password, mobile_no)
    else:
        return result


def report_to_recycler():
    """
    Reports wastage information to the recycler.

    Returns:
        dict: Details of the reported wastage.
    """
    return check_wastage()


def cost_of_wastage_report():
    """
    Retrieves and returns the cost of garbage wastage.

    Returns:
        dict: work reports with cost of garbage
    """
    return get_cost_of_garbage()


def calculate_total_profit():
    """
    Calculates and returns the total profit.

    Returns:
        float: The total calculated profit.
    """
    return calculate_profit()


def load_admins():
    """
    Loads admin data into the `admins` dictionary from the data file.

    This function calls `read_admins()` to populate the global `admins` dictionary
    with data from the file specified by `DATA_FILE`.
    """
    read_admins()


def validate_admin(admin_email, admin_password):
    """
    Validates the admin's email and password.

    Args:
        admin_email (str): The admin's email address.
        admin_password (str): The admin's password.

    Returns:
        bool: True if the email and password are valid; False otherwise.
    """
    return is_admin_valid(admin_email, admin_password)


def is_admin_already_registered():
    """
    Checks if an admin is already registered.

    Returns:
        bool: True if an admin is registered; False otherwise.
    """
    return is_admin_registered()

