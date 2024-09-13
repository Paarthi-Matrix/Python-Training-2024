from service.recycler import (
    get_wastage_report,
    calculate_rate
)


def fetch_wastage_report():
    """
    Retrieve the report of wastage.

    This function calls the service to get the wastage report, which includes details
    about the quantity and type of waste collected.

    Returns:
        dict: The wastage report, including details such as types and amounts of waste.
    """
    return get_wastage_report()


def rate_calculation():
    """
    Calculate the rate based on the wastage data.

    This function invokes the service to calculate the rate, which may be
    based on factors such as the type and amount of waste collected.

    Returns:
        dict: work report after calculating the rate for wastage
    """
    return calculate_rate()
