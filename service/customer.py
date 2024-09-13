import uuid
from datetime import datetime

from exception.custom_exception import (
    ResourceNotFoundException,
    UserAlreadyExistsError
)

from helper.constant import (
    BIN_CREATED_WITH_ID,
    COMPLAINT_REGISTERED,
    CUSTOMER_DELETED_WITH_ID,
    LOG_CUSTOMER_REGISTERED_WITH_ID,
    LOG_CUSTOMER_UPDATED, IS_DELETED, DICT_EMAIL, DICT_NAME, CUSTOMER_ID, DRIVER_EMAIL, DOOR_NO, AREA, BIN_ID,
    STATUS, COMPLAINT_STATUS
)

from resources.logger_configuration import logger


# Dictionary to store customer details by their ID
customer_details = {}
bins = {}
complaints = {}


def get_all_customer():
    """
    Generator function that yields customer details from the customer details dictionary.

    If there are no customers in the dictionary, it yields None.

    Yields:
    - dict: A dictionary containing the details of each customer.
    - None: If the customer details dictionary is empty.
    """
    if len(customer_details) == 0:
        yield None, None
    else:
        is_customer_available = False
        for customer_id in customer_details:
            if not customer_details[customer_id][IS_DELETED]:
                is_customer_available = True
                yield customer_id, customer_details[customer_id]
        if not is_customer_available:
            yield None, None


def register_customer(name, email, password, mobile_no):
    """
    Registers a new customer and returns a unique customer ID.

    Parameters:
    - name: Customer's name
    - email: Customer's email
    - password: Customer's password
    - mobile_no: Customer's mobile number

    Returns:
    - customer_id: The unique ID assigned to the customer
    """
    if len(customer_details) != 0:
        for customer_id in customer_details:
            if customer_details[customer_id][DICT_EMAIL] == email:
                raise UserAlreadyExistsError("Already registered user with email: " + email)

    customers = {
        "name": name,
        "email": email,
        "password": password,
        "mobile_no": mobile_no,
        "is_deleted": False
    }
    customer_id = str(uuid.uuid4())
    customer_details[customer_id] = customers
    logger.info(LOG_CUSTOMER_REGISTERED_WITH_ID.format(customer_detail=customer_id))
    return customer_id


def search_customer(customer_identifier):
    """
    Retrieves and prints the details of a customer by their ID.

    Parameters:
    - cus_id: The unique ID of the customer
    """
    from validator.validation import is_valid_name
    if is_valid_name(customer_identifier):
        customers_by_name = {}
        for customer_id in customer_details:
            detail = customer_details[customer_id]
            if not detail[IS_DELETED]:
                customer_name = detail[DICT_NAME]
                if customer_name.lower().__contains__(customer_identifier
                                                              .lower()):
                    customers_by_name[customer_id] = detail
        if len(customers_by_name) == 0:
            raise ResourceNotFoundException("No customer found by this name: " + customer_identifier)
        else:
            return customers_by_name
    else:
        if is_customer_present(customer_identifier):
            return customer_details.get(customer_identifier)


def remove_customer(customer_id):
    """
    Removes a customer from the customer details dictionary.

    Parameters:
    - customer_id: The unique ID of the customer to be removed.

    Returns:
    - None: If the customer is successfully removed.
    - customer_id: If the customer ID does not exist in the dictionary.
    """
    if is_customer_present(customer_id):
        customer_details.get(customer_id)[IS_DELETED] = True
        logger.info(CUSTOMER_DELETED_WITH_ID.format(customer_id=customer_id))
        return None


def update_customer(customer_id, detail_to_update, to_update):
    """
    Updates a specific detail of a customer in the customer details dictionary.

    Parameters:
    - customer_id: The unique ID of the customer to be updated.
    - detail_to_update: The new value for the specified detail.
    - to_update: The key representing the detail to be updated (e.g., 'name', 'email').

    Returns:
    - customer_id: The unique ID of the customer that was updated.
    """
    if to_update != 'name':
        for id_of_customer in customer_details:
            if customer_details[id_of_customer][to_update] == detail_to_update:
                raise UserAlreadyExistsError("Already registered user with this data: " + detail_to_update)

    customer = customer_details[customer_id]
    customer[to_update] = detail_to_update
    logger.info(LOG_CUSTOMER_UPDATED.format(customer_id=customer_id))
    return True


