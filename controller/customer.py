from helper.constant import (
    ERROR_INVALID_AREA, ERROR_INVALID_CYCLE_PERIOD, ERROR_INVALID_CITY,
    ERROR_INVALID_DOOR_NO, ERROR_INVALID_EMAIL, ERROR_INVALID_LANDMARK,
    ERROR_INVALID_LOAD, ERROR_INVALID_NAME, ERROR_INVALID_PASSWORD,
    ERROR_INVALID_WASTAGE, LOG_BIN_ALREADY_CREATED
)

from resources.logger_configuration import logger

from service.customer import (
    create_bin, get_customer_bin, get_customer_details, is_address_already_available,
    is_bin_available, is_bin_created_for_customer, is_customer_present,
    register_customer, raise_complaint
)

from service.driver import (
    check_profit, get_driver_email, is_valid_complaint
)
from util.common_util import hash_password

from validator.validation import (
    check_valid_input, is_complaint_valid, is_valid_city, is_valid_cycle_period,
    is_valid_door_no, is_valid_email, is_valid_load, is_valid_mobile,
    is_valid_name, is_valid_password, is_valid_wastage_type
)


def add_customer(customer_name, customer_email, password, mobile_no):
    """
    Validates and registers a new customer with the provided details.

    Args:
        customer_name (str): The name of the customer.
        customer_email (str): The email address of the customer.
        password (str): The password for the customer account.
        mobile_no (str): The mobile number of the customer.

    Returns:
        dict or bool: A dictionary of validation errors if any; otherwise, the result of the registration.
    """
    result = {}
    if not check_valid_input(customer_name, is_valid_name):
        result[customer_name] = ERROR_INVALID_NAME
    if not check_valid_input(customer_email, is_valid_email):
        result[customer_email] = ERROR_INVALID_EMAIL
    if not check_valid_input(password, is_valid_password):
        result[password] = ERROR_INVALID_PASSWORD
    if not check_valid_input(mobile_no, is_valid_mobile):
        result[mobile_no] = ERROR_INVALID_PASSWORD

    if len(result) == 0:
        return register_customer(customer_name, customer_email, hash_password(password), mobile_no)
    return result


def check_if_customer_present(customer_id):
    """
    Checks if a customer with the given ID is present and if a bin has been created for the customer.

    Args:
        customer_id (str): The unique identifier of the customer.

    Returns:
        bool: True if the customer is present and no bin is created; otherwise, logs an error if a bin is created.
    """
    if is_customer_present(customer_id):
        if not is_bin_created_for_customer(customer_id):
            return True
        else:
            logger.error(LOG_BIN_ALREADY_CREATED.format(customer_id=customer_id))


def is_area_available(area):
    """
    Checks if the given area is available for assignment to a driver.

    Args:
        area (str): The area to check.

    Returns:
        str: The email address of the driver assigned to the area.
    """
    return get_driver_email(area)


def add_bin_detail(area, door_no, landmark, city, load_type,
                   cycle_period, wastage_type, driver_email, customer_id):
    """
    Validates and creates a bin with the provided details.

    Args:
        area (str): The area where the bin will be located.
        door_no (str): The door number of the location.
        landmark (str): The landmark near the location.
        city (str): The city where the bin will be located.
        load_type (str): The type of load for the bin.
        cycle_period (str): The cycle period for the bin.
        wastage_type (str): The type of wastage the bin will handle.
        driver_email (str): The email address of the assigned driver.
        customer_id (str): The unique identifier of the customer.

    Returns:
        dict or bool: A dictionary of validation errors if any; otherwise, the result of bin creation.
    """
    result = {}
    if not check_valid_input(area, is_valid_name):
        result[area] = ERROR_INVALID_AREA
    if not check_valid_input(door_no, is_valid_door_no):
        result[door_no] = ERROR_INVALID_DOOR_NO
    if not check_valid_input(landmark, is_valid_name):
        result[landmark] = ERROR_INVALID_LANDMARK
    if not check_valid_input(city, is_valid_city):
        result[city] = ERROR_INVALID_CITY
    if not check_valid_input(load_type, is_valid_load):
        result[load_type] = ERROR_INVALID_LOAD
    if not check_valid_input(cycle_period, is_valid_cycle_period):
        result[cycle_period] = ERROR_INVALID_CYCLE_PERIOD
    if not check_valid_input(wastage_type, is_valid_wastage_type):
        result[wastage_type] = ERROR_INVALID_WASTAGE

    if len(result) == 0:
        if not is_address_already_available(door_no, area):
            return create_bin(area, door_no, landmark, city, load_type, cycle_period, wastage_type,
                              driver_email, customer_id)
    return result


def check_if_bin_available(bin_id):
    """
    Checks if a bin with the given ID is available and if it has a valid complaint.

    Args:
        bin_id (str): The unique identifier of the bin.

    Returns:
        bool: True if the bin is available and has a valid complaint; otherwise, False.
    """
    if is_bin_available(bin_id):
        if is_valid_complaint(bin_id):
            return True


def validate_complaint(bin_id, complaint):
    """
    Validates and raises a complaint for the specified bin.

    Args:
        bin_id (str): The unique identifier of the bin.
        complaint (str): The complaint to be raised.

    Returns:
        bool: True if the complaint is valid and raised successfully; otherwise, False.
    """
    if check_valid_input(complaint, is_complaint_valid):
        return raise_complaint(bin_id, complaint)
    return False


def check_if_profit_credited(bin_id):
    """
    Checks if profit has been credited for the specified bin.

    Args:
        bin_id (str): The unique identifier of the bin.
    """
    if is_bin_available(bin_id):
        return check_profit(bin_id)


def fetch_customer_detail(email):
    """
    Fetches and returns the details of a customer based on their email address.

    Args:
        email (str): The email address of the customer.

    Returns:
        dict: The details of the customer associated with the email address.
    """
    return get_customer_details(email)


def get_bin_detail(customer_id):
    """
    Retrieves the bin details for a customer based on their ID.

    Args:
        customer_id (str): The unique identifier of the customer.

    Returns:
        dict: The details of the bin assigned to the customer if the customer is present.
    """
    if is_customer_present(customer_id):
        return get_customer_bin(customer_id)
