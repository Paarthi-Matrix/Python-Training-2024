from constant.constant import (USER_CREATION_SUCCESS, ERROR_USER_CREATION, USER_LOGIN_SUCCESS, ERROR_ADD_MONEY,
                               ERROR_USER_NOT_FOUND, ERROR_USER_LOGIN, USER_MONEY_ADDED, USER_NOT_FOUND)
from service.user import create_user, login_user, add_money
from resources.log_configuration import setup_logger

logger = setup_logger()


def user_creation_controller(username, password, email):
    """
    User creation controller.
    Checks if the create_user is success or not
    Returns success message or error message if user creation is not done
    :param username: username string type
    :param password: password string type
    :param email: email string type
    :return: success message or error message
    """
    try:
        user_id = create_user(username, password, email)
        if user_id:
            logger.info(USER_CREATION_SUCCESS.format(username, user_id))
            return USER_CREATION_SUCCESS.format(username, user_id)
        return ERROR_USER_CREATION.format(username)
    except ValueError:
        logger.error(ERROR_USER_CREATION.format(username))
        return ERROR_USER_CREATION.format(username)


def user_login_controller(username, password):
    """
    After user creation logging is done.
    -Checks if the user exists and logged in message is showed
    -Value error is handled if the user is not existed
    :param username: username user input
    :param password: password user input
    :return: success message or error message
    """
    try:
        user_id = login_user(username, password)
        if user_id:
            logger.info(USER_LOGIN_SUCCESS.format(user_id))
            return USER_LOGIN_SUCCESS.format(user_id)
        return ERROR_USER_NOT_FOUND
    except ValueError:
        logger.error(ERROR_USER_LOGIN)
        return ERROR_USER_LOGIN


def add_money_controller(user_id, amount):
    """
    Add money feature
    -user after login can enter the money
    - If add money is true, the success message is displayed
    - Returns error message if the add_money is false
    :param user_id: user_id generated UUID
    :param amount: float amount
    :return: returns error message or success message
    """
    try:
        if add_money(user_id, amount):
            logger.info(USER_MONEY_ADDED.format(amount, user_id))
            return USER_MONEY_ADDED.format(amount, user_id)
        return USER_NOT_FOUND
    except ValueError:
        logger.error(ERROR_ADD_MONEY)
        return ERROR_ADD_MONEY
