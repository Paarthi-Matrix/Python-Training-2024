from Services.user_service import create_user, login_user, add_money
from Utils.log_configuration import setup_logger

logger = setup_logger()


def user_creation_controller(username, password, email):
    return create_user(username, password, email)


def user_login_controller(username, password):
    return login_user(username, password)


def add_money_controller(user_id, amount):
    return add_money(user_id, amount)
