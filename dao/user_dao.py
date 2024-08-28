import random
import string

from constants.biznex_constants import CUSTOMER_CATEGORY_NAME
from constants.biznex_constants import CUSTOMER_ID_PREFIX
from constants.biznex_constants import USER_DICT_USER_CATEGORY
from constants.biznex_constants import USER_DICT_USER_ID
from constants.biznex_constants import VENDOR_CATEGORY_NAME
from constants.biznex_constants import VENDOR_ID_PREFIX
from custom_exceptions.id_generation_exception import IdGenerationException

users = {}


def user_id_generator(user_category):
    """
    Generates a unique user ID based on the user category.

    Parameters:
        user_category (str) : This string represents the category of the user. (VENDOR or USER)

    Returns:
        user_id (str) : Returns a unique user id for every user based on their category
                        Returns None if user_category is invalid.
    """
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    if user_category.upper() == VENDOR_CATEGORY_NAME:
        return VENDOR_ID_PREFIX + random_string
    elif user_category.upper() == CUSTOMER_CATEGORY_NAME:
        return CUSTOMER_ID_PREFIX + random_string
    else:
        return None


def create(user):
    """
    Creates a user and assigns a unique ID.

    Parameters:
        user (dict) : Dictionary of user details

    Returns:
        user (dict) : Returns a dict containing user details with generated user_id.
    """
    user_id = user_id_generator(user[USER_DICT_USER_CATEGORY])
    print("User id is", user_id)
    if user_id is None:
        raise IdGenerationException(user[USER_DICT_USER_CATEGORY])
    users[user_id] = user
    user[USER_DICT_USER_ID] = user_id
    return user


def get_by_user_id(user_id):
    """
    Retrieves a user by their ID.

    Parameters:
        user_id (str) : user id of the user to be retrieved.

    Returns:
        user (dict) : Returns the user based on the user_id
                      Returns None if there is no such user id found
    """

    if user_id not in users:
        return None
    return users[user_id]


def get_users():
    """
    Returns all users.

    Returns:
        users (dict) : Returns dictionary of users
    """
    print("dao user")
    return users


def delete_user(user_id):
    """
    Deletes a user based on the user ID.

    Parameters:
        user_id (str) : The ID of the user to be deleted.

    Returns:
        bool : Returns True if the user was successfully deleted; otherwise, returns False.
    """
    if user_id in users:
        del users[user_id]
        return True
    return False


def get_by_attribute(attribute_name, search_term):
    """
    This function is used to search and get list of users by specified attribute.

    Parameters:
        attribute_name (str) : Name of the attribute to be changed.
        search_term (str) : The value or date to be searched in the dictionary.

    Returns:
        search_list (list) : The list of users that matches the search term.
                             Returns empty list if no matches found.
    """
    search_result = []
    for user_id, data in users.items():
        attribute_value = data.get(attribute_name, "")
        if search_term.lower() in attribute_value.lower():
            search_result.append(data)
    return search_result


def update(user):
    """
    Updates the users by user_id
    """
    users[user[USER_DICT_USER_ID]] = user
    return
