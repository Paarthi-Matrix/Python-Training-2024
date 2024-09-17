import re
import uuid


from constant.constant import (USERNAME_REGEX, PASSWORD_REGEX, EMAIL_REGEX, ERROR_USER_EXISTS, INITIAL_BALANCE,
                               USER_MONEY_ADDED, USER_LOGIN_SUCCESS, USER_BALANCE, ERROR_USER_NOT_FOUND)
from resources.log_configuration import setup_logger

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
    return user_id


def login_user(username, password):
    for user_id, user_details in users_db.items():
        if (user_details['username'] == username) and (user_details['password'] == password):
            logger.info(USER_LOGIN_SUCCESS.format(user_id))
            return user_id
    return None


def add_money(user_id, amount):
    """
    User add money feature
    -User can add the money after logging in.
    :param user_id: User_id of the user
    :param amount: amount to be added in the user account
    :return: returns true or false
    """
    if user_id in users_db:
        users_db[user_id]['amount'] += amount
        logger.info(USER_MONEY_ADDED.format(amount, user_id))
        return True
    return False


def get_user_balance(user_id):
    """
    User balance display:
    - This function is used to check the users balance
    - This is usually done after adding the money to the balance
    :param user_id: uuid generated
    :return: balance float type returns
    """
    if user_id in users_db:
        balance = users_db[user_id]['amount']
        logger.info(USER_BALANCE.format(balance))
        return balance
    return ERROR_USER_NOT_FOUND