def is_customer_present(customer_id):
    """
    Checks if a customer exists in the customer details dictionary.

    Parameters:
    - customer_id: The unique ID of the customer to be checked.

    Returns:
    - True: If the customer exists in the dictionary.
    - False: If the customer does not exist in the dictionary.
    """
    if (customer_id in customer_details and not
    customer_details[customer_id][IS_DELETED]):
        return True
    raise ResourceNotFoundException("No customer found by this Id: " + customer_id)


def is_bin_created_for_customer(customer_id):
    """
    Checks if a bin has been created for the specified customer ID.

    Args:
        customer_id (str): The ID of the customer.

    Returns:
        bool: True if a bin exists for the customer ID; False otherwise.
    """
    for bin_id in bins:
        if bins[bin_id][CUSTOMER_ID] == customer_id:
            return True
    return False


def create_bin(area, door_no, landmark, city, load_type,
               cycle_period, wastage_type, driver_email, customer_id):
    """
    Creates a new bin with the provided details and assigns it a unique ID.

    Args:
        area (str): The area where the bin is located.
        door_no (str): The door number associated with the bin.
        locality (str): The locality where the bin is located.
        landmark (str): A landmark near the bin's location.
        city (str): The city where the bin is located.
        load_type (str): The type of load the bin will handle.
        cycle_period (str): The cycle period for waste collection.
        wastage_type (str): The type of waste the bin will collect.
        driver_email (str): The email of the driver assigned to the bin.
        customer_id (str): The ID of the customer associated with the bin.
    """
    customer_bin = {
        "area": area,
        "door_no": door_no,
        "landmark": landmark,
        "city": city,
        "load_type": load_type,
        "cycle_period": cycle_period,
        "wastage_type": wastage_type,
        "customer_id": customer_id,
        "driver_email": driver_email
    }
    bin_id = str(uuid.uuid4())
    bins[bin_id] = customer_bin
    logger.info(BIN_CREATED_WITH_ID.format(bin_detail=bin_id))
    return bin_id


def get_bins(email):
    """
    Retrieves bins assigned to a driver with the specified email address.

    Args:
        email (str): The email address of the driver.

    Yields:
        tuple: The ID and details of each bin assigned to the driver.

    Raises:
        ResourceNotFoundException: If no bins are assigned to the driver with the specified email.
    """
    is_driver_present = False
    for bin_id in bins:
        if bins[bin_id][DRIVER_EMAIL] == email:
            is_driver_present = True
            yield bin_id, bins[bin_id]
    if not is_driver_present:
        raise ResourceNotFoundException("No Bins allocated yet "
                                        "to driver whose email Id: " + email)


def is_bin_available(bin_id):
    """
    Checks if a bin with the specified ID exists.

    Args:
        bin_id (str): The ID of the bin to check.

    Returns:
        bool: True if the bin exists; otherwise, raises ResourceNotFoundException.

    Raises:
        ResourceNotFoundException: If no bin is found with the specified ID.
    """
    if bin_id in bins:
        return True
    raise ResourceNotFoundException("No Bin found by this Id: " + bin_id)


def get_bin_wastage_type(bin_id):
    """
    Retrieves the details of a bin, including its wastage type, by its ID.

    Args:
        bin_id (str): The ID of the bin.

    Returns:
        dict: Details of the bin, including its wastage type.

    Raises:
        ResourceNotFoundException: If the bin is not available.
    """
    if is_bin_available(bin_id):
        return bins[bin_id]


