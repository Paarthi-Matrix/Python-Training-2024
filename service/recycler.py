import uuid
from datetime import datetime
from exception.custom_exception import ResourceNotFoundException, GarbageCollectorException

recycler_details = {}
wastage_reports = {}


def register_recycler(recycler_name, recycler_email, password, mobile_no):
    """
    Registers a new recycler with the provided details and generates a unique recycler ID.

    Args:
        recycler_name (str): The name of the recycler.
        recycler_email (str): The email address of the recycler.
        password (str): The password for the recycler's account.
        mobile_no (str): The mobile number of the recycler.

    Returns:
        str: A unique identifier for the registered recycler.
    """
    recycler_id = str(uuid.uuid4())
    recycler_detail = {
        "name": recycler_name,
        "email": recycler_email,
        "password": password,
        "mobile_no": mobile_no
    }
    recycler_details[recycler_id] = recycler_detail
    return recycler_id


def is_recycler_registered():
    """
    Checks if there is at least one recycler registered.

    Returns:
        bool: True if more than one recycler is registered; False otherwise.
    """
    if len(recycler_details) >= 1:
        return True
    return False


def is_wastage_report_added():
    today = datetime.today().date()
    if len(wastage_reports) != 0:
        for wastage_id in wastage_reports:
            report = wastage_reports[wastage_id]
            recycled = report.get("Recycled")
            date_time = report.get("date_time")

            if recycled == 'No' and date_time and date_time.date() != today:
                return True
        return False
    else:
        return True


def add_wastage_report(bio_waste_weight, non_bio_waste_weight, total_waste):
    """
    Adds a new wastage report with the given waste details.

    Args:
        bio_waste_weight (float): The weight of biodegradable waste.
        non_bio_waste_weight (float): The weight of non-biodegradable waste.
        total_waste (float): The total weight of waste.

    The function creates a report with cost and profit details set to zero and records the current date and time.
    """
    for wastage_id in wastage_reports:
        if wastage_reports[wastage_id]["Recycled"] == "No":
            bio_waste_weight += wastage_reports[wastage_id]["bio_waste_weight"]
            non_bio_waste_weight += wastage_reports[wastage_id]["non_bio_waste_weight"]
            total_waste += wastage_reports[wastage_id]["total_waste"]

    garbage_collections = {
        "bio_waste_weight": bio_waste_weight,
        "non_bio_waste_weight": non_bio_waste_weight,
        "total_waste": total_waste,
        "cost_of_bio_degradable": 0,
        "cost_of_non_bio_degradable": 0,
        "total_profit": 0,
        "Recycled": "No",
        "date_time": datetime.now()
    }
    wastage_id = str(uuid.uuid4())
    wastage_reports[wastage_id] = garbage_collections


def get_wastage_report():
    """
    Retrieves wastage reports that have not been recycled.

    Yields:
        dict: Details of wastage reports marked as not recycled.

    Raises:
        ResourceNotFoundException: If no wastage reports are found.
    """
    if len(wastage_reports) != 0:
        for wastage_id in wastage_reports:
            if is_wastage_report_valid_date(wastage_reports[wastage_id]["date_time"]):
                return wastage_reports[wastage_id]
            else:
                raise ResourceNotFoundException("No wastage report found for today")
    else:
        raise ResourceNotFoundException("No wastage report found")


def calculate_rate():
    """
    Calculates and updates the cost and profit for wastage reports that have not been recycled.

    The function updates each report's cost of biodegradable and non-biodegradable waste and the total profit,
    then marks the report as recycled.

    Raises:
        ResourceNotFoundException: If no wastage reports are found.
    """
    if len(wastage_reports) != 0:
        for wastage_id in wastage_reports:
            if (wastage_reports[wastage_id]["Recycled"] == "No" and
                    is_wastage_report_valid_date(wastage_reports[wastage_id]["date_time"])):
                wastage_reports[wastage_id]["cost_of_bio_degradable"] = wastage_reports[wastage_id][
                                                                            "bio_waste_weight"] * 50
                wastage_reports[wastage_id]["cost_of_non_bio_degradable"] = wastage_reports[wastage_id][
                                                                                "non_bio_waste_weight"] * 100
                wastage_reports[wastage_id]["total_profit"] = (wastage_reports[wastage_id][
                                                                   "bio_waste_weight"] * 50) + (
                                                                      wastage_reports[wastage_id][
                                                                          "non_bio_waste_weight"] * 100)
                wastage_reports[wastage_id]["Recycled"] = "Yes"
                return wastage_reports
            else:
                raise GarbageCollectorException("Rate has already been calculated on Garbage")
    else:
        raise ResourceNotFoundException("No wastage report found")


def get_cost_of_garbage():
    """
    Retrieves wastage reports that have been recycled.

    Yields:
        dict: Details of wastage reports marked as recycled.

    Raises:
        ResourceNotFoundException: If no recycled wastage reports are found.
    """
    if len(wastage_reports) != 0:
        for wastage_id in wastage_reports:
            if (wastage_reports[wastage_id]["Recycled"] == "Yes" and
                    is_wastage_report_valid_date(wastage_reports[wastage_id]["date_time"])):
                return wastage_reports[wastage_id]
            else:
                raise GarbageCollectorException("Garbage not yet recycled by the Recycler")
    else:
        raise ResourceNotFoundException("No wastage report found")


def calculate_profit():
    """
    Updates the total profit for recycled wastage reports by deducting customer profit.

    The function uses an external service to calculate and adjust the profit for each recycled report.

    Raises:
        ResourceNotFoundException: If no wastage reports are found.
    """

    from service.driver import calculate_wastage_profit
    if len(wastage_reports) != 0:
        for wastage_id in wastage_reports:
            if (wastage_reports[wastage_id]["Recycled"] == "Yes" and
                    is_wastage_report_valid_date(wastage_reports[wastage_id]["date_time"])):
                customer_profit = calculate_wastage_profit()
                wastage_reports[wastage_id]["total_profit"] = (
                        wastage_reports[wastage_id]["total_profit"] - customer_profit)
            else:
                raise GarbageCollectorException("Garbage not yet recycled by the Recycler")
    else:
        raise ResourceNotFoundException("No wastage report found")


def get_calculated_report():
    if len(wastage_reports) != 0:
        for wastage_id in wastage_reports:
            if wastage_reports[wastage_id]["Recycled"] == "Yes":
                return wastage_reports[wastage_id]
            else:
                raise GarbageCollectorException("Wastage report not yet recycled by Recycler")
    raise GarbageCollectorException("No wastage reports added yet")


def view_calculated_report(wastage_report):
    for wastage_id in wastage_report:
        for wastage, wastage_data in wastage_report[wastage_id].items():
            print(wastage, " : ", wastage_data)


def is_wastage_report_valid_date(report_date):
    today = datetime.today().date()
    return report_date.date() == today
