import getpass

from controller.admin import (add_admin_detail, add_driver, add_recycler, calculate_total_profit,
                              check_customer_present, delete_customer, find_all_customer, find_customer,
                              find_driver, fetch_all_work_reports, get_all_complaints, report_to_recycler,
                              cost_of_wastage_report, update_customer_detail, load_admins, validate_admin,
                              is_admin_already_registered)

from controller.customer import (add_customer, check_if_bin_available, check_if_customer_present,
                                 check_if_profit_credited, fetch_customer_detail, get_bin_detail,
                                 is_area_available, validate_complaint, add_bin_detail)

from controller.driver import (collect_details_to_update, find_bins, fetch_work_reports, get_bin_details,
                               get_complaints, get_driver_detail, give_work_report)

from controller.recycler import fetch_wastage_report, rate_calculation, check_if_recycler_registered

from exception.custom_exception import (GarbageCollectorException,
                                        ResourceAlreadyExistsException, ResourceNotFoundException,
                                        UserAlreadyExistsError)

from helper.constant import (ADMIN_MENU, BIN_CREATED_WITH_ID,
                             COMPLAINT_REGISTERED, CUSTOMER_ID, CUSTOMER_MENU, CUSTOMER_REGISTERED,
                             DICT_EMAIL, DICT_MOBILE, DICT_NAME, CHOICE_RANGE_1_13, ERROR_COMPLAINT_INVALID,
                             ERROR_INVALID_STATUS, LOG_APPLICATION_END, VALUE_ERROR_IN_CUSTOMER_MENU,
                             MAIN_MENU, NO_CUSTOMER_SIGNED_UP, NO_WORK_REPORT, ONE, PROMPT_ADMIN_NAME,
                             PROMPT_BIN_ID, PROMPT_BIN_STATUS, PROMPT_CHOICE, PROMPT_CUSTOMER_AREA,
                             PROMPT_CUSTOMER_CITY, PROMPT_CUSTOMER_CYCLE_PERIOD, PROMPT_CUSTOMER_DOOR_NO,
                             PROMPT_CUSTOMER_LANDMARK, PROMPT_CUSTOMER_LOAD,
                             PROMPT_CUSTOMER_NAME, PROMPT_CUSTOMER_WASTAGE_TYPE, PROMPT_EMAIL,
                             PROMPT_EMAIL_TO_UPDATE, PROMPT_MOBILE, PROMPT_MOBILE_TO_UPDATE, PROMPT_NAME_TO_UPDATE,
                             PROMPT_PASSWORD, PROMPT_PASSWORD_TO_UPDATE, PROMPT_RECYCLER_NAME, PROMPT_ROLE,
                             PROMPT_SEARCH_CUSTOMER_ID, PROMPT_SEARCH_NAME, RECYCLER_MENU, RECYCLER_REGISTERED,
                             SEARCH_CUSTOMER_MENU, SEVEN, SIX, TEN, THIRTEEN, TOTAL_PROFIT_CALCULATED,
                             PROMPT_TOTAL_WASTE, TWO, THREE, FOUR, FIVE, EIGHT, NINE, ELEVEN, TWELVE, WORK_REPORT_ADDED,
                             PROMPT_BIO_WASTE_WEIGHT, PROMPT_NON_BIO_WASTE_WEIGHT, CUSTOMER_REMOVED, UPDATED_CUSTOMER,
                             UPDATE_CUSTOMER_MENU, CHOICE_RANGE_1_3, PROMPT_RAISE_COMPLAINT, BIN_ID,
                             DICT_PASSWORD, ADMIN_REGISTERED, PROMPT_DRIVER_NAME, PROMPT_DRIVER_AREA, DRIVER_REGISTERED,
                             DRIVER_MENU, CHOICE_RANGE_1_6, CHOICE_RANGE_1_4, CHOICE_RANGE_1_7, CHOICE_RANGE_1_5,
                             ADMIN_UNAUTHORIZED, ADMIN_ALREADY_REGISTERED, RECYCLER_ALREADY_REGISTERED,
                             RECYCLER_NOT_REGISTERED, WASTE_TYPE, PROFIT_BIO_WASTE, PROFIT_NON_BIO_WASTE)

from resources.logger_configuration import logger

from util.common_util import continue_operation


def perform_customer_actions():
    """
    Displays the customer menu and processes customer-related actions based on user input.

    The customer menu allows the user to register, view or update their profile, or exit.
    Logs user actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    print(CUSTOMER_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= SEVEN:
        if choice == ONE:
            customer_name = input(PROMPT_CUSTOMER_NAME)
            customer_email = input(PROMPT_EMAIL)
            password = getpass.getpass(PROMPT_PASSWORD)
            mobile_no = input(PROMPT_MOBILE)
            customer_detail = add_customer(customer_name, customer_email,
                                           password, mobile_no)
            if isinstance(customer_detail, dict):
                for customer_field, error_message in customer_detail.items():
                    print(customer_field, " : ", error_message)
            else:
                print(CUSTOMER_REGISTERED.format(customer_detail=customer_detail))
        elif choice == TWO:
            customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
            if check_if_customer_present(customer_id):
                area = input(PROMPT_CUSTOMER_AREA)
                door_no = input(PROMPT_CUSTOMER_DOOR_NO)
                landmark = input(PROMPT_CUSTOMER_LANDMARK, )
                city = input(PROMPT_CUSTOMER_CITY)
                load_type = input(PROMPT_CUSTOMER_LOAD)
                cycle_period = input(PROMPT_CUSTOMER_CYCLE_PERIOD)
                wastage_type = input(PROMPT_CUSTOMER_WASTAGE_TYPE)
                driver_email = is_area_available(area)

                bin_detail = add_bin_detail(area, door_no, landmark, city, load_type, cycle_period,
                                            wastage_type, driver_email, customer_id)
                if isinstance(bin_detail, dict):
                    for bin_field, error_message in bin_detail.items():
                        print(bin_field, error_message)
                else:
                    print(BIN_CREATED_WITH_ID.format(bin_detail=bin_detail))

        elif choice == THREE:
            bin_id = input(PROMPT_BIN_ID)
            if check_if_bin_available(bin_id):
                complaint = input(PROMPT_RAISE_COMPLAINT)
                if not validate_complaint(bin_id, complaint):
                    print(ERROR_COMPLAINT_INVALID)
                else:
                    print(COMPLAINT_REGISTERED.format(bin_id=bin_id))
        elif choice == FOUR:
            bin_id = input(PROMPT_BIN_ID)
            work_reports = check_if_profit_credited(bin_id)
            if work_reports:
                for work_field, work_report in work_reports.items():
                    print(work_field, " : ", work_report)
        elif choice == FIVE:
            email = input(PROMPT_EMAIL)
            customer_id, customer_details = fetch_customer_detail(email)
            print(CUSTOMER_ID, " : ", customer_id)
            for customer_field, customer_detail in customer_details.items():
                print(customer_field, " : ", customer_detail)
        elif choice == SIX:
            customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
            bin_id, bin_details = get_bin_detail(customer_id)
            print(BIN_ID, " : ", bin_id)
            for bin_field, bin_detail in bin_details.items():
                print(bin_field, " : ", bin_detail)
        elif choice == SEVEN:
            return
    else:
        print(CHOICE_RANGE_1_7)
    continue_operation(perform_customer_actions)


def get_customer_detail():
    print(SEARCH_CUSTOMER_MENU)
    search_choice = int(input(PROMPT_CHOICE))
    if ONE <= search_choice <= FOUR:
        if search_choice == ONE:
            name = input(PROMPT_SEARCH_NAME)
            customers = find_customer(name)
            for id_of_customer in customers:
                print("Customer_Id: ", id_of_customer)
                for customer_attribute in customers[id_of_customer]:
                    print(customer_attribute, "-",
                          customers[id_of_customer][customer_attribute])
        elif search_choice == TWO:
            id_of_customer = input(PROMPT_SEARCH_CUSTOMER_ID)
            customer_detail = find_customer(id_of_customer)
            print("Customer_Id: ", id_of_customer)
            for detail in customer_detail:
                print(detail, "-",
                      customer_detail[detail])
        elif search_choice == THREE:
            customers = find_all_customer()
            for id_of_customer, customer_detail in customers:
                if id_of_customer is None:
                    print(NO_CUSTOMER_SIGNED_UP)
                else:
                    print("Customer_Id: ", id_of_customer)
                    for customer_attribute, detail in (customer_detail.items()):
                        print(customer_attribute, "-", detail)
        elif search_choice == FOUR:
            return
    else:
        print(CHOICE_RANGE_1_4)


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
            if update_customer_detail(customer_id, name, DICT_NAME):
                print(UPDATED_CUSTOMER)
        elif choice == TWO:
            email = input(PROMPT_EMAIL_TO_UPDATE)
            if update_customer_detail(customer_id, email, DICT_EMAIL):
                print(UPDATED_CUSTOMER)
        elif choice == THREE:
            password = getpass.getpass(PROMPT_PASSWORD_TO_UPDATE)
            if update_customer_detail(customer_id, password, DICT_PASSWORD):
                print(UPDATED_CUSTOMER)
        elif choice == FOUR:
            mobile = input(PROMPT_MOBILE_TO_UPDATE)
            if update_customer_detail(customer_id, mobile, DICT_MOBILE):
                print(UPDATED_CUSTOMER)
        elif choice == FIVE:
            return
    else:
        print(CHOICE_RANGE_1_5)


def login_admin():
    """
    Prompts for admin email and password, then validates them.

    If the credentials are valid, it calls `manage_admin_tasks()`.
    Otherwise, it prints an unauthorized access message.
    """

    admin_email = input(PROMPT_EMAIL)
    admin_password = getpass.getpass(PROMPT_PASSWORD)
    if validate_admin(admin_email, admin_password):
        manage_admin_tasks()
    else:
        print(ADMIN_UNAUTHORIZED)


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
            if not is_admin_already_registered():
                name = input(PROMPT_ADMIN_NAME)
                email = input(PROMPT_EMAIL)
                password = getpass.getpass(PROMPT_PASSWORD)
                mobile = input(PROMPT_MOBILE)

                admin_detail = add_admin_detail(name, email, password, mobile)
                if isinstance(admin_detail, dict):
                    for admin_field, error_message in admin_detail.items():
                        print(admin_field, error_message)
                else:
                    print(ADMIN_REGISTERED)
            else:
                print(ADMIN_ALREADY_REGISTERED)
        elif choice == TWO:
            name = input(PROMPT_DRIVER_NAME)
            email = input(PROMPT_EMAIL)
            password = getpass.getpass(PROMPT_PASSWORD)
            mobile_no = input(PROMPT_MOBILE)
            area = input(PROMPT_DRIVER_AREA)
            driver_detail = add_driver(name, email, password, mobile_no, area)
            if isinstance(driver_detail, dict):
                for driver_field, error_message in driver_detail.items():
                    print(driver_field, " : ", error_message)
            else:
                print(DRIVER_REGISTERED.format(driver_detail=driver_detail))
        elif choice == THREE:
            get_customer_detail()
        elif choice == FOUR:
            customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
            if delete_customer(customer_id):
                print(CUSTOMER_REMOVED)
        elif choice == FIVE:
            customer_id = input(PROMPT_SEARCH_CUSTOMER_ID)
            if check_customer_present(customer_id):
                update_profile(customer_id)
        elif choice == SIX:
            area = input(PROMPT_DRIVER_AREA)
            driver_detail = find_driver(area)
            for driver_field in driver_detail:
                print(driver_field, ' - ', driver_detail[driver_field])
        elif choice == SEVEN:
            work_reports = fetch_all_work_reports()
            if work_reports is None:
                print(NO_WORK_REPORT)
            else:
                for work_id in work_reports:
                    print("Work Id: ", work_id)
                    for bin_field, bin_detail in work_reports[work_id].items():
                        print(bin_field, ":", bin_detail)
                    print()
        elif choice == EIGHT:
            complaints = get_all_complaints()
            for complaint_id, bin_detail in complaints:
                print("Complaint Id:", complaint_id)
                for bin_attribute, complaint in bin_detail.items():
                    print(bin_attribute, " : ", complaint)
        elif choice == NINE:
            if not check_if_recycler_registered():
                recycler_name = input(PROMPT_RECYCLER_NAME)
                recycler_email = input(PROMPT_EMAIL)
                password = getpass.getpass(PROMPT_PASSWORD)
                mobile_no = input(PROMPT_MOBILE)
                recycler_detail = add_recycler(recycler_name, recycler_email, password, mobile_no)
                if isinstance(recycler_detail, dict):
                    for recycler_field, error_message in recycler_detail.items():
                        print(recycler_field, " : ", error_message)
                else:
                    print(RECYCLER_REGISTERED)
            else:
                print(RECYCLER_ALREADY_REGISTERED)
        elif choice == TEN:
            if check_if_recycler_registered():
                total_waste, bio_waste_weight, non_bio_waste_weight = report_to_recycler()
                print(PROMPT_TOTAL_WASTE, " : ", total_waste, end=" ")
                print(PROMPT_BIO_WASTE_WEIGHT, " : ", bio_waste_weight, end=" ")
                print(PROMPT_NON_BIO_WASTE_WEIGHT, " : ", non_bio_waste_weight)
            else:
                print(RECYCLER_NOT_REGISTERED)
        elif choice == ELEVEN:
            if check_if_recycler_registered():
                wastage = cost_of_wastage_report()
                for wastage_field, wastage_detail in wastage.items():
                    print(wastage_field, " : ", wastage_detail)
            else:
                print(RECYCLER_NOT_REGISTERED)
        elif choice == TWELVE:
            if check_if_recycler_registered():
                total_profit = calculate_total_profit()
                print(TOTAL_PROFIT_CALCULATED.format(total_profit=total_profit))
            else:
                print(RECYCLER_NOT_REGISTERED)
        elif choice == THIRTEEN:
            return
    else:
        print(CHOICE_RANGE_1_13)
    continue_operation(manage_admin_tasks)


def perform_driver_actions():
    """
       Displays a menu for managing driver operations and handles user input.

       The function provides six options:
       1. View driver details by email.
       2. View bins associated with a driver.
       3. Update bin status and record wastage details.
       4. View a driver's work reports.
       5. Check and display driver-related complaints.
       6. Exit the menu.

       Handles invalid input and logs relevant actions and errors.
    """
    print(DRIVER_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= SIX:
        if choice == ONE:
            email = input(PROMPT_EMAIL)
            driver_details = get_driver_detail(email)
            for driver_field, driver_detail in driver_details.items():
                print(driver_field, ":", driver_detail)
        elif choice == TWO:
            email = input(PROMPT_EMAIL)
            if get_driver_detail(email):
                bins = find_bins(email)
                for bin_id, bin_details in bins:
                    print("Bin Id: ", bin_id)
                    for bin_field in bin_details:
                        print(bin_field, " : ", bin_details[bin_field])
                    print()
        elif choice == THREE:
            bin_id = input(PROMPT_BIN_ID)
            bin_details = get_bin_details(bin_id)
            bio_weight, non_bio_weight = collect_details_to_update(bin_details[WASTE_TYPE])
            status = input(PROMPT_BIN_STATUS)
            if not give_work_report(bin_id, bin_details, status, bio_weight, non_bio_weight):
                print(ERROR_INVALID_STATUS)
            else:
                print(WORK_REPORT_ADDED)
        elif choice == FOUR:
            email = input(PROMPT_EMAIL)
            work_reports = fetch_work_reports(email)
            for work_report in work_reports:
                for work_field, work_detail in work_report.items():
                    if work_field not in [PROFIT_BIO_WASTE, PROFIT_NON_BIO_WASTE]:
                        print(work_field, " : ", work_detail)
                print()
        elif choice == FIVE:
            email = input(PROMPT_EMAIL)
            complaints = get_complaints(email)
            for complaint_id, bin_detail in complaints:
                print("Complaint Id:", complaint_id)
                for bin_field, complaint in bin_detail.items():
                    if bin_field != "driver_email":
                        print(bin_field, " : ", complaint)
        elif choice == SIX:
            return
    else:
        print(CHOICE_RANGE_1_6)
    continue_operation(perform_driver_actions)


def handle_recycling():
    """
      Displays a menu for managing recycler operations and processes user input.

      The function provides four options:
      1. View wastage reports if the recycler is registered.
      2. Calculate and log the recycling rate if the recycler is registered.
      3. Exit the menu.

      Handles invalid input and logs relevant actions and errors. Assumes `RECYCLER_MENU`, `PROMPT_CHOICE`,
      and logging constants are defined elsewhere.
      """
    print(RECYCLER_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= THREE:
        if choice == ONE:
            wastage = fetch_wastage_report()
            for wastage_field, wastage_detail in wastage.items():
                print(wastage_field, " : ", wastage_detail)
        elif choice == TWO:
            wastage_reports = rate_calculation()
            for wastage_id in wastage_reports:
                for wastage, wastage_data in wastage_reports[wastage_id].items():
                    print(wastage, " : ", wastage_data)
        elif choice == THREE:
            return
    else:
        print(CHOICE_RANGE_1_3)
    continue_operation(handle_recycling)


def main():
    while True:
        try:
            print(MAIN_MENU)
            role = int(input(PROMPT_ROLE))
            if ONE <= role <= FIVE:
                if role == ONE:
                    perform_customer_actions()
                elif role == TWO:
                    login_admin()
                elif role == THREE:
                    perform_driver_actions()
                elif role == FOUR:
                    handle_recycling()
                elif role == FIVE:
                    logger.info(LOG_APPLICATION_END)
                    break
            else:
                print(CHOICE_RANGE_1_5)
        except ValueError as e:
            logger.error(VALUE_ERROR_IN_CUSTOMER_MENU.format(e=e), exc_info=True)
        except UserAlreadyExistsError as e:
            logger.error(e, exc_info=True)
        except ResourceNotFoundException as e:
            logger.warning(e, exc_info=True)
        except GarbageCollectorException as e:
            logger.error(e, exc_info=True)
        except ResourceAlreadyExistsException as e:
            logger.warning(e, exc_info=True)


if __name__ == "__main__":
    load_admins()
    main()
