import re
from constant.logger_constant import (
    LOG_ERROR_INVALID_NAME,
    LOG_ERROR_INVALID_EMAIL,
    LOG_ERROR_INVALID_PASSWORD,
    LOG_ERROR_INVALID_MOBILE,
    LOG_ERROR_INVALID_AREA,LOG_ERROR_INVALID_LOCALITY,
    LOG_ERROR_INVALID_LANDMARK,
    LOG_ERROR_INVALID_CITY,
    LOG_ERROR_INVALID_LOAD, LOG_ERROR_INVALID_CYCLE_PERIOD,
    LOG_ERROR_INVALID_WASTAGE,
    LOG_ERROR_INVALID_DOOR_NO,
)

from constant.prompt_constant import (
    PROMPT_CUSTOMER_NAME,
    PROMPT_ADMIN_NAME,
    PROMPT_EMAIL,
    PROMPT_PASSWORD,
    PROMPT_MOBILE,
    PROMPT_DRIVER_AREA,
    PROMPT_DRIVER_NAME,
    PROMPT_CUSTOMER_AREA,
    PROMPT_CUSTOMER_LOCALITY,
    PROMPT_CUSTOMER_LANDMARK,
    PROMPT_CUSTOMER_CITY,
    PROMPT_CUSTOMER_CYCLE_PERIOD,
    PROMPT_CUSTOMER_WASTAGE_TYPE,
    PROMPT_CUSTOMER_LOAD,
    PROMPT_CUSTOMER_DOOR_NO, PROMPT_RECYCLER_NAME,
)

from resources.logger_configuration import logger

from service.customer_service import (
    is_address_already_available
)

from service.driver_service import (
    get_driver_email
)

from util.common_util import hash_password

from constant.regex_constant import REGEX_VALIDATE_STATUS, REGEX_VALIDATE_WASTAGE_TYPE, REGEX_VALIDATE_DOOR_N0, \
    REGEX_VALID_COMPLAINT


def is_valid_name(name):
    return bool(re.match(r'^[A-Za-z ]+$', name))


def is_valid_email(email):
    return bool(re.match(r'^[a-z0-9_.]+@(ideas2it|gmail|yahoo)\.com$', email))


def is_valid_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\s]{8,}$', password))


def is_valid_mobile(mobile):
    return bool(re.match(r'^[6-9]\d{9}$', mobile))


def is_valid_load(load):
    if re.match(r'^(low|Heavy)$', load, re.IGNORECASE):
        return True
    return False


def is_valid_cycle_period(cycle_period):
    if re.match(r'^(daily)$', cycle_period, re.IGNORECASE):
        return True
    return False


def is_valid_wastage_type(wastage_type):
    return bool(re.match(REGEX_VALIDATE_WASTAGE_TYPE, wastage_type, re.IGNORECASE))


def is_valid_city(city):
    return bool(re.match(r'^chennai$', city, re.IGNORECASE))


def is_valid_status(status):
    if re.match(REGEX_VALIDATE_STATUS, status, re.IGNORECASE):
        return True
    return False


def is_valid_door_no(door_no):
    if re.match(REGEX_VALIDATE_DOOR_N0, door_no):
        return True
    return False


def is_complaint_valid(complaint):
    if re.match(REGEX_VALID_COMPLAINT, complaint):
        return True
    return False


def get_valid_input(prompt, validation_func, error_message):
    """Helper function to get and validate input."""
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            logger.warning(error_message)
            print()


def collect_customer_details():
    """
    Collects and validates customer details such as name, email, password, mobile number, and account number.

    Prompts the user to input customer details and validates the input using predefined functions.
    Returns the validated customer details.

    Returns:
        tuple: A tuple containing customer_name, customer_email, password, mobile_no, and account_no.
    """
    customer_name = get_valid_input(
        PROMPT_CUSTOMER_NAME,
        is_valid_name,
        LOG_ERROR_INVALID_NAME
    )

    customer_email = get_valid_input(
        PROMPT_EMAIL,
        is_valid_email,
        LOG_ERROR_INVALID_EMAIL
    )

    password = get_valid_input(
        PROMPT_PASSWORD,
        is_valid_password,
        LOG_ERROR_INVALID_PASSWORD
    )
    encoded_password = hash_password(password)
    mobile_no = get_valid_input(
        PROMPT_MOBILE,
        is_valid_mobile,
        LOG_ERROR_INVALID_MOBILE
    )

    return customer_name, customer_email, encoded_password, mobile_no


