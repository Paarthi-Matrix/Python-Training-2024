from constants.biznex_constants import (
    CUSTOMER_CATEGORY_NAME,
    USER_DICT_USER_CATEGORY,
    USER_DICT_USER_ID
)
from controller.customer_controller import customer_menu
from resources.logging_config import logger
from service.user_service import check_credential, create, get_all
from vendor_controller import vendor_management


def load_user(user, load):  # todo
    """
       Creates a new user with the specified details.

       Parameters:
           user (dict): The user details to be created.
           load (bool): A flag indicating whether to load additional data.

       Returns:
           dict: The result of the user creation process.
    """
    logger.debug("creating users...")
    return create(user, load)


def login_user(login_credential):
    """
    Authenticates a user based on provided credentials and logs the outcome.

    Parameters:
        login_credential (dict): Dictionary containing login credentials,
                                 including user ID and password.

    """
    while True:  # todo remove while  implement pytantic
        user = check_credential(login_credential)
        if user is not None:
            logger.info(f"User with user ID {login_credential[USER_DICT_USER_ID]} logged in successfully.")
            if user[USER_DICT_USER_CATEGORY] == CUSTOMER_CATEGORY_NAME:
                logger.debug(f"User {user[USER_DICT_USER_CATEGORY]} logged in as customer")
                return customer_menu(user)
            else:
                logger.debug(f"User {user[USER_DICT_USER_CATEGORY]} logged in as vendor")
                return vendor_management(user)
        else:
            logger.error(f"Invalid credentials provided for user ID {login_credential[USER_DICT_USER_ID]}.")
            return


def get_users():
    """
        Retrieves all user records from the data source.

        Returns:
            list: A list of all users retrieved by the `get_all` function.
    """
    return get_all()


