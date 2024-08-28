from resources.logging_config import logger
from service.user_service import add_user, check_credential, get_users, remove_user, get_by_user_attribute
from constants.biznex_constants import (
    INVALID_CREDENTIAL_MESSAGE,
    USER_DICT_USER_ID,
    USER_DICT_USER_PASSWORD)


def register_user(user):
    """
    Registers a new user and logs the success message.

    Parameters:
        user (dict): Dictionary containing user details to be registered.
    """
    user = add_user(user)
    logger.info(f"User {user['name']} created successfully. The user ID is {user['user_id']}.")
    return


def login_user(login_credential):
    """
    Authenticates a user based on provided credentials and logs the outcome.

    Parameters:
        login_credential (dict): Dictionary containing login credentials,
                                 including user ID and password.

    """
    if check_credential(login_credential):
        logger.info(f"User with user ID {login_credential[USER_DICT_USER_ID]} logged in successfully.")
        print(f"Login successful, Welcome {login_credential[USER_DICT_USER_ID]}")
    else:
        logger.error(f"Invalid credentials provided for user ID {login_credential[USER_DICT_USER_ID]}.")
        print(INVALID_CREDENTIAL_MESSAGE)


def display_all_users():
    """
    Retrieves and returns all registered users.

    Returns:
        dict: A dictionary containing all registered users.
    """
    users = get_users()
    logger.info("Retrieved all users successfully.")
    return users


def delete_user():
    """
    Deletes a user based on provided user ID and logs the outcome.

    Prompts the user for a user ID, attempts to delete the corresponding user,
    and logs whether the deletion was successful or if the user ID was not found.

    """
    user_id = input("Enter the user ID of the user to be deleted: ").strip()
    if remove_user(user_id):
        logger.info(f"User with ID {user_id} has been successfully deleted.")
    else:
        logger.error(f"User with ID {user_id} not found.")


def get_by_attribute(attribute_name, search_term):
    """
    Searches for and retrieves users based on a specified attribute.

    Parameters:
        attribute_name (str): The attribute's name to search for.
        search_term (str) : The actual data to be searched

    Returns:
        list: A list of users that match the search criteria.

    """
    return get_by_user_attribute(attribute_name, search_term)
