from helper.logger_constant import (
    LOG_VALUE_ERROR_IN_CUSTOMER_MENU,
    LOG_VALUE_ERROR_IN_UPDATE_PROFILE,
    LOG_CUSTOMER_DELETED_WITH_ID,
    LOG_VALUE_ERROR_IN_ADMIN_MENU,
    LOG_NO_CUSTOMER_SIGNED_UP,
    LOG_APPLICATION_END, LOG_ERROR_CHOICE_RANGE_1_4, LOG_ERROR_ROLE_INTEGER,
    LOG_REDIRECTING_HOME, LOG_END_SEARCH,
    LOG_ERROR_CHOICE_RANGE_1_5, LOG_ERROR_CHOICE_RANGE_1_6,
    LOG_ERROR_INVALID_NAME, LOG_ERROR_INVALID_EMAIL,
    LOG_ERROR_INVALID_PASSWORD, LOG_ERROR_INVALID_MOBILE
)

from helper.menu_constant import (
    CUSTOMER_MENU, UPDATE_CUSTOMER_MENU, ADMIN_MENU, SEARCH_CUSTOMER_MENU,
    MAIN_MENU
)

from helper.prompt_constant import (
    PROMPT_CUSTOMER_NAME, PROMPT_EMAIL, PROMPT_PASSWORD,
    PROMPT_MOBILE, PROMPT_ACCOUNT_NO, PROMPT_CHOICE,
    PROMPT_CUSTOMER_ID, PROMPT_NAME_TO_UPDATE, PROMPT_EMAIL_TO_UPDATE,
    PROMPT_PASSWORD_TO_UPDATE, PROMPT_MOBILE_TO_UPDATE,
    PROMPT_SEARCH_NAME, PROMPT_SEARCH_CUSTOMER_ID, PROMPT_ROLE
)

from resources.logger_configuration import logger

from service.customer_service import (
    search_customer, register_customer, get_all_customer,
    remove_customer, is_customer_present, update_customer
)

from util.validation import (
    is_valid_name, is_valid_email,
    is_valid_password, is_valid_mobile
)

from custom_exception.resource_not_found_exception import ResourceNotFoundException


def get_valid_input(prompt, validation_func, error_message):
    """Helper function to get and validate input."""
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            logger.warning(error_message)
            print()


def collect_customer_details():
    """
    Collects and validates customer details such as name, email, password, mobile number, and account number.

    Prompts the user to input customer details and validates the input using predefined functions.
    Returns the validated customer details.

    Returns:
        tuple: A tuple containing customer_name, customer_email, password, mobile_no, and account_no.
    """
    customer_name = get_valid_input(
        PROMPT_CUSTOMER_NAME,
        is_valid_name,
        LOG_ERROR_INVALID_NAME
    )

    customer_email = get_valid_input(
        PROMPT_EMAIL,
        is_valid_email,
        LOG_ERROR_INVALID_EMAIL
    )

    password = get_valid_input(
        PROMPT_PASSWORD,
        is_valid_password,
        LOG_ERROR_INVALID_PASSWORD
    )

    mobile_no = get_valid_input(
        PROMPT_MOBILE,
        is_valid_mobile,
        LOG_ERROR_INVALID_MOBILE
    )

    account_no = input(PROMPT_ACCOUNT_NO)

    return customer_name, customer_email, password, mobile_no, account_no


