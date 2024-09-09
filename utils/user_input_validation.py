import re
from datetime import date, datetime

from constants.biznex_constants import (
    DOB_VALIDATION_REGEX,
    EMAIL_VALIDATION_REGEX,
    GENDER_CATEGORY,
    INVALID_DATE_FORMATE,
    NAME_VALIDATION_REGEX,
    NUMBER_REGEX,
    PASSWORD_VALIDATION_REGEX,
    PHONE_NUMBER_VALIDATION_REGEX
)
from resources.logging_config import logger


def is_valid_number(number):
    return bool(re.match(NUMBER_REGEX, number))


def user_name_validation(name):
    """
    Validates the user's name. Name should only contain alphabets and spaces,
    and be between 2 and 50 characters long

    Parameters:
        name (str): The name of the user.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    return bool(re.match(NAME_VALIDATION_REGEX, name))


def phone_number_validation(phone_number):
    """
    Validates the user's phone number.
    Phone number should be 10 digits long

    Parameters:
        phone_number (str): The phone number of the user.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """

    return bool(re.match(PHONE_NUMBER_VALIDATION_REGEX, phone_number))


def email_validation(email):
    """
    Validates the user's email address.
    This function gives basic email pattern validation.

    Parameters:
        email (str): The email address of the user.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    return bool(re.match(EMAIL_VALIDATION_REGEX, email))


def gender_validation(gender):
    """
    Validates the user's gender input.
    Acceptable values are Male, Female, Others
    Parameters:
        gender (str): The gender of the user.

    Returns:
        bool: True if the gender is valid, False otherwise.
    """
    return gender.strip().lower() in GENDER_CATEGORY


def date_of_birth_validation(dob):
    """
    Validates the user's date of birth.
    Date format should be DD/MM/YYYY
    Parameters:
        dob (str): The date of birth of the user in DD/MM/YYYY format.

    Returns:
        bool: True if the date of birth is valid, False otherwise.
    """

    return bool(re.match(DOB_VALIDATION_REGEX, dob))


def password_validation(password):
    """
    Validates the user's password.
    The password should be at least 8 characters long and contain special characters

    Parameters:
        password (str): The password entered by the user.

    Returns:
        bool: True if the password is valid, False otherwise.
    """

    return bool(re.match(PASSWORD_VALIDATION_REGEX, password))


def is_valid_future_date(date_str):
    """
    Validates if the given date string is in the correct format and is not in the past.

    Parameters:
        date_str (str): The date string to validate, expected in "YYYY-MM-DD" format.

    Returns:
        bool: True if the date is valid and not in the past, False otherwise.
    """
    try:
        input_date = datetime.strptime(date_str, "%d/%m/%Y").date()

        if input_date >= date.today():
            return True
        else:
            return False
    except ValueError:
        logger.error(INVALID_DATE_FORMATE)
        return False
