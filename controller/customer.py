from helper.constant import (
    LOG_BIN_ALREADY_CREATED,
    LOG_ERROR_COMPLAINT_INVALID,
    LOG_COMPLAINT_REGISTERED,
    LOG_ERROR_CHOICE_RANGE_1_6, CUSTOMER_MENU,
    PROMPT_CHOICE, PROMPT_SEARCH_CUSTOMER_ID, PROMPT_BIN_ID,
    PROMPT_RAISE_COMPLAINT, PROMPT_EMAIL, PROMPT_CONTINUE_PROCESS, PROMPT_YES, ONE, SIX, TWO, THREE, FOUR, FIVE,
)

from resources.logger_configuration import logger

from service.customer import (
    register_customer,
    is_customer_present,
    create_bin,
    is_bin_available,
    is_bin_created_for_customer,
    raise_complaint,
    get_customer_details,
    get_customer_bin
)

from service.driver import (
    is_valid_complaint,
    check_profit
)

from util.validation import (
    is_complaint_valid,
    get_valid_input,
    collect_bin_details,
    collect_customer_details
)


def ask_for_continue():
    choice = input(PROMPT_CONTINUE_PROCESS)
    if choice.upper() == PROMPT_YES:
        perform_customer_actions()


def perform_customer_actions():
    result = {}
    """
    Displays the customer menu and processes customer-related actions based on user input.

    The customer menu allows the user to register, view or update their profile, or exit.
    Logs user actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    print(CUSTOMER_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= SIX:
        if choice == ONE:
            customer_name, customer_email, password, mobile_no = \
                collect_customer_details()
            register_customer(
                customer_name, customer_email,
                password, mobile_no
            )
            result['status'] = 'Customer Registered Successfully'

        elif choice == TWO:
            customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
            if is_customer_present(customer_id):
                if not is_bin_created_for_customer(customer_id):
                    (area, door_no, landmark, city, load_type,
                     cycle_period, wastage_type, driver_email) = collect_bin_details()
                    create_bin(area, door_no, landmark, city, load_type, cycle_period, wastage_type,
                               driver_email, customer_id)
                    result['status'] = 'Bin Registered Successfully'
                else:
                    logger.error(LOG_BIN_ALREADY_CREATED.format(customer_id=customer_id))
        elif choice == THREE:
            bin_id = input(PROMPT_BIN_ID)
            if is_bin_available(bin_id):
                if is_valid_complaint(bin_id):
                    complaint = get_valid_input(PROMPT_RAISE_COMPLAINT, is_complaint_valid,
                                                LOG_ERROR_COMPLAINT_INVALID)
                    raise_complaint(bin_id, complaint)
                    result['status'] = LOG_COMPLAINT_REGISTERED.format(bin_id=bin_id)
                    logger.info(LOG_COMPLAINT_REGISTERED.format(bin_id=bin_id))
        elif choice == FOUR:
            bin_id = input(PROMPT_BIN_ID)
            if is_bin_available(bin_id):
                work_reports = check_profit(bin_id)
                result['work_reports'] = work_reports
        elif choice == FIVE:
            email = input(PROMPT_EMAIL)
            customer_id, customer_details = get_customer_details(email)
            result['customer_id'] = customer_id
            result['customer_details'] = customer_details
        elif choice == SIX:
            customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
            if is_customer_present(customer_id):
                bin_id, bin_details = get_customer_bin(customer_id)
                result['bin_id'] = bin_id
                result['bin_details'] = bin_details
    else:
        logger.warning(LOG_ERROR_CHOICE_RANGE_1_6)

    return result