def is_address_already_available(door_no, area):
    """
    Checks if a bin with the specified door number and area already exists.

    Args:
        door_no (str): The door number of the bin.
        area (str): The area where the bin is located.

    Returns:
        bool: False if the address is available; raises UserAlreadyExistsError if the address already exists.

    Raises:
        UserAlreadyExistsError: If a bin with the same door number and area is already present.
    """
    for bin_id in bins:
        if bins[bin_id][AREA] == area and bins[bin_id][DOOR_NO] == door_no:
            raise UserAlreadyExistsError("Address already exist")
    return False


def raise_complaint(bin_id, complaint):
    """
    Creates a new complaint record for a specified bin.

    Args:
        bin_id (str): The ID of the bin associated with the complaint.
        complaint (str): The description of the complaint.

    Creates:
        A complaint record with status "pending" and a unique complaint ID.
    """
    if bin_id in bins:
        area = bins[bin_id][AREA]
        customer_id = bins[bin_id][CUSTOMER_ID]
        driver_email = bins[bin_id][DRIVER_EMAIL]
        customer_complaints = {
            "area": area,
            "complaint": complaint,
            "bin_id": bin_id,
            "customer_id": customer_id,
            "driver_email": driver_email,
            "status": "pending",
            "date_time": datetime.now()
        }
        complaint_id = str(uuid.uuid4())
        complaints[complaint_id] = customer_complaints
        logger.info(COMPLAINT_REGISTERED.format(bin_id=bin_id))
        return True


def view_all_complaints():
    """
    Yields all registered complaints.

    Yields:
        tuple: Complaint ID and details of each complaint.

    Raises:
        ResourceNotFoundException: If no complaints are registered.
    """
    if len(complaints) != 0:
        for complaint_id in complaints:
            yield complaint_id, complaints[complaint_id]
    else:
        raise ResourceNotFoundException("No complaints registered yet")


def check_complaints(email):
    """
    Retrieves complaints associated with a specified driver's email.

    Args:
        email (str): The email address of the driver.

    Yields:
        tuple: Complaint ID and details of each complaint associated with the driver's email.

    Raises:
        ResourceNotFoundException: If no complaints are registered for the specified email.
    """
    is_complaint_registered = False
    for complaint_id in complaints:
        if complaints[complaint_id][DRIVER_EMAIL] == email:
            is_complaint_registered = True
            yield complaint_id, complaints[complaint_id]

    if not is_complaint_registered:
        raise ResourceNotFoundException("No complaint registered for your email: " + email)


def change_complaint_status(status, bin_id):
    """
    Updates the status of a complaint associated with the specified bin ID.

    Args:
        status (str): The new status of the complaint.
        bin_id (str): The ID of the bin associated with the complaint.

    Updates:
        The status of the complaint to the specified value if it matches today's date.
    """
    for complaint_id in complaints:
        if complaints[complaint_id][BIN_ID] == bin_id:
            complaints[complaint_id][STATUS] = status


def get_customer_details(email):
    """
    Retrieves customer details by their email address.

    Args:
        email (str): The email address of the customer.

    Returns:
        tuple: Customer ID and details of the customer.

    Raises:
        ResourceNotFoundException: If no customer is found with the specified email.
    """
    for customer_id in customer_details:
        if customer_details[customer_id][DICT_EMAIL] == email:
            return customer_id, customer_details[customer_id]
    raise ResourceNotFoundException("No customer found by this email: " + email)


def get_customer_bin(customer_id):
    """
    Retrieves the bin associated with a specified customer ID.

    Args:
        customer_id (str): The ID of the customer.

    Returns:
        tuple: Bin ID and details of the bin associated with the customer ID.

    Raises:
        ResourceNotFoundException: If no bin is found for the specified customer ID.
    """
    for bin_id in bins:
        if bins[bin_id][CUSTOMER_ID] == customer_id:
            return bin_id, bins[bin_id]
    raise ResourceNotFoundException("No bin registered for this customer_id: " + customer_id)


def is_complaint_raised(bin_id):
    for complaint_id in complaints:
        if complaints[complaint_id][BIN_ID] == bin_id and complaints[complaint_id][STATUS] == COMPLAINT_STATUS:
            return True
        else:
            return False
