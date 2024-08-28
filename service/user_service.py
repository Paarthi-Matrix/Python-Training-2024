from resources.logging_config import logger

from dao.user_dao import create, delete_user, get_by_attribute, get_by_user_id, get_users, update
from constants.biznex_constants import USER_DICT_USER_ID, USER_DICT_USER_PASSWORD


def add_user(user):
    """
    Adds a new user by creating a user entry and assigning a unique ID.

    Parameters:
        user (dict): Dictionary containing user details.
                     The dictionary should have user details except the user ID.

    Returns:
        dict: Returns the user dictionary with the generated user ID.
    """
    logger.debug(f"Attempting to add user with details: {user}")
    user = create(user)
    logger.info(f"User {user['name']} added successfully with ID: {user['user_id']}")
    return user


def check_credential(login_credential):
    """
    Verifies the user's credentials for login.

    Parameters:
        login_credential (dict): Dictionary containing user ID and password.

    Returns:
        bool: Returns True if the credentials are valid; otherwise, returns False.
    """
    logger.debug(f"Checking credentials for user ID: {login_credential[USER_DICT_USER_ID]}")
    user = get_by_user_id(login_credential[USER_DICT_USER_ID])
    if user is None or user[USER_DICT_USER_PASSWORD] != login_credential[USER_DICT_USER_PASSWORD]:
        logger.warning(f"Invalid login attempt for user ID: {login_credential[USER_DICT_USER_ID]}")
        return False
    logger.info(f"User ID {login_credential[USER_DICT_USER_ID]} logged in successfully.")
    return True


def get_all_users():
    """
    Retrieves all users from the system.

    Returns:
        dict: Returns a dictionary of all users.
    """
    logger.debug("Retrieving all users.")
    users = get_users()
    logger.info(f"Retrieved {len(users)} users.")
    return users


def remove_user(user_id):
    """
    Removes a user from the system by their user ID.

    Parameters:
        user_id (str): The ID of the user to be removed.

    Returns:
        bool: Returns True if the user was successfully removed; otherwise, returns False.
    """
    logger.debug(f"Attempting to remove user with ID: {user_id}")
    result = delete_user(user_id)
    if result:
        logger.info(f"User with ID {user_id} removed successfully.")
    else:
        logger.error(f"Failed to remove user with ID {user_id}. User not found.")
    return result


def get_by_user_attribute(attribute_name, search_term):
    """
    Retrieves a user or users based on a specified attribute.

    Parameters:
        attribute_name (str): The name of the attribute to search by.
        search_term (str): The value to search for within the specified attribute.

    Returns:
        dict: Returns a dictionary of users that match the search criteria.
    """
    logger.debug(f"Searching for users with {attribute_name} = {search_term}")
    users = get_by_attribute(attribute_name, search_term)
    if users:
        logger.info(f"Found {len(users)} user(s) with {attribute_name} = {search_term}")
    else:
        logger.warning(f"No users found with {attribute_name} = {search_term}")
    return users


def update_password(user):
    """
    Updates the password of the user
    """
    update(user)
