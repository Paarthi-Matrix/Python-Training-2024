import re

from project.constant.constant import (
    EMAIL_REGEX, MOBILE_NUMBER_REGEX,
    NAME_REGEX, PASSWORD_REGEX, LICENSE_REGEX, LOCATION_REGEX
)
from project.config.config import logger


def is_valid_email(email):
    """
    Validates an email address.

    This function checks if the provided email address matches the pattern
    defined by EMAIL_REGEX. It returns True if the email is valid, and False otherwise.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    return re.match(EMAIL_REGEX, email) is not None


def is_valid_mobile(number):
    """
    Validates a mobile phone number.

    This function checks if the provided mobile number matches the pattern
    defined by MOBILE_NUMBER_REGEX. It returns True if the number is valid, and False otherwise.

    Args:
        number (str): The mobile phone number to validate.

    Returns:
        bool: True if the mobile phone number is valid, False otherwise.
    """
    return re.match(MOBILE_NUMBER_REGEX, number) is not None


def is_valid_name(name):
    """
    Validates a name.

    This function checks if the provided name matches the pattern defined by NAME_REGEX.
    It returns True if the name is valid, and False otherwise.

    Args:
        name (str): The name to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    return re.match(NAME_REGEX, name) is not None


def is_valid_password(password):
    """
     Validates a password.

     This function checks if the provided password matches the pattern defined by PASSWORD_REGEX.
     It returns True if the password is valid, and False otherwise.

     Args:
         password (str): The password to validate.

     Returns:
         bool: True if the password is valid, False otherwise.
     """
    return re.match(PASSWORD_REGEX, password) is not None


# ex: TN-01-2000-1234567
def is_valid_license(license_number):
    """
    Validates a license number.

    This function checks if the provided license number matches the pattern defined by LICENSE_REGEX.
    It returns True if the license number is valid, and False otherwise.

    Args:
        license_number (str): The license number to validate.

    Returns:
        bool: True if the license number is valid, False otherwise.
    """
    return re.match(LICENSE_REGEX, license_number) is not None


def is_valid_location(location):
    return re.match(LOCATION_REGEX, location) is not None


def update_entity(entity, to_update, input_prompt, validation_func, success_msg, error_msg, update_func):
    """
    Handles the update process for a given entity.

    Prompts the user for a new value, validates it using the provided
    validation function, and updates the entity with the new value if valid.
    Logs appropriate messages based on the result of the update.

    Args:
        entity: The entity object to be updated.
        to_update: The key or field in the entity to be updated.
        input_prompt: The prompt message to be displayed to the user.
        validation_func: A function to validate the new value.
        success_msg: The message to log upon a successful update.
        error_msg: The message to log if the validation fails.
        update_func: A function that performs the actual update on the entity.
    """
    while True:
        new_value = input(input_prompt)
        if validation_func(new_value):
            if update_func(entity, to_update, new_value.lower()):
                print(success_msg)
            break
        else:
            logger.warning(error_msg)


def input_validation(value, validation_func, error_msg):
    """
    Prompts the user for input and validates it using the provided validation function.

    Args:
        value (str): The value to validate.
        validation_func (function): A function to validate the user input.
        error_msg (str): The error message to log if validation fails.

    Returns:
        str: The validated user input.
    """
    if validation_func(value):
        return value
    else:
        return error_msg


def continue_operations(operation_func):
    choice = input("Do you want to continue ? (yes/no): ").lower()
    if choice == "yes":
        operation_func()
