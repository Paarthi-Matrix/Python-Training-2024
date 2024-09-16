import traceback

from project.config.config import logger
from project.constant.constant import (
    PICK_CHOICE, INPUT_NAME, INPUT_EMAIL, INPUT_LOCATION, INPUT_CONTACT,
    INVALID_CHOICE, INPUT_PASSWORD, NAME_UPDATED, EMAIL_UPDATED, INPUT_ID,
    MOBILE_NUMBER_KEY, MOBILE_NUMBER_UPDATED, LOCATION_UPDATED,
    INPUT_LICENSE_NUMBER, LICENSE_NUMBER_KEY, LICENSE_NUMBER_UPDATED, ZERO,
    ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, PASSWORD_UPDATED, PASSWORD_KEY,
    DELIVERY_PARTNER_UPDATE_CHOICE, UPDATE_DELIVERY_PARTNER_NOT_FOUND,
    DELIVERY_PARTNER_ADDED, INVALID_NAME, INVALID_EMAIL, INVALID_CONTACT,
    INVALID_LOCATION, INVALID_PASSWORD, NAME_KEY, LOCATION_KEY, EMAIL_KEY,
    INVALID_LICENSE, DELIVERY_PARTNER_NOT_FOUND, NO_AVAILABLE_ORDERS,
    STATUS_PLACED, STATUS, ORDER_ASSIGNED_TO_DELIVERY_PARTNER, ORDER_ID_KEY,
    ORDER_NOT_FOUND_OR_NOT_AVAILABLE, CURRENT_ORDER_ID_KEY, STATUS_ASSIGNED,
    ORDER_PICKED_BY_DELIVERY_PARTNER, ORDER_NOT_FOUND_OR_NOT_ASSIGNED,
    DELIVERY_PARTNER_HAS_NO_ORDER_TO_PICK, STATUS_IN_TRANSPORT,
    ORDER_DELIVERED, INVALID_OTP, ORDER_NOT_FOUND_OR_NOT_IN_TRANSPORT,
    DELIVERY_PARTNER_HAS_NO_ORDER_TO_DELIVER
)
from project.service.customer import list_available_orders, get_order
from project.service.delivery import (
    add, update, get, assign_delivery_partner, pick_up_order, deliver_order
)
from project.utils.utils import (
    is_valid_email, is_valid_mobile, is_valid_name, is_valid_password,
    is_valid_license, input_validation, update_entity, continue_operations
)


def update_delivery():
    """
    Manages the update process for delivery person details based on user input.

    Prompts the user to select the detail to update and performs the update
    if the delivery person is found. Uses `handle_update` for updating specific
    fields of the delivery person.

    The user is prompted to select from updating the name, email, mobile number,
    location, license number, or password. Handles invalid choices and delivery
    person not found scenarios.
    """
    print(DELIVERY_PARTNER_UPDATE_CHOICE)
    choice = input(PICK_CHOICE)
    if not (choice.isnumeric() and len(choice) == ONE and ZERO <= int(choice) <= SIX):
        raise ValueError
    choice = int(choice)

    if choice in range(ONE, SEVEN):
        unique_id = input(INPUT_ID)
        delivery_partner = get(unique_id)
        if delivery_partner:
            if choice == ONE:
                update_entity(delivery_partner, NAME_KEY, INPUT_NAME, is_valid_name, NAME_UPDATED, INVALID_NAME,
                              update)
            elif choice == TWO:
                update_entity(delivery_partner, EMAIL_KEY, INPUT_EMAIL, is_valid_email, EMAIL_UPDATED,
                              INVALID_EMAIL, update)
            elif choice == THREE:
                update_entity(delivery_partner, MOBILE_NUMBER_KEY, INPUT_CONTACT, is_valid_mobile,
                              MOBILE_NUMBER_UPDATED, INVALID_CONTACT, update)
            elif choice == FOUR:
                update_entity(delivery_partner, LOCATION_KEY, INPUT_LOCATION, is_valid_name, LOCATION_UPDATED,
                              INVALID_LOCATION, update)
            elif choice == FIVE:
                update_entity(delivery_partner, LICENSE_NUMBER_KEY, INPUT_LICENSE_NUMBER, is_valid_license,
                              LICENSE_NUMBER_UPDATED, INVALID_LICENSE, update)
            elif choice == SIX:
                update_entity(delivery_partner, PASSWORD_KEY, INPUT_PASSWORD, is_valid_password,
                              PASSWORD_UPDATED, INVALID_PASSWORD, update)
        else:
            logger.warning(UPDATE_DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id))
    else:
        logger.warning(INVALID_CHOICE)
    continue_operations(update_delivery)


