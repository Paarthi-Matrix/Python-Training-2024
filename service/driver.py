import uuid
from datetime import datetime

from exception.custom_exception import (
    ResourceNotFoundException,
    GarbageCollectorException, ResourceAlreadyExistsException
)

from helper.constant import (
    DRIVER_REGISTERED,
    LOG_USER_ALREADY_REGISTERED_EMAIL,
    LOG_USER_ALREADY_REGISTERED_PASSWORD,
    LOG_USER_ALREADY_REGISTERED_AREA,
    NO_DRIVER,
    PROMPT_BIN_COMPLETED, PROMPT_BIN_INCOMPLETE,
    WASTAGE_WEIGHT_CALCULATED, LOG_BIN_UPDATED, DICT_EMAIL, PASSWORD, AREA, BIN_ID, BIO_WASTE, NON_BIO_WASTE, STATUS,
    DATE_TIME, HUNDRED, TEN, TWENTY, RECYCLED, PROFIT_BIO_WASTE, PROFIT_NON_BIO_WASTE, NO, YES
)

from resources.logger_configuration import logger

from service.recycler import add_wastage_report, is_wastage_report_added

driver_details = {}
work_reports = {}


def add_driver(name, email, password, mobile_no, area):
    """
    Adds a new driver with the provided details and generates a unique driver ID.

    Args:
        name (str): The name of the driver.
        email (str): The email address of the driver.
        password (str): The password for the driver's account.
        mobile_no (str): The mobile number of the driver.
        area (str): The area where the driver operates.
    """
    drivers = {
        "name": name,
        "email": email,
        "password": password,
        "mobile_no": mobile_no,
        "area": area
    }
    driver_id = str(uuid.uuid4())
    driver_details[driver_id] = drivers
    logger.info(DRIVER_REGISTERED.format(driver_detail=driver_id))
    return driver_id


def register_driver(name, email, password, mobile_no, area):
    """
    Registers a driver if the email, password, or area are not already in use.

    Args:
        name (str): The name of the driver.
        email (str): The email address of the driver.
        password (str): The password for the driver's account.
        mobile_no (str): The mobile number of the driver.
        area (str): The area where the driver operates.
    """
    for driver_id in driver_details:
        driver = driver_details.get(driver_id)
        if driver[DICT_EMAIL] == email:
            logger.warning(LOG_USER_ALREADY_REGISTERED_EMAIL.format(email=email))
            break
        elif driver[PASSWORD] == password:
            logger.warning(LOG_USER_ALREADY_REGISTERED_PASSWORD.format(password=password))
            break
        elif driver[AREA] == area:
            logger.warning(LOG_USER_ALREADY_REGISTERED_AREA.format(area=area))
            break
        else:
            return add_driver(name, email, password, mobile_no, area)

    else:
        return add_driver(name, email, password, mobile_no, area)


def search_driver(area):
    """
    Searches for a driver in the specified area.

    Args:
        area (str): The area to search for a driver.

    Returns:
        dict: The details of the driver if found; otherwise, None.
    """
    for driver_id in driver_details:
        if driver_details[driver_id][AREA] == area:
            return driver_details[driver_id]
    logger.warning(NO_DRIVER.format(area=area))
    raise ResourceNotFoundException(NO_DRIVER.format(area=area))


def get_driver_email(area):
    """
    Retrieves the email address of a driver assigned to a specified area.

    Args:
        area (str): The area to search for a driver.

    Returns:
        str: The email address of the driver.

    Raises:
        ResourceNotFoundException: If no driver is found in the specified area.
    """
    for driver_id in driver_details:
        if driver_details[driver_id][AREA].lower() == area.lower():
            return driver_details[driver_id][DICT_EMAIL]
    raise ResourceNotFoundException("No driver assigned to this area: " + area)


def is_driver_available(email):
    """
    Checks if a driver with the specified email is available and retrieves their details.

    Args:
        email (str): The email address of the driver.

    Returns:
        dict: Details of the driver if found.

    Raises:
        ResourceNotFoundException: If no driver is found with the specified email.
    """
    for driver_id in driver_details:
        if driver_details[driver_id][DICT_EMAIL] == email:
            return driver_details[driver_id]
    raise ResourceNotFoundException("No driver found by this email: " + email)


def add_work_report(driver_email, status, bio_weight, non_bio_weight, bin_id, area):
    """
    Adds or updates a work report for a driver and bin, including waste details and status.

    Args:
        driver_email (str): The email address of the driver.
        status (str): The status of the work (e.g., "completed").
        bio_weight (float): The weight of biodegradable waste.
        non_bio_weight (float): The weight of non-biodegradable waste.
        bin_id (str): The ID of the bin.
        area (str): The area where the bin is located.

    Updates:
        If a work report for the given bin ID already exists, it updates the existing report; otherwise, it creates a new report.
    """
    updated_bin_detail = {
        "email": driver_email,
        "bin_id": bin_id,
        "status": status,
        "bio-weight": bio_weight,
        "non_bio-weight": non_bio_weight,
        "profit_bio-weight": 0,
        "profit_non_bio-weight": 0,
        "area": area,
        "date_time": datetime.now(),
        "Recycled": "No"
    }
    # To add the wastage weights to the previous weights if it is not recycled yet
    for work_id in work_reports:
        if work_reports[work_id][BIN_ID] == bin_id:
            updated_bin_detail[BIO_WASTE] = work_reports[work_id][BIO_WASTE] + bio_weight
            updated_bin_detail[NON_BIO_WASTE] = work_reports[work_id][NON_BIO_WASTE] + non_bio_weight
            work_reports[work_id] = updated_bin_detail
            break
    else:
        work_reports[str(uuid.uuid4())] = updated_bin_detail
    logger.info(LOG_BIN_UPDATED)
    return True


