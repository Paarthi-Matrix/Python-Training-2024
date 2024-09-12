import json
import uuid

from constants.biznex_constants import (
    FILE_PATH, USER_DICT_IS_DELETE,
    USER_DICT_USER_ID, USER_DICT_USER_PASSWORD
)
from resources.logging_config import logger
from utils.password_utils import hash_password


users = {}


def put_user_to_file(user):
    """
        Writes a user's data to a file in JSON format.

        The function converts the user ID to a string and appends the user's data
        to the specified file in JSON format, ensuring each user is written on a new line.

        Parameters:
            user (dict): A dictionary containing user information.
    """
    file_path = FILE_PATH
    user[USER_DICT_USER_ID] = str(user[USER_DICT_USER_ID])
    with open(file_path, "a") as file:
        file.write(json.dumps(user) + "\n")


def create(user, load=False):
    """
    Creates a user and assigns a unique ID.

    Parameters:
        user (dict) : Dictionary of user details

    Returns:
        user (dict) : Returns a dict containing user details with generated user_id.
        load (bool) : Optional parameter if you don't want to write user to the file
    """

    user_id = ""
    if not load:
        user_id = uuid.uuid4()
        user[USER_DICT_USER_ID] = str(user_id)
        put_user_to_file(user)
    else:
        user_id = user[USER_DICT_USER_ID]

    users[str(user_id)] = user
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
    print("Current users dictionary:", users)

    if user_id not in users:
        return None
    return users[user_id]


def check_credential(login_credential):
    """
    Verifies the user's credentials for login.

    Parameters:
        login_credential (dict): Dictionary containing user ID and password.

    Returns:
        bool: Returns True if the credentials are valid; otherwise, returns False.
    """
    user_id = login_credential[USER_DICT_USER_ID]
    logger.debug(f"Checking credentials for user ID: {user_id}")

    user = get_by_user_id(user_id)

    if user is None or user[USER_DICT_IS_DELETE] == True:
        logger.error(f"Invalid user ID: {user_id}. User not found.")
        return None

    hashed_password = hash_password(login_credential[USER_DICT_USER_PASSWORD])
    if user[USER_DICT_USER_PASSWORD] != hashed_password:
        logger.warning(f"Invalid password for user ID: {user_id}.")
        return None

    logger.info(f"User ID {user_id} logged in successfully.")
    return user


def get_all():
    return users


def delete_by_id(user_id):
    """
        This function is used to softly delete the user based on user_id

        Parameters:
             user_id (str) : User id to be deleted

        Returns:
            bool : returns True if the user deleted successfully
                   Else return False
    """
    user = users.get(user_id, None)
    if user is None:
        return False
    else:
        user[USER_DICT_IS_DELETE] = True
        return True
