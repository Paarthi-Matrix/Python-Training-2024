import uuid

from constant.constant import PASSWORD_KEY, LOCATION_KEY, IS_DELETE
from service.customer import get as get_customer

delivery_partners = {}


def add(name: str,password, email: str, location: str,
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
    delivery_partners[unique_id] = {
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


def get(unique_id: str):
    """
    Retrieves a delivery person's details by their unique ID if they are not marked as deleted.

    Parameters:
    - unique_id (str): The unique ID of the delivery person.

    Returns:
    - dict: The delivery person's details, or None if the delivery person is not found or is deleted.
    """
    delivery_partner = delivery_partners.get(unique_id)
    if delivery_partner:
        if not delivery_partner[IS_DELETE]:
            return delivery_partner
    return None

def filter_delivery_partner_info(delivery_partner):
    """
    Filters out sensitive information (e.g., password) from a delivery person's details.

    Parameters:
    - delivery_partner (dict): The delivery person's full details.

    Returns:
    - dict: The delivery person's details with sensitive information removed.
    """
    return {key: value for key, value in delivery_partner.items() if key not in [PASSWORD_KEY,IS_DELETE]}

def get_all():
    """
    Retrieves all delivery persons who are not marked as deleted.

    Returns:
    - dict: A dictionary of all delivery persons with their sensitive information removed.
    """
    filtered_delivery_partners = {
        delivery_partner_id: filter_delivery_partner_info(delivery_partner)
        for delivery_partner_id, delivery_partner in delivery_partners.items()
        if not delivery_partner.get(IS_DELETE, False)
    }
    return filtered_delivery_partners


def update_ratings(ratings: int, delivery_partner):
    """
    Updates the delivery person's ratings by adding a new rating and recalculating the average rating.

    Parameters:
    - ratings (int): The new rating to add.
    - delivery_partner (dict): The delivery person's details.

    Returns:
    - bool: True if the rating was successfully updated.
    """
    total_ratings = delivery_partner["total_ratings"].append(ratings)
    delivery_partner["ratings"] = sum(total_ratings) / len(total_ratings)
    return True


def remove(unique_id: str):
    """
    Marks a delivery person as deleted.

    Parameters:
    - unique_id (str): The unique ID of the delivery person to delete.

    Returns:
    - bool: True if the delivery person was successfully marked as deleted.
    """
    delivery_partner = get(unique_id)
    delivery_partner["is_deleted"] = True
    return True


def update(delivery_partner: dict, to_update: str, details_to_update: str):
    """
    Updates a specific detail of a delivery person.

    Parameters:
    - delivery_partner (dict): The delivery person's details.
    - to_update (str): The key of the detail to update.
    - details_to_update (str): The new value for the specified detail.

    Returns:
    - bool: True if the update was successful.
    """
    delivery_partner[to_update] = details_to_update
    return True


def assign_delivery_partner(delivery_partner, order, delivery_partner_id, order_id):
    """
    Assigns a delivery person to an order.

    Parameters:
    - delivery_partner (dict): The delivery person's details.
    - order (dict): The order details.
    - delivery_partner_id (str): The unique ID of the delivery person.
    - order_id (str): The unique ID of the order.

    Returns:
    - dict: The updated order details with the assigned delivery person.
    """
    order["status"] = "Assigned"
    order["delivery_partner_id"] = delivery_partner_id
    delivery_partner["current_order_id"] = order_id
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


def deliver_order(order, delivery_partner, otp_input):
    """
    Updates the status of an order to "Delivered" if the correct OTP is provided by the customer.

    Parameters:
    - order (dict): The order details.
    - delivery_partner (dict): The delivery person's details.
    - otp_input (str): The OTP provided by the customer.

    Returns:
    - dict or bool: The updated order details if the OTP is correct, False if the OTP is incorrect.
    """
    if otp_input == order["otp"]:
        order["status"] = "Delivered"
        delivery_partner.pop("current_order_id", None)
        delivery_partner["completed_orders"] += 1
        delivery_partner[LOCATION_KEY] = get_customer(order["customer_id"])[LOCATION_KEY]
        return order
    else:
        return None