import re
import uuid


from Utils.constants import (USERNAME_REGEX, PASSWORD_REGEX, EMAIL_REGEX, ERROR_USER_NOT_FOUND, INVALID_CREDENTIALS,
                             ERROR_ADD_MONEY, USER_CREATION_SUCCESS, ERROR_USER_EXISTS, INITIAL_BALANCE,
                             USER_MONEY_ADDED, ERROR_USER_CREATION, USER_LOGIN_SUCCESS)
from Utils.log_configuration import setup_logger

logger = setup_logger()

users_db = {}


def username_check(username):
    """To validate username with regex."""
    if not re.match(USERNAME_REGEX, username):
        raise ValueError("Invalid username format.")


def password_check(password):
    """to validate password with regex."""
    if not re.match(PASSWORD_REGEX, password):
        raise ValueError("Invalid password format.")


def email_check(email):
    """To validate email with regex."""
    if not re.match(EMAIL_REGEX, email):
        raise ValueError("Invalid email format.")


def create_user(username, password, email):
    """To create a new user with validation."""
    try:
        username_check(username)
        password_check(password)
        email_check(email)
        if any(user['username'] == username for user in users_db.values()):
            raise ValueError(ERROR_USER_EXISTS.format(username))
        user_id = f"user_{str(uuid.uuid4())}"
        users_db[user_id] = {
            'username': username,
            'password': password,
            'email': email,
            'amount': INITIAL_BALANCE
        }
        logger.info(USER_CREATION_SUCCESS.format(username, user_id))
        return user_id
    except ValueError as e:
        logger.error(ERROR_USER_CREATION.format(username, e))
        return None


def login_user(username, password):
    try:
        for user_id, user_details in users_db.items():
            if (user_details['username'] == username) and (user_details['password'] == password):
                logger.info(USER_LOGIN_SUCCESS.format(user_id))
                return user_id
        logger.error(INVALID_CREDENTIALS)
        return None
    except ValueError as e:
        logger.error(ERROR_USER_NOT_FOUND)
        return None


def add_money(user_id, amount):
    try:
        if user_id in users_db:
            users_db[user_id]['amount'] += amount
            logger.info(USER_MONEY_ADDED.format(amount, user_id))
            return True
        else:
            logger.error(ERROR_USER_NOT_FOUND)
            return False
    except ValueError:
        logger.error(ERROR_ADD_MONEY)
        return False
