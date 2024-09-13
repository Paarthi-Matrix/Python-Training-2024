import json
import os

from helper.constant import LOG_ADMIN_CREATED, DATA_FILE, PASSWORD
from resources.logger_configuration import logger
from util.common_util import check_password

admins = {}


def save_admins():
    """
    Saves the current state of the `admins` dictionary to a JSON file.

    The file is written to the location specified by `DATA_FILE`. The JSON data
    is formatted with an indentation level of 4 spaces to enhance readability.

    This function does not return any value. It simply persists the `admins`
    dictionary to the specified file.
    """
    with open(DATA_FILE, 'w') as file:
        json.dump(admins, file, indent=4)


def register_admin(name, email, encoded_password, mobile):
    """
    Registers a new admin with the provided details.

    Args:
        name (str): The name of the admin.
        email (str): The email address of the admin. This serves as the unique
                     identifier for the admin in the `admins` dictionary.
        encoded_password (str): The encoded password for the admin's account.
        mobile (str): The mobile number of the admin.

    Returns:
        bool: True if the registration was successful.
    """
    admins[email] = {
        'name': name,
        'password': encoded_password,
        'mobile': mobile
    }
    save_admins()
    logger.info(LOG_ADMIN_CREATED)
    return True


def read_admins():
    """
    Loads admin data from the JSON file into the `admins` dictionary.

    This function reads from the file specified by `DATA_FILE`. If the file
    exists and contains valid JSON data, the data is loaded into the global
    `admins` dictionary. If the file is empty or contains invalid JSON, the
    `admins` dictionary is initialized as an empty dictionary.

    Raises:
        JSONDecodeError: If the file contains invalid JSON, an error message
                         will be printed, and `admins` will be initialized
                         as an empty dictionary.
    """
    global admins
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                content = file.read().strip()  # Read and strip whitespace
                if content:  # Check if the content is empty
                    admins = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")


def is_admin_registered():
    """Checks if at least one admin is registered.

    Returns:
        bool: True if more than one admin detail is present; False otherwise."""
    if len(admins) == 1:
        return True
    return False


def is_admin_valid(admin_email, admin_password):
    """
    Checks if the provided email and password are valid for an admin.

    Args:
        admin_email (str): The admin's email address.
        admin_password (str): The admin's password.

    Returns:
        bool: True if the email exists and the password matches; False otherwise.
    """
    if admin_email in admins:
        return check_password(admins[admin_email][PASSWORD], admin_password)
    return False
