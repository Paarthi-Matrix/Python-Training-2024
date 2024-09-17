from constant.constant import (
    USER_DICT_USER_CATEGORY,
    USER_DICT_NAME, INVALID_NAME_FORMATE, NAME_ERROR, USER_DICT_PHONE_NUMBER, INVALID_PASSWORD,
    PHONE_NUMBER_ERROR, USER_DICT_EMAIL, INVALID_EMAIL,
    EMAIL_ERROR, USER_DICT_GENDER,
    USER_DICT_DOB, GENDER_ERROR,
    INVALID_GENDER, INVALID_DOB, DOB_ERROR, USER_DICT_USER_PASSWORD, PASSWORD_ERROR
)
from resources.config import logger
from service.user import check_and_return_user, create, get_all, delete as delete_by_id
from util.password_utils import hash_password
from util.user_input_validation import user_name_validation, phone_number_validation, email_validation, \
    gender_validation, date_of_birth_validation, password_validation


def load(user, load):
    """
       Creates a new user with the specified details.

       Parameters:
           user (dict): The user details to be created.
           load (bool) : This boolean flag determines whether the file user need to be added in user
                      Optional parameter if you don't want to write user to the file

       Returns:
           dict : The result of the user creation process.
    """
    error_message = {}
    if not user_name_validation(user[USER_DICT_NAME]):
        error_message[NAME_ERROR] = INVALID_NAME_FORMATE
    if not phone_number_validation(user[USER_DICT_PHONE_NUMBER]):
        error_message[PHONE_NUMBER_ERROR] = INVALID_PASSWORD
    if not email_validation(user[USER_DICT_EMAIL]):
        error_message[EMAIL_ERROR] = INVALID_EMAIL
    if not gender_validation(user[USER_DICT_GENDER]):
        error_message[GENDER_ERROR] = INVALID_GENDER
    if not date_of_birth_validation(user[USER_DICT_DOB]):
        error_message[DOB_ERROR] = INVALID_DOB
    if (not load) and (not password_validation(user[USER_DICT_USER_PASSWORD])):
        error_message[PASSWORD_ERROR] = INVALID_PASSWORD

    if len(error_message):
        return error_message
    if not load:
        user[USER_DICT_USER_PASSWORD] = hash_password(user[USER_DICT_USER_PASSWORD])
    return create(user, load)


def login_user(login_credential):
    """
    Authenticates a user based on provided credentials and logs the outcome.

    Parameters:
        login_credential (dict): Dictionary containing login credentials,
                                 including user ID and password.

    """
    user = check_and_return_user(login_credential)
    if user is not None:
        logger.info(f"User with user ID {login_credential[USER_DICT_EMAIL]} logged in successfully.")
        logger.info(f"User {login_credential[USER_DICT_EMAIL]} logged in as {user[USER_DICT_USER_CATEGORY]}")
        return user
    else:
        logger.warn(f"Invalid credentials provided for user ID {login_credential[USER_DICT_EMAIL]}.")
        return None


def get_users():
    """
        Retrieves all user records from the data source.

        Returns:
            dict : A list of all users retrieved by the `get_all` function.
    """
    return get_all()


def delete(user_id):
    """
    Used to softly delete the user from the database

    Parameters:
        user_id (str) : User id of the user

    Returns:
        bool  : True if the user is deleted successfully.
                False if no user id found

    """
    return delete_by_id(user_id)


