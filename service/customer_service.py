from custom_exception.resource_not_found_exception import ResourceNotFoundException

from helper.logger_constant import (
    LOG_CUSTOMER_REGISTERED_WITH_ID,
    LOG_CUSTOMER_UPDATED
)

from resources.logger_configuration import logger

from util.validation import is_valid_name

import uuid

# Dictionary to store customer details by their ID
customer_details = {}


def get_all_customer():
    """
    Generator function that yields customer details from the customer details dictionary.

    If there are no customers in the dictionary, it yields None.

    Yields:
    - dict: A dictionary containing the details of each customer.
    - None: If the customer details dictionary is empty.
    """
    if len(customer_details) == 0:
        yield None
    else:
        for customer_id in customer_details:
            yield customer_details[customer_id]


def register_customer(name, email, password, mobile_no, account_no):
    """
    Registers a new customer and returns a unique customer ID.

    Parameters:
    - name: Customer's name
    - email: Customer's email
    - password: Customer's password
    - mobile_no: Customer's mobile number
    - account_no: Customer's account number

    Returns:
    - customer_id: The unique ID assigned to the customer
    """
    # Create a dictionary to store customer information
    customers = {
        "name": name,
        "email": email,
        "password": password,
        "mobile_no": mobile_no,
        "account_no": account_no
    }

    # Generate a unique customer ID using uuid4
    customer_id = str(uuid.uuid4())

    # Store customer details in the global dictionary
    customer_details[customer_id] = customers

    logger.info(LOG_CUSTOMER_REGISTERED_WITH_ID.format(customer_id=customer_id))


def search_customer(customer_identifier):
    """
    Retrieves and prints the details of a customer by their ID.

    Parameters:
    - cus_id: The unique ID of the customer
    """
    if is_valid_name(customer_identifier):
        customers = customer_details.values()
        find_customers = []
        for detail in customers:
            customer_name = detail["name"]
            if customer_name.lower().__contains__(customer_identifier
                                                          .lower()):
                find_customers.append(detail)
        if len(find_customers) == 0:
            raise ResourceNotFoundException("No customer found by this name: " + customer_identifier)
        else:
            return find_customers
    else:
        if customer_identifier in customer_details:
            return customer_details.get(customer_identifier)
        else:
            raise ResourceNotFoundException("No customer found by this Id: " + customer_identifier)


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
        customer_details.pop(customer_id)
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
    customer = customer_details[customer_id]
    customer[to_update] = detail_to_update
    logger.info(LOG_CUSTOMER_UPDATED.format(customer_id=customer_id
                                            , field=to_update, value=detail_to_update))
    return customer_id


def is_customer_present(customer_id):
    """
    Checks if a customer exists in the customer details dictionary.

    Parameters:
    - customer_id: The unique ID of the customer to be checked.

    Returns:
    - True: If the customer exists in the dictionary.
    - False: If the customer does not exist in the dictionary.
    """
    if customer_id in customer_details:
        return True
    raise ResourceNotFoundException("No customer found by this Id: " + customer_id)
