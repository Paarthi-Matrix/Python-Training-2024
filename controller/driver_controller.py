from constant.logger_constant import (
    LOG_VALUE_ERROR_IN_ADMIN_MENU,
    LOG_REDIRECTING_HOME,
    LOG_ERROR_INVALID_WASTAGE,
    LOG_ERROR_INVALID_STATUS,
    LOG_BIN_UPDATED,
    LOG_BIN_STATUS_COMPLETED,
    LOG_ERROR_CHOICE_RANGE_1_6,
    LOG_INVALID_WEIGHT,
    LOG_WORK_REPORT_INCOMPLETE
)

from constant.menu_constant import (
    DRIVER_MENU
)

from constant.prompt_constant import (
    PROMPT_EMAIL,
    PROMPT_CHOICE,
    PROMPT_BIN_ID,
    PROMPT_BIN_STATUS,
    PROMPT_WASTAGE_TYPE,
    PROMPT_BIO_DEGRADABLE,
    PROMPT_NON_BIO_DEGRADABLE,
    PROMPT_BIO_DEGRADABLE_WASTE,
    PROMPT_NON_BIO_DEGRADABLE_WASTE,
    PROMPT_BIN_COMPLETED,
    PROMPT_BIN_INCOMPLETE
)

from resources.logger_configuration import logger

from service.customer_service import (
    get_bins,
    get_bin_wastage_type,
    check_complaints,
    change_complaint_status,
    is_complaint_raised
)

from service.driver_service import (
    is_driver_available,
    add_work_report,
    is_status_completed,
    get_work_reports,

)

from util.validation import (
    is_valid_status,
    get_valid_input
)

from exception.custom_exception import (
    ResourceNotFoundException
)


def update_status():
    """Get valid status input from the user."""
    status = get_valid_input(
        PROMPT_BIN_STATUS,
        is_valid_status,
        LOG_ERROR_INVALID_STATUS
    )
    return status


def is_valid_weight(weight):
    """Validate that the weight is not above 100 kg."""
    return 1 <= weight <= 100


def get_weight_input(prompt):
    """Get valid weight input from the user."""
    while True:
        try:
            weight = int(input(prompt))
            if is_valid_weight(weight):
                return weight
            else:
                logger.warning(LOG_INVALID_WEIGHT)
        except ValueError:
            logger.error(LOG_VALUE_ERROR_IN_ADMIN_MENU)


def collect_details_to_update(wastage_type):
    """
    Collect weights for the specified wastage type.
    If wastage type is 'Both', prompt for both Bio-degradable and Non Bio-degradable weights.
    """
    if wastage_type.upper() == PROMPT_BIO_DEGRADABLE:
        bio_degradable_weight = get_weight_input(PROMPT_BIO_DEGRADABLE_WASTE)
        return bio_degradable_weight, None

    elif wastage_type.upper() == PROMPT_NON_BIO_DEGRADABLE:
        non_bio_degradable_weight = get_weight_input(PROMPT_NON_BIO_DEGRADABLE_WASTE)
        return None, non_bio_degradable_weight

    elif wastage_type.upper() == PROMPT_WASTAGE_TYPE:
        bio_degradable_weight = get_weight_input(PROMPT_BIO_DEGRADABLE_WASTE)
        non_bio_degradable_weight = get_weight_input(PROMPT_NON_BIO_DEGRADABLE_WASTE)
        return bio_degradable_weight, non_bio_degradable_weight

    else:
        print(LOG_ERROR_INVALID_WASTAGE)
        return None, None


def driver():
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
    while True:
        try:
            print(DRIVER_MENU)
            choice = int(input(PROMPT_CHOICE))
            if choice >= 1 and choice <= 6:
                if choice == 1:
                    email = input(PROMPT_EMAIL)
                    driver_details = is_driver_available(email)
                    for driver_attribute, detail in driver_details.items():
                        print(driver_attribute, ":", detail)
                elif choice == 2:
                    email = input(PROMPT_EMAIL)
                    if is_driver_available(email):
                        bins = get_bins(email)
                        for bin_id, bin_details in bins:
                            print("Bin Id: ", bin_id)
                            for bin_attribute in bin_details:
                                print(bin_attribute, " : ", bin_details[bin_attribute])
                            print()
                elif choice == 3:
                    bin_id = input(PROMPT_BIN_ID)
                    bin_details = get_bin_wastage_type(bin_id)
                    status = update_status()
                    is_already_completed, is_already_incomplete = is_status_completed(bin_id)
                    if is_already_completed:
                        logger.warning(LOG_BIN_STATUS_COMPLETED.format(bin_id=bin_id))
                    elif is_already_incomplete == PROMPT_BIN_INCOMPLETE == status:
                        logger.info(LOG_WORK_REPORT_INCOMPLETE.format(bin_id=bin_id))
                    else:
                        if status.upper() == PROMPT_BIN_COMPLETED:
                            bio_weight, non_bio_weight = collect_details_to_update(bin_details["wastage_type"])
                            if bio_weight is None:
                                bio_weight = 0
                            if non_bio_weight is None:
                                non_bio_weight = 0
                        else:
                            bio_weight, non_bio_weight = 0, 0
                        add_work_report(bin_details['driver_email'], status, bio_weight, non_bio_weight, bin_id,
                                        bin_details['area'])
                        if is_complaint_raised(bin_id):
                            change_complaint_status(PROMPT_BIN_COMPLETED, bin_id)
                        logger.info(LOG_BIN_UPDATED.format(bin_id=bin_id))
                elif choice == 4:
                    email = input(PROMPT_EMAIL)
                    if is_driver_available(email):
                        work_reports = get_work_reports(email)
                        for work_report in work_reports:
                            for key, value in work_report.items():
                                if key not in ["profit_bio-weight", "profit_non_bio-weight"]:
                                    print(key, " : ", value)
                            print()
                elif choice == 5:
                    email = input(PROMPT_EMAIL)
                    if is_driver_available(email):
                        complaints = check_complaints(email)
                        for complaint_id, bin_detail in complaints:
                            print("Complaint Id:", complaint_id)
                            for bin_attribute, complaint in bin_detail.items():
                                if bin_attribute != "driver_email":
                                    print(bin_attribute, " : ", complaint)
                elif choice == 6:
                    logger.info(LOG_REDIRECTING_HOME)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_6)
        except ValueError as e:
            logger.error(LOG_VALUE_ERROR_IN_ADMIN_MENU.format(e=e))
        except ResourceNotFoundException as e:
            logger.error(e)
