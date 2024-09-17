from constant.constant import (USER_CREATION_SUCCESS, ERROR_USER_CREATION, USER_LOGIN_SUCCESS, ERROR_ADD_MONEY,
                               ERROR_USER_NOT_FOUND, ERROR_USER_LOGIN, USER_MONEY_ADDED, USER_NOT_FOUND)
from service.user import create_user, login_user, add_money
from resources.log_configuration import setup_logger

logger = setup_logger()


def user_creation_controller(username, password, email):
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
    try:
        if add_money(user_id, amount):
            logger.info(USER_MONEY_ADDED.format(amount, user_id))
            return USER_MONEY_ADDED.format(amount, user_id)
        return USER_NOT_FOUND
    except ValueError:
        logger.error(ERROR_ADD_MONEY)
        return ERROR_ADD_MONEY