def collect_bin_details():
    """
    Collects and validates bin details such as area, driver email, locality, landmark, city, load type
    cycle period, wastage type.

    Prompts the user to input customer details and validates the input using predefined functions.
    Returns the validated bin details.

    Returns:
        tuple: A tuple containing area, driver email, locality, landmark, city, load type
               cycle period, wastage type.
    """
    area = get_valid_input(
        PROMPT_CUSTOMER_AREA,
        is_valid_name,
        LOG_ERROR_INVALID_AREA
    )
    driver_email = get_driver_email(area)
    if driver_email:
        door_no = get_valid_input(
            PROMPT_CUSTOMER_DOOR_NO,
            is_valid_door_no,
            LOG_ERROR_INVALID_DOOR_NO
        )
        if not is_address_already_available(door_no, area):
            landmark = get_valid_input(
                PROMPT_CUSTOMER_LANDMARK,
                is_valid_name,
                LOG_ERROR_INVALID_LANDMARK
            )

            city = get_valid_input(
                PROMPT_CUSTOMER_CITY,
                is_valid_city,
                LOG_ERROR_INVALID_CITY
            )

            load_type = get_valid_input(
                PROMPT_CUSTOMER_LOAD,
                is_valid_load,
                LOG_ERROR_INVALID_LOAD
            )

            cycle_period = get_valid_input(
                PROMPT_CUSTOMER_CYCLE_PERIOD,
                is_valid_cycle_period,
                LOG_ERROR_INVALID_CYCLE_PERIOD
            )

            wastage_type = get_valid_input(
                PROMPT_CUSTOMER_WASTAGE_TYPE,
                is_valid_wastage_type,
                LOG_ERROR_INVALID_WASTAGE
            )
            return area, door_no, landmark, city, load_type, cycle_period, wastage_type, driver_email


def collect_admin_details():
    """
    Collects and validates admin details such as name, email, password

    Prompts the user to input admin details and validates the input using predefined functions.
    Returns the validated admin details.

    Returns:
        tuple: A tuple containing name, email, password
    """
    admin_name = get_valid_input(
        PROMPT_ADMIN_NAME,
        is_valid_name,
        LOG_ERROR_INVALID_NAME
    )

    admin_email = get_valid_input(
        PROMPT_EMAIL,
        is_valid_email,
        LOG_ERROR_INVALID_EMAIL
    )

    password = get_valid_input(
        PROMPT_PASSWORD,
        is_valid_password,
        LOG_ERROR_INVALID_PASSWORD
    )
    encoded_password = hash_password(password)
    return admin_name, admin_email, encoded_password


def collect_driver_details():
    """
    Collects and validates driver details such as name, email, password, mobile no, area

    Prompts the user to input driver details and validates the input using predefined functions.
    Returns the validated driver details.

    Returns:
        tuple: A tuple containing name, email, password, mobile no, area
    """
    driver_name = get_valid_input(
        PROMPT_DRIVER_NAME,
        is_valid_name,
        LOG_ERROR_INVALID_NAME
    )

    driver_email = get_valid_input(
        PROMPT_EMAIL,
        is_valid_email,
        LOG_ERROR_INVALID_EMAIL
    )

    password = get_valid_input(
        PROMPT_PASSWORD,
        is_valid_password,
        LOG_ERROR_INVALID_PASSWORD
    )
    encoded_password = hash_password(password)
    mobile_no = get_valid_input(
        PROMPT_MOBILE,
        is_valid_mobile,
        LOG_ERROR_INVALID_MOBILE
    )

    area = input(PROMPT_DRIVER_AREA)

    return driver_name, driver_email, encoded_password, mobile_no, area


def collect_recycler_details():
    recycler_name = get_valid_input(
        PROMPT_RECYCLER_NAME,
        is_valid_name,
        LOG_ERROR_INVALID_NAME
    )

    recycler_email = get_valid_input(
        PROMPT_EMAIL,
        is_valid_email,
        LOG_ERROR_INVALID_EMAIL
    )

    password = get_valid_input(
        PROMPT_PASSWORD,
        is_valid_password,
        LOG_ERROR_INVALID_PASSWORD
    )
    encoded_password = hash_password(password)
    mobile_no = get_valid_input(
        PROMPT_MOBILE,
        is_valid_mobile,
        LOG_ERROR_INVALID_MOBILE
    )
    return recycler_name, recycler_email, encoded_password, mobile_no