def get_all_work_reports():
    """
    Retrieves all work reports.

    Returns:
        dict: A dictionary of work reports if any exist; otherwise, None.
    """
    if len(work_reports) == 0:
        return None
    return work_reports


def is_status_completed(bin_id):
    """
    Checks if the status of a specified bin ID is marked as completed and if it was completed today.

    Args:
        bin_id (str): The ID of the bin to check.

    Returns:
        bool: True if the bin status is completed and the report date is today; False otherwise.
    """
    for work_id in work_reports:
        if work_reports[work_id][BIN_ID] == bin_id:
            if work_reports[work_id][STATUS] == PROMPT_BIN_COMPLETED:
                # To check if the status is completed and the work report date is today's date
                return work_reports[work_id][DATE_TIME].date() == datetime.today().date(), PROMPT_BIN_COMPLETED
            else:
                # Work report status is incomplete
                return False, PROMPT_BIN_INCOMPLETE
    else:
        # No work reports added yet
        return False, None


def get_work_reports(email):
    """
    Yields work reports associated with a specified email address.

    Args:
        email (str): The email address of the driver.

    Yields:
        dict: Details of the work reports associated with the email address.
    """
    found = False
    for work_id in work_reports:
        if work_reports[work_id][DICT_EMAIL] == email:
            found = True
            yield work_reports[work_id]

    if not found:
        raise ResourceNotFoundException("No work reports found for driver whose email Id: " + email)


def is_valid_complaint(bin_id):
    """
    Validates if there is a valid complaint for the given bin ID based on the date and status of the work report.

    Args:
        bin_id (str): The ID of the bin to check.

    Returns:
        bool: True if the complaint is valid; False otherwise.
    """
    today = datetime.today().date()
    for work_id, report in work_reports.items():
        bin_match = report[BIN_ID] == bin_id
        date_match = report[DATE_TIME].date() == today
        time_match = report[DATE_TIME].hour >= 12
        status_match = report[STATUS].upper() == PROMPT_BIN_INCOMPLETE

        if not bin_match:
            return True

        if date_match:
            # To check if the bin report is incomplete and time is above 12 afternoon
            if time_match and status_match:
                return True
            elif report[STATUS].upper() == PROMPT_BIN_COMPLETED:
                raise GarbageCollectorException("Work has already been completed for today where Bin Id: " + bin_id)
            else:
                raise GarbageCollectorException("Unable to raise complaint before 12 Noon for bin Id " + bin_id)
    else:
        return True


def check_wastage():
    """
    Checks the total amount of wastage and processes it if both bio and non-bio waste are above 100 units.

    Returns:
        tuple: Total waste, bio waste weight, and non-bio waste weight if conditions are met.

    Raises:
        GarbageCollectorException: If the total wastage is less than 100.
        ResourceNotFoundException: If no work reports are found.
    """
    bio_waste_weight, non_bio_waste_weight = 0, 0
    if len(work_reports) != 0:
        for work_id in work_reports:
            if work_reports[work_id][RECYCLED] == NO:
                bio_waste_weight += work_reports[work_id][BIO_WASTE]
                non_bio_waste_weight += work_reports[work_id][NON_BIO_WASTE]

        if bio_waste_weight >= HUNDRED and non_bio_waste_weight >= HUNDRED:
            total_waste = bio_waste_weight + non_bio_waste_weight
            if is_wastage_report_added():
                add_wastage_report(bio_waste_weight, non_bio_waste_weight, total_waste)
            else:
                raise ResourceAlreadyExistsException("Wastage report already send to the Recycler for today")
            logger.info(
                WASTAGE_WEIGHT_CALCULATED.format(total_waste, bio_waste_weight, non_bio_waste_weight))
            return total_waste, bio_waste_weight, non_bio_waste_weight
        elif bio_waste_weight == 0 and non_bio_waste_weight == 0:
            # If the work report given incomplete by the driver
            raise GarbageCollectorException("Work reports are Incomplete..Unable to process the weightage of Wastage")
        raise GarbageCollectorException("Total wastage less than 100 to process")
    else:
        raise ResourceNotFoundException("No work report Found")


def calculate_wastage_profit():
    """
    Calculates and updates the profit from recycling based on the waste reports. Marks the reports as recycled.

    Returns:
        float: The total profit from recycling.

    Updates:
        The profit details for each work report and marks them as recycled.
    """
    customer_profit = 0
    for work_id in work_reports:
        if work_reports[work_id][RECYCLED] == NO:
            bio_degradable_profit = work_reports[work_id][BIO_WASTE] * TEN
            non_bio_degradable_profit = work_reports[work_id][NON_BIO_WASTE] * TWENTY
            work_reports[work_id][PROFIT_BIO_WASTE] = bio_degradable_profit
            work_reports[work_id][PROFIT_NON_BIO_WASTE] = non_bio_degradable_profit
            work_reports[work_id][RECYCLED] = YES
            work_reports[work_id][BIO_WASTE] = 0
            work_reports[work_id][NON_BIO_WASTE] = 0
            customer_profit += bio_degradable_profit + non_bio_degradable_profit
        else:
            raise GarbageCollectorException("Profit has already been calculated and credited to respective Bin owners")
    return customer_profit


def check_profit(bin_id):
    """
    Retrieves the profit details for a specified bin ID.

    Args:
        bin_id (str): The ID of the bin to check.

    Returns:
        dict: Profit details for the specified bin ID.

    Raises:
        ResourceNotFoundException: If no profit details are found for the specified bin ID.
    """
    if len(work_reports) > 0:
        for work_id in work_reports:
            if work_reports[work_id][BIN_ID] == bin_id:
                return work_reports[work_id]
    else:
        raise ResourceNotFoundException("Profit not yet calculated")
