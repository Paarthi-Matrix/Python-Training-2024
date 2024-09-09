import uuid

from common.common_constants import PASSWORD_KEY
from common.restaurant_constants import LOCATION_KEY, IS_DELETE
from service.customer_service import get_by_id

delivery_persons = {}


def add_delivery_person(name: str,password, email: str, location: str,
                        mobile_number: str, license_number: str):
    """
    Registers a new delivery person and assigns them a unique ID.

    Parameters:
    - name (str): The name of the delivery person.
    - password: The delivery person's password.
    - email (str): The delivery person's email address.
    - location (str): The delivery person's location.
    - mobile_number (str): The delivery person's mobile number.
    - license_number (str): The delivery person's license number.

    Returns:
    - str: The unique ID assigned to the delivery person.
    """
    unique_id = str(uuid.uuid4())
    delivery_persons[unique_id] = {
        "id": unique_id,
        "name": name,
        "password":password,
        "email": email,
        "mobile_number": mobile_number,
        "license_number": license_number,
        "location": location,
        "ratings": None,
        "completed_orders": 0,
        "total_ratings": [],
        IS_DELETE: False
    }
    return unique_id


def get_delivery_person_by_id(unique_id: str):
    """
    Retrieves a delivery person's details by their unique ID if they are not marked as deleted.

    Parameters:
    - unique_id (str): The unique ID of the delivery person.

    Returns:
    - dict: The delivery person's details, or None if the delivery person is not found or is deleted.
    """
    delivery_person = delivery_persons.get(unique_id)
    if delivery_person:
        if not delivery_person[IS_DELETE]:
            return delivery_person
    return None

def filter_delivery_person_info(delivery_person):
    """
    Filters out sensitive information (e.g., password) from a delivery person's details.

    Parameters:
    - delivery_person (dict): The delivery person's full details.

    Returns:
    - dict: The delivery person's details with sensitive information removed.
    """
    return {key: value for key, value in delivery_person.items() if key not in [PASSWORD_KEY,IS_DELETE]}

def get_all_delivery_persons():
    """
    Retrieves all delivery persons who are not marked as deleted.

    Returns:
    - dict: A dictionary of all delivery persons with their sensitive information removed.
    """
    filtered_delivery_persons = {
        delivery_person_id: filter_delivery_person_info(delivery_person)
        for delivery_person_id, delivery_person in delivery_persons.items()
        if not delivery_person.get(IS_DELETE, False)
    }
    return filtered_delivery_persons


def update_ratings(ratings: int, delivery_person):
    """
    Updates the delivery person's ratings by adding a new rating and recalculating the average rating.

    Parameters:
    - ratings (int): The new rating to add.
    - delivery_person (dict): The delivery person's details.

    Returns:
    - bool: True if the rating was successfully updated.
    """
    total_ratings = delivery_person["total_ratings"].append(ratings)
    delivery_person["ratings"] = sum(total_ratings) / len(total_ratings)
    return True


def remove_delivery_person(unique_id: str):
    """
    Marks a delivery person as deleted.

    Parameters:
    - unique_id (str): The unique ID of the delivery person to delete.

    Returns:
    - bool: True if the delivery person was successfully marked as deleted.
    """
    delivery_person = get_delivery_person_by_id(unique_id)
    delivery_person["is_deleted"] = True
    return True


def update_delivery_person_details(delivery_person: dict, to_update: str, details_to_update: str):
    """
    Updates a specific detail of a delivery person.

    Parameters:
    - delivery_person (dict): The delivery person's details.
    - to_update (str): The key of the detail to update.
    - details_to_update (str): The new value for the specified detail.

    Returns:
    - bool: True if the update was successful.
    """
    delivery_person[to_update] = details_to_update
    return True


def assign_delivery_person(delivery_person, order, delivery_person_id, order_id):
    """
    Assigns a delivery person to an order.

    Parameters:
    - delivery_person (dict): The delivery person's details.
    - order (dict): The order details.
    - delivery_person_id (str): The unique ID of the delivery person.
    - order_id (str): The unique ID of the order.

    Returns:
    - dict: The updated order details with the assigned delivery person.
    """
    order["status"] = "Assigned"
    order["delivery_person_id"] = delivery_person_id
    delivery_person["current_order_id"] = order_id
    return order


def pick_up_order(order):
    """
    Updates the status of an order to "In Transport" when the delivery person picks it up.

    Parameters:
    - order (dict): The order details.

    Returns:
    - dict: The updated order details with the new status.
    """
    order["status"] = "In Transport"
    return order


def deliver_order(order, delivery_person, otp_input):
    """
    Updates the status of an order to "Delivered" if the correct OTP is provided by the customer.

    Parameters:
    - order (dict): The order details.
    - delivery_person (dict): The delivery person's details.
    - otp_input (str): The OTP provided by the customer.

    Returns:
    - dict or bool: The updated order details if the OTP is correct, False if the OTP is incorrect.
    """
    if otp_input == order["otp"]:
        order["status"] = "Delivered"
        delivery_person.pop("current_order_id", None)
        delivery_person["completed_orders"] += 1
        delivery_person[LOCATION_KEY] = get_by_id(order["customer_id"])[LOCATION_KEY]
        return order
    else:
        return False