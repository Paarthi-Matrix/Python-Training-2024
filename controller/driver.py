from helper.constant import (
    ERROR_INVALID_STATUS, ERROR_INVALID_WASTAGE,
    LOG_BIN_STATUS_COMPLETED, LOG_BIN_UPDATED, LOG_INVALID_WEIGHT,
    LOG_VALUE_ERROR_IN_ADMIN_MENU, LOG_WORK_REPORT_INCOMPLETE,
    PROMPT_BIO_DEGRADABLE, PROMPT_BIO_DEGRADABLE_WASTE, PROMPT_BIN_COMPLETED,
    PROMPT_BIN_INCOMPLETE, PROMPT_NON_BIO_DEGRADABLE, PROMPT_NON_BIO_DEGRADABLE_WASTE,
    PROMPT_WASTAGE_TYPE
)

from resources.logger_configuration import logger

from service.customer import (
    change_complaint_status, check_complaints, get_bin_wastage_type,
    get_bins, is_complaint_raised
)

from service.driver import (
    add_work_report, get_work_reports, is_driver_available, is_status_completed
)

from validator.validation import (
    check_valid_input, is_valid_status
)


def is_valid_weight(weight):
    """
    Validate that the weight is within the acceptable range.

    Args:
        weight (int): The weight to be validated.

    Returns:
        bool: True if the weight is between 1 and 100 kg inclusive; otherwise, False.
    """
    return 1 <= weight <= 100


def get_weight_input(prompt):
    """
    Prompt the user for a weight input and validate it.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        int or None: The valid weight input from the user if it is within the
        acceptable range; otherwise, logs a warning and returns None.
    """
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
    Collect and return weights based on the wastage type specified.

    Args:
        wastage_type (str): The type of wastage ('Bio-degradable', 'Non Bio-degradable', or 'Both').

    Returns:
        tuple: A tuple containing the weights for Bio-degradable and Non Bio-degradable waste.
               If wastage_type is 'Both', both weights are provided. If not, one of the weights is None.
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
        print(ERROR_INVALID_WASTAGE)
        return None, None


def get_driver_detail(email):
    """
    Check if a driver with the given email is available.

    Args:
        email (str): The email address of the driver.

    Returns:
        bool: True if the driver is available; otherwise, False.
    """
    return is_driver_available(email)


def find_bins(email):
    """
    Retrieve the bins associated with the specified driver's email.

    Args:
        email (str): The email address of the driver.

    Returns:
        list: A list of bins associated with the driver.
    """
    return get_bins(email)


def give_work_report(bin_id, bin_details, status, bio_weight, non_bio_weight):
    """
    Submit a work report for a bin, including its status and waste weights.

    Args:
        bin_id (str): The unique identifier of the bin.
        bin_details (dict): A dictionary containing details of the bin, including 'driver_email' and 'area'.
        status (str): The status of the bin (e.g., 'Completed', 'Incomplete').
        bio_weight (int or None): The weight of Bio-degradable waste; None if not applicable.
        non_bio_weight (int or None): The weight of Non Bio-degradable waste; None if not applicable.

    Returns:
        bool: True if the work report is successfully added and the complaint
        status is updated if needed; otherwise, False.
    """
    if check_valid_input(status, is_valid_status):
        is_already_completed, is_already_incomplete = is_status_completed(bin_id)
        if is_already_completed:
            logger.warning(LOG_BIN_STATUS_COMPLETED.format(bin_id=bin_id))
        elif is_already_incomplete == PROMPT_BIN_INCOMPLETE == status:
            logger.info(LOG_WORK_REPORT_INCOMPLETE.format(bin_id=bin_id))
        else:
            if status.upper() == PROMPT_BIN_COMPLETED:
                if bio_weight is None:
                    bio_weight = 0
                if non_bio_weight is None:
                    non_bio_weight = 0
            else:
                bio_weight, non_bio_weight = 0, 0
            if add_work_report(bin_details['driver_email'], status, bio_weight, non_bio_weight, bin_id,
                               bin_details['area']):
                if is_complaint_raised(bin_id):
                    change_complaint_status(PROMPT_BIN_COMPLETED, bin_id)
                return True
            logger.info(LOG_BIN_UPDATED.format(bin_id=bin_id))
    else:
        logger.warning(ERROR_INVALID_STATUS)
        return False


def fetch_work_reports(email):
    """
    Retrieve all work reports associated with the specified driver's email.

    Args:
        email (str): The email address of the driver.

    Returns:
        list: A list of work reports associated with the driver.
    """
    if is_driver_available(email):
        return get_work_reports(email)


def get_complaints(email):
    """
    Retrieve all complaints associated with the specified driver's email.

    Args:
        email (str): The email address of the driver.

    Returns:
        list: A list of complaints associated with the driver.
    """
    if is_driver_available(email):
        return check_complaints(email)


def get_bin_details(bin_id):
    """
    Retrieve the details of the bin, including its wastage type, based on its ID.

    Args:
        bin_id (str): The unique identifier of the bin.

    Returns:
        dict: The details of the bin, including its wastage type.
    """
    return get_bin_wastage_type(bin_id)