def customer():
    """
    Displays the customer menu and processes customer-related actions based on user input.

    The customer menu allows the user to register, view or update their profile, or exit.
    Logs user actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    try:
        while True:
            print(CUSTOMER_MENU)

            choice = int(input(PROMPT_CHOICE))
            if 1 <= choice <= 4:
                if choice == 1:
                    (customer_name, customer_email, password, mobile_no,
                     account_no) = collect_customer_details()
                    register_customer(
                        customer_name, customer_email,
                        password, mobile_no, account_no
                    )
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    logger.info(LOG_REDIRECTING_HOME)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_4)
    except ValueError as e:
        logger.error(LOG_VALUE_ERROR_IN_CUSTOMER_MENU.format(e=e))


def update_profile():
    """
    Updates the profile information of a customer based on the provided customer ID.

    Raises:
        ValueError: If a non-integer input is provided where an integer is expected.
    """
    while True:
        try:
            print(UPDATE_CUSTOMER_MENU)
            choice = int(input(PROMPT_CHOICE))
            if 1 <= choice <= 5:
                customer_id = input(PROMPT_CUSTOMER_ID)
                if is_customer_present(customer_id):
                    if choice == 1:
                        name = input(PROMPT_NAME_TO_UPDATE)
                        update_customer(customer_id, name, "name")
                    elif choice == 2:
                        email = input(PROMPT_EMAIL_TO_UPDATE)
                        update_customer(customer_id, email, "email")
                    elif choice == 3:
                        password = input(PROMPT_PASSWORD_TO_UPDATE)
                        update_customer(customer_id, password, "password")
                    elif choice == 4:
                        mobile = input(PROMPT_MOBILE_TO_UPDATE)
                        update_customer(customer_id, mobile, "mobile")
                    elif choice == 5:
                        logger.info(LOG_REDIRECTING_HOME)
                        break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_5)

        except ValueError as e:
            logger.error(LOG_VALUE_ERROR_IN_UPDATE_PROFILE.format(e=e))
        except ResourceNotFoundException as e:
            logger.error(e)


def admin():
    """
    Displays the admin menu and processes admin-related actions based on user input.

    The admin menu allows the admin to register, search, remove customers, update profiles, or exit.
    Logs actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    while True:
        try:
            print(ADMIN_MENU)
            choice = int(input(PROMPT_CHOICE))
            if 1 <= choice <= 6:
                if choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    while True:
                        try:
                            print(SEARCH_CUSTOMER_MENU)
                            search_choice = int(input(PROMPT_CHOICE))
                            if 1 <= search_choice <= 4:
                                if search_choice == 1:
                                    name = input(PROMPT_SEARCH_NAME)
                                    customers = search_customer(name)
                                    for detail in customers:
                                        for key in detail:
                                            print(key, "-", detail[key])
                                elif search_choice == 2:
                                    customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
                                    customer_detail = search_customer(customer_id)
                                    for detail in customer_detail:
                                        print(detail, "-",
                                              customer_detail[detail])
                                elif search_choice == 3:
                                    for customer_detail in get_all_customer():
                                        if customer_detail is None:
                                            logger.warning(LOG_NO_CUSTOMER_SIGNED_UP)
                                        else:
                                            for key, value in (customer_detail
                                                    .items()):
                                                print(key, "-", value)
                                elif search_choice == 4:
                                    logger.info(LOG_END_SEARCH)
                                    break
                            else:
                                logger.warning(LOG_ERROR_CHOICE_RANGE_1_5)
                        except ResourceNotFoundException as e:
                            logger.error(e)
                        except ValueError as e:
                            logger.error(LOG_VALUE_ERROR_IN_ADMIN_MENU
                                         .format(e=e))

                elif choice == 4:
                    customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
                    remove_customer(customer_id)
                    logger.info(LOG_CUSTOMER_DELETED_WITH_ID.format(customer_id=customer_id))
                elif choice == 5:
                    update_profile()
                elif choice == 6:
                    logger.info(LOG_REDIRECTING_HOME)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_6)
        except ValueError as e:
            logger.error(LOG_VALUE_ERROR_IN_ADMIN_MENU.format(e=e))
        except ResourceNotFoundException as e:
            logger.error(e)


def main():
    """
    Displays the main menu and routes the user to the appropriate role-based menu.

    The main menu allows the user to select a role: customer, admin, or exit.
    Logs actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    while True:
        try:
            print(MAIN_MENU)
            role = int(input(PROMPT_ROLE))

            if 1 <= role <= 4:
                if role == 1:
                    customer()
                elif role == 2:
                    admin()
                elif role == 3:
                    pass
                elif role == 4:
                    logger.info(LOG_APPLICATION_END)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_4)
        except ValueError as e:
            logger.error(LOG_ERROR_ROLE_INTEGER, ": ", e)


if __name__ == "__main__":
    main()
