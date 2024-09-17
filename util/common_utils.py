import random
import string

from constant.constant import ENTER_YOUR_EMAIL, ENTER_PHONE_NUMBER, ENTER_DELIVERY_DATE, ENTER_PAYMENT_METHOD, \
    VALID_PAYMENT_METHODS, INVALID_PAYMENT_METHOD
from resources.config import logger
from util.user_input_validation import email_validation, phone_number_validation, is_valid_future_date


def generate_random_string(length=8):
    """
    Generates a random string of the specified length consisting of uppercase letters and digits.

    Parameters:
        length (int): The length of the random string to generate (default is 8).

    Returns:
        str: A random string of the specified length.
    """
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


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
    """
    This method gets, checks and returns the valid payment methods.
    The valid payment methods are bank transfer, credit card, cheque

    Returns:
        payment_method (str) : Valid payment methods given by the user
    """
    while True:
        payment_method = input(ENTER_PAYMENT_METHOD).strip().lower()
        if payment_method in VALID_PAYMENT_METHODS:
            print(f"Payment method accepted: {payment_method}")
            return payment_method
        else:
            logger.error(INVALID_PAYMENT_METHOD)