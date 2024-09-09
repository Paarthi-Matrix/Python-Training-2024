from constant.logger_constant import (
    LOG_VALUE_ERROR_IN_CUSTOMER_MENU,
    LOG_REDIRECTING_HOME,
    LOG_BIN_ALREADY_CREATED,
    LOG_ERROR_COMPLAINT_INVALID,
    LOG_COMPLAINT_REGISTERED,
    LOG_ERROR_CHOICE_RANGE_1_6,
)

from constant.menu_constant import (
    CUSTOMER_MENU
)

from constant.prompt_constant import (
    PROMPT_EMAIL,
    PROMPT_CHOICE,
    PROMPT_SEARCH_CUSTOMER_ID,
    PROMPT_BIN_ID,
    PROMPT_RAISE_COMPLAINT
)

from resources.logger_configuration import logger

from service.customer_service import (
    register_customer,
    is_customer_present,
    create_bin,
    is_bin_available,
    is_bin_created_for_customer,
    raise_complaint,
    get_customer_details,
    get_customer_bin
)

from service.driver_service import (
    is_valid_complaint,
    check_profit
)

from util.validation import (
    is_complaint_valid,
    get_valid_input,
    collect_bin_details,
    collect_customer_details
)

from exception.custom_exception import (
    ResourceNotFoundException,
    UserAlreadyExistsError, GarbageCollectorException
)


def customer():
    """
    Displays the customer menu and processes customer-related actions based on user input.

    The customer menu allows the user to register, view or update their profile, or exit.
    Logs user actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    while True:
        try:
            print(CUSTOMER_MENU)

            choice = int(input(PROMPT_CHOICE))
            if 1 <= choice <= 7:
                if choice == 1:
                    customer_name, customer_email, password, mobile_no = \
                        collect_customer_details()
                    register_customer(
                        customer_name, customer_email,
                        password, mobile_no
                    )
                elif choice == 2:
                    customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
                    if is_customer_present(customer_id):
                        if not is_bin_created_for_customer(customer_id):
                            area, door_no, landmark, city, load_type, cycle_period, wastage_type, driver_email \
                                = collect_bin_details()
                            create_bin(area, door_no, landmark, city, load_type, cycle_period, wastage_type,
                                       driver_email, customer_id)
                        else:
                            logger.error(LOG_BIN_ALREADY_CREATED.format(customer_id=customer_id))
                elif choice == 3:
                    bin_id = input(PROMPT_BIN_ID)
                    if is_bin_available(bin_id):
                        if is_valid_complaint(bin_id):
                            complaint = get_valid_input(PROMPT_RAISE_COMPLAINT, is_complaint_valid,
                                                        LOG_ERROR_COMPLAINT_INVALID)
                            raise_complaint(bin_id, complaint)
                            logger.info(LOG_COMPLAINT_REGISTERED.format(bin_id=bin_id))
                elif choice == 4:
                    bin_id = input(PROMPT_BIN_ID)
                    if is_bin_available(bin_id):
                        work_reports = check_profit(bin_id)
                        for work_item, work_detail in work_reports.items():
                            print(work_item, " : ", work_detail)
                elif choice == 5:
                    email = input(PROMPT_EMAIL)
                    customer_id, customer_details = get_customer_details(email)
                    print("Customer Id: ", customer_id)
                    for customer_item, customer_detail in customer_details.items():
                        print(customer_item, " : ", customer_detail)
                elif choice == 6:
                    customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
                    if is_customer_present(customer_id):
                        bin_id, bin_details = get_customer_bin(customer_id)
                        print("Bin_Id: ", bin_id)
                        for bin_item, bin_detail in bin_details.items():
                            if bin_item != "customer_id":
                                print(bin_item, " : ", bin_detail)
                elif choice == 7:
                    logger.info(LOG_REDIRECTING_HOME)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_6)
        except ValueError as e:
            logger.error(LOG_VALUE_ERROR_IN_CUSTOMER_MENU.format(e=e))
        except UserAlreadyExistsError as e:
            logger.error(e)
        except ResourceNotFoundException as e:
            logger.error(e)
        except GarbageCollectorException as e:
            logger.error(e)
