import json
import uuid

from constants.constants import (
    FILE_PATH, USER_DICT_IS_DELETE,
    USER_DICT_USER_ID, USER_DICT_USER_PASSWORD, USER_DICT_EMAIL
)
from resources.config import logger
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
        load (bool) : This boolean flag determines whether the file user need to be added in user
                      Optional parameter if you don't want to write user to the file

    Returns:
        user (dict) : Returns a dict containing user details with generated user_id.
    """
    user_id = uuid.uuid4()
    user[USER_DICT_USER_ID] = str(user_id)
    if not load:
        put_user_to_file(user)
    users[user[USER_DICT_EMAIL]] = user
    return user


def get_by_email(user_email):
    """
    Retrieves a user by their e-email.

    Parameters:
        user_email (str) : user email of the user to be retrieved.

    Returns:
        user (dict) : Returns the user based on the user_email
                      Returns None if there is no such user email found
    """
    if user_email in users:
        return users[user_email]
    return None


def check_and_return_user(login_credential):
    """
    Verifies the user's credentials for login.

    Parameters:
        login_credential (dict): Dictionary containing user ID and password.

    Returns:
        bool: Returns True if the credentials are valid; otherwise, returns False.
    """
    user_email = login_credential[USER_DICT_EMAIL]
    logger.debug(f"Checking credentials for user email: {user_email}")
    user = get_by_email(user_email)
    if user is None or (user[USER_DICT_IS_DELETE]):
        logger.error(f"Invalid user email: {user_email}. User not found.")
        return None
    hashed_password = hash_password(login_credential[USER_DICT_USER_PASSWORD])
    if user[USER_DICT_USER_PASSWORD] != hashed_password:
        print("db password", user[USER_DICT_USER_PASSWORD])
        print("user given pasword", hashed_password)
        logger.warning(f"Invalid password for user email: {user_email}.")
        return None
    logger.info(f"User {user_email} logged in successfully.")
    return user


def get_all():
    return users


def delete(user_id):
    """
        This function is used to softly delete the user based on user_id

        Parameters:
             user_id (str) : User id to be deleted

        Returns:
            bool : returns True if the user deleted successfully
                   Else return False
    """
    user = users.get(user_id.strip(), None)
    if user is None:
        return False
    else:
        user[USER_DICT_IS_DELETE] = True
        logger.info(f"User {user[USER_DICT_USER_ID]} deleted.")
        return True
