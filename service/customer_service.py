import uuid
from helper.customer_constant import UUID_VERSION
from util.validation import is_valid_name

# Dictionary to store customer details by their ID
customer_details = {}


def get_all_customer():
    if len(customer_details) == 0:
        yield None
    else:
        for customer in customer_details:
            yield customer_details[customer]


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

    return customer_id


def search_customer(customer_identifier):
    """
    Retrieves and prints the details of a customer by their ID.

    Parameters:
    - cus_id: The unique ID of the customer
    """
    try:
        if is_valid_name(customer_identifier):
            customers = customer_details.values()
            find_customers = []
            for detail in customers:
                customer_name = detail["name"]
                if customer_name.lower().__contains__(customer_identifier.lower()):
                    find_customers.append(detail)
            if len(find_customers) == 0:
                return None
            else:
                return find_customers
        else:
            uuid_obj = uuid.UUID(customer_identifier, version=UUID_VERSION)
            return customer_details.get(customer_identifier)

    except ValueError:
        return None


def remove_customer(customer_id):
    if customer_details.__contains__(customer_id):
        customer_details.pop(customer_id)
        return None
    else:
        return customer_id


def update_customer(customer_id, detail_to_update, to_update):
        customer = customer_details[customer_id]
        customer[to_update] = detail_to_update
        return customer_id



def is_customer_present(customer_id):
    if customer_details.__contains__(customer_id):
        return True
    return False