def create_delivery(name, password, email, mobile_number, location, license_number):
    """
    Prompts the user to input details for creating a new delivery person and adds them.
    """
    result = {}
    try:
        delivery_partner_name = input_validation(name, is_valid_name, INVALID_NAME)
        delivery_partner_password = input_validation(password, is_valid_password, INVALID_PASSWORD)
        delivery_partner_email = input_validation(email, is_valid_email, INVALID_EMAIL)
        delivery_partner_mobile_number = input_validation(mobile_number, is_valid_mobile, INVALID_CONTACT)
        delivery_partner_location = input_validation(location, is_valid_name, INVALID_LOCATION)
        delivery_partner_license_number = input_validation(license_number, is_valid_name, INVALID_LICENSE)
        if delivery_partner_name != name:
            result.setdefault(400, []).append(delivery_partner_name)
        if delivery_partner_password != password:
            result.setdefault(400, []).append(delivery_partner_password)
        if delivery_partner_email != email:
            result.setdefault(400, []).append(delivery_partner_email)
        if delivery_partner_mobile_number != mobile_number:
            result.setdefault(400, []).append(delivery_partner_mobile_number)
        if delivery_partner_location != location:
            result.setdefault(400, []).append(delivery_partner_location)
        if delivery_partner_license_number != license_number:
            result.setdefault(400, []).append(delivery_partner_license_number)
        if not result:
            unique_id = add(delivery_partner_name.lower(), delivery_partner_password, delivery_partner_email.lower(),
                            delivery_partner_location.lower(), delivery_partner_mobile_number,
                            delivery_partner_license_number)
            logger.info(DELIVERY_PARTNER_ADDED.format(unique_id=unique_id))
            result[200] = DELIVERY_PARTNER_ADDED.format(unique_id=unique_id)
            return result
        else:
            return result
    except ValueError as ve:
        logger.error(f"Value Error Occurred: {str(ve)}\n{traceback.format_exc()}")
        result[400] = "Incorrect Value"
        return result


def get_available_orders(unique_id: str):
    result = {}
    delivery_partner = get(unique_id)
    if not delivery_partner:
        logger.warning(DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id))
        result[404] = DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id)
        return result
    orders = list_available_orders(delivery_partner[LOCATION_KEY])
    if orders:
        result[200] = orders
        return result
    else:
        logger.warning(NO_AVAILABLE_ORDERS)
        result[404] = NO_AVAILABLE_ORDERS
        return result


def assign_delivery(unique_id: str, order_id: str):
    result = {}
    delivery_partner = get(unique_id)
    if delivery_partner:
        order = get_order(order_id)
        if order and order[STATUS] == STATUS_PLACED:
            assigned_order = assign_delivery_partner(
                delivery_partner, order, unique_id, order_id)
            logger.info(ORDER_ASSIGNED_TO_DELIVERY_PARTNER.
                        format(order_id=assigned_order[ORDER_ID_KEY],
                               unique_id=unique_id))
            result[200] = ORDER_ASSIGNED_TO_DELIVERY_PARTNER.format(
                order_id=assigned_order[ORDER_ID_KEY], unique_id=unique_id)
            return result
        else:
            logger.warning(ORDER_NOT_FOUND_OR_NOT_AVAILABLE)
            result[404] = ORDER_NOT_FOUND_OR_NOT_AVAILABLE
            return result
    else:
        logger.warning(DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id))
        result[404] = DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id)


def pick_order(unique_id: str):
    result = {}
    delivery_partner = get(unique_id)
    if not delivery_partner:
        logger.warning(DELIVERY_PARTNER_NOT_FOUND)
        result[404] = DELIVERY_PARTNER_NOT_FOUND
        return result
    if CURRENT_ORDER_ID_KEY in delivery_partner:
        order_id = delivery_partner[CURRENT_ORDER_ID_KEY]
        order = get_order(order_id)
        if order and order[STATUS] == STATUS_ASSIGNED:
            picked_order = pick_up_order(order)
            logger.warning(ORDER_PICKED_BY_DELIVERY_PARTNER.format(
                order_id=picked_order[ORDER_ID_KEY], unique_id=unique_id))
            result[200] = ORDER_PICKED_BY_DELIVERY_PARTNER.format(
                order_id=picked_order[ORDER_ID_KEY], unique_id=unique_id)
            return result
        else:
            logger.warning(ORDER_NOT_FOUND_OR_NOT_ASSIGNED)
            result[404] = ORDER_NOT_FOUND_OR_NOT_ASSIGNED
            return result
    else:
        logger.warning(DELIVERY_PARTNER_HAS_NO_ORDER_TO_PICK)
        result[204] = DELIVERY_PARTNER_HAS_NO_ORDER_TO_PICK
        return result


def complete_order(delivery_partner_id: str, otp):
    result = {}
    delivery_partner = get(delivery_partner_id)
    if not delivery_partner:
        logger.warning(DELIVERY_PARTNER_NOT_FOUND.format(unique_id=delivery_partner_id))
        result[404] = DELIVERY_PARTNER_NOT_FOUND.format(unique_id=delivery_partner_id)
        return result
    if CURRENT_ORDER_ID_KEY in delivery_partner:
        order_id = delivery_partner[CURRENT_ORDER_ID_KEY]
        order = get_order(order_id)
        if order and order[STATUS] == STATUS_IN_TRANSPORT:
            delivered_order = deliver_order(order, delivery_partner, otp)
            if delivered_order:
                logger.info(ORDER_DELIVERED.format(order_id=delivered_order[ORDER_ID_KEY]))
                result[200] = ORDER_DELIVERED.format(order_id=delivered_order[ORDER_ID_KEY])
                return result
            else:
                logger.warning(INVALID_OTP)
                result[400] = INVALID_OTP
                return result
        else:
            logger.warning(ORDER_NOT_FOUND_OR_NOT_IN_TRANSPORT)
            result[409] = ORDER_NOT_FOUND_OR_NOT_IN_TRANSPORT
            return result
    else:
        logger.warning(DELIVERY_PARTNER_HAS_NO_ORDER_TO_DELIVER)
        result[204] = DELIVERY_PARTNER_HAS_NO_ORDER_TO_DELIVER
        return result
def get_my_details(unique_id:str):
    result = {}
    delivery_partner = get(unique_id)
    if delivery_partner:
        logger.info(delivery_partner)
        result[200] = delivery_partner
        return result
    else:
        logger.warning(DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id))
        result[404] = DELIVERY_PARTNER_NOT_FOUND.format(unique_id=unique_id)
        return result
