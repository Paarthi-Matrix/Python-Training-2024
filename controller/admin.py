from helper.constant import (
    LOG_CUSTOMER_DELETED_WITH_ID,
    LOG_NO_CUSTOMER_SIGNED_UP,
    LOG_ADMIN_CREATED_WITH_ID,
    LOG_UNAUTHORIZED_ADMIN_CREATION_ATTEMPT,
    LOG_ERROR_CHOICE_RANGE_1_5,
    LOG_ADMIN_AUTHORIZATION,
    LOG_WORK_REPORT,
    LOG_RECYCLER_REGISTERED,
    LOG_WASTAGE_WEIGHT_CALCULATED,
    LOG_CALCULATED_PROFIT,
    LOG_ERROR_CHOICE_RANGE_1_13, LOG_RECYCLER_ALREADY_REGISTERED, ADMIN_MENU, PROMPT_CHOICE, SEARCH_CUSTOMER_MENU,
    PROMPT_SEARCH_NAME, PROMPT_SEARCH_CUSTOMER_ID, PROMPT_DRIVER_AREA, UPDATE_CUSTOMER_MENU, PROMPT_NAME_TO_UPDATE,
    PROMPT_EMAIL_TO_UPDATE, PROMPT_PASSWORD_TO_UPDATE, PROMPT_MOBILE_TO_UPDATE, ONE, THIRTEEN, TWO, THREE, FOUR, FIVE,
    SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN, TWELVE,
)

from resources.logger_configuration import logger

from service.customer import (
    search_customer,
    get_all_customer,
    remove_customer,
    update_customer,
    is_customer_present,
    view_all_complaints
)

from service.admin import (
    register_admin,
    is_admin_registered
)

from service.driver import (
    register_driver,
    search_driver,
    get_all_work_reports,
    check_wastage,
)

from service.recycler import (
    register_recycler,
    is_recycler_registered,
    calculate_profit,
    get_cost_of_garbage
)

from util.validation import (
    collect_admin_details,
    collect_driver_details,
    collect_recycler_details
)


def get_customer_detail():
    print(SEARCH_CUSTOMER_MENU)
    search_choice = int(input(PROMPT_CHOICE))
    if ONE <= search_choice <= FOUR:
        if search_choice == ONE:
            name = input(PROMPT_SEARCH_NAME)
            customers = search_customer(name)
            for id_of_customer in customers:
                print("Customer_Id: ", id_of_customer)
                for customer_attribute in customers[id_of_customer]:
                    print(customer_attribute, "-",
                          customers[id_of_customer][customer_attribute])
        elif search_choice == TWO:
            id_of_customer = input(PROMPT_SEARCH_CUSTOMER_ID)
            customer_detail = search_customer(id_of_customer)
            print("Customer_Id: ", id_of_customer)
            for detail in customer_detail:
                print(detail, "-",
                      customer_detail[detail])
        elif search_choice == THREE:
            customers = get_all_customer()
            for id_of_customer, customer_detail in customers:
                if id_of_customer is None:
                    logger.warning(LOG_NO_CUSTOMER_SIGNED_UP)
                else:
                    print("Customer_Id: ", id_of_customer)
                    for customer_attribute, detail in (customer_detail.items()):
                        print(customer_attribute, "-", detail)
    else:
        logger.warning(LOG_ERROR_CHOICE_RANGE_1_5)


def manage_admin_tasks():
    """
    Displays the admin menu and processes admin-related actions based on user input.

    The admin menu allows the admin to register, search, remove customers, update profiles, or exit.
    Logs actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    print(ADMIN_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= THIRTEEN:
        if choice == ONE:
            if not is_admin_registered():
                name, email, password = collect_admin_details()
                register_status = register_admin(name, email, password)
                logger.info(LOG_ADMIN_CREATED_WITH_ID.
                            format(register_status=register_status))
            else:
                logger.warning(LOG_UNAUTHORIZED_ADMIN_CREATION_ATTEMPT)
        elif choice == TWO:
            if is_admin_registered():
                name, email, password, mobile_no, area = (
                    collect_driver_details())
                register_driver(name, email, password, mobile_no, area)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == THREE:
            if is_admin_registered():
                get_customer_detail()
        elif choice == FOUR:
            if is_admin_registered():
                customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
                remove_customer(customer_id)
                logger.info(LOG_CUSTOMER_DELETED_WITH_ID.format(customer_id=customer_id))
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == FIVE:
            if is_admin_registered():
                customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
                if is_customer_present(customer_id):
                    update_profile(customer_id)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == SIX:
            if is_admin_registered():
                area = input(PROMPT_DRIVER_AREA)
                driver = search_driver(area)
                if driver is not None:
                    for key in driver:
                        print(key, ' - ', driver[key])
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == SEVEN:
            if is_admin_registered():
                work_report = get_all_work_reports()
                if work_report is not None:
                    for work_id in work_report:
                        print("Work Id: ", work_id)
                        for bin_attribute, detail in work_report[work_id].items():
                            print(bin_attribute, ":", detail)
                        print()
                else:
                    logger.info(LOG_WORK_REPORT)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == EIGHT:
            if is_admin_registered():
                complaints = view_all_complaints()
                for complaint_id, bin_detail in complaints:
                    print("Complaint Id:", complaint_id)
                    for bin_attribute, complaint in bin_detail.items():
                        print(bin_attribute, " : ", complaint)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == NINE:
            if is_admin_registered():
                if not is_recycler_registered():
                    recycler_name, recycler_email, password, mobile_no = collect_recycler_details()
                    recycler_id = register_recycler(recycler_name, recycler_email, password, mobile_no)
                    logger.info(LOG_RECYCLER_REGISTERED.format(recycler_id=recycler_id))
                else:
                    logger.warning(LOG_RECYCLER_ALREADY_REGISTERED)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == TEN:
            if is_admin_registered():
                total_waste, bio_waste_weight, non_bio_waste_weight = check_wastage()
                logger.info(
                    LOG_WASTAGE_WEIGHT_CALCULATED.format(total_waste, bio_waste_weight, non_bio_waste_weight))
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == ELEVEN:
            if is_admin_registered():
                wastage = get_cost_of_garbage()
                for wastage_item, wastage_data in wastage.items():
                    print(wastage_item, " : ", wastage_data)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
        elif choice == TWELVE:
            if is_admin_registered():
                calculate_profit()
                logger.info(LOG_CALCULATED_PROFIT)
            else:
                logger.warning(LOG_ADMIN_AUTHORIZATION)
    else:
        logger.warning(LOG_ERROR_CHOICE_RANGE_1_13)


def update_profile(customer_id):
    """
    Updates the profile information of a customer based on the provided customer ID.

    Raises:
        ValueError: If a non-integer input is provided where an integer is expected.
    """
    print(UPDATE_CUSTOMER_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= FIVE:
        if choice == ONE:
            name = input(PROMPT_NAME_TO_UPDATE)
            update_customer(customer_id, name, "name")
        elif choice == TWO:
            email = input(PROMPT_EMAIL_TO_UPDATE)
            update_customer(customer_id, email, "email")
        elif choice == THREE:
            password = input(PROMPT_PASSWORD_TO_UPDATE)
            update_customer(customer_id, password, "password")
        elif choice == FOUR:
            mobile = input(PROMPT_MOBILE_TO_UPDATE)
            update_customer(customer_id, mobile, "mobile_no")
    else:
        logger.warning(LOG_ERROR_CHOICE_RANGE_1_5)
