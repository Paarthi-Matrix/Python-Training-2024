from common.common_constants import (
    PICK_CHOICE, INPUT_NAME, EXITING,
    INPUT_EMAIL, INPUT_LOCATION, INPUT_CONTACT, INVALID_CHOICE,
    INVALID_INPUT, INPUT_PASSWORD, NAME_UPDATED, EMAIL_UPDATED, INPUT_ID,
    MOBILE_NUMBER_KEY, MOBILE_NUMBER_UPDATED,
    LOCATION_UPDATED, INPUT_LICENSE_NUMBER, LICENSE_NUMBER_KEY,
    LICENSE_NUMBER_UPDATED, AVAILABLE_ORDERS,
    NO_AVAILABLE_ORDERS, STATUS, STATUS_PLACED, STATUS_IN_TRANSPORT,
    STATUS_ASSIGNED, INPUT_OTP, ORDER_ID_KEY, ZERO, ONE, TWO,
    THREE, FOUR, FIVE, SIX, SEVEN, INVALID_OTP, PASSWORD_UPDATED, PASSWORD_KEY
)
from common.customer_constants import (
    INPUT_ORDER_ID, ORDER_NOT_FOUND_OR_NOT_AVAILABLE,
    ORDER_NOT_FOUND_OR_NOT_ASSIGNED,
    ORDER_DELIVERED, ORDER_NOT_FOUND_OR_NOT_IN_TRANSPORT,
    ORDER_PICKED_BY_DELIVERY_PERSON, ORDER_ASSIGNED_TO_DELIVERY_PERSON
)
from common.delivery_person_constants import (
    DELIVERY_PERSON_CHOICE, DELIVERY_PERSON_UPDATE_CHOICE,
    UPDATE_DELIVERY_PERSON_NOT_FOUND, DELIVERY_PERSON_ADDED,
    INPUT_DELIVERY_PERSON_ID, DELIVERY_PERSON_NOT_FOUND,
    CURRENT_ORDER_ID_KEY, DELIVERY_PERSON_HAS_NO_ORDER_TO_DELIVER,
    DELIVERY_PERSON_HAS_NO_ORDER_TO_PICK
)
from common.restaurant_constants import (
    INVALID_NAME, INVALID_EMAIL,
    INVALID_CONTACT, INVALID_LOCATION, INVALID_PASSWORD, NAME_KEY,
    LOCATION_KEY, EMAIL_KEY, INVALID_LICENSE
)
from resources.logging_config import logger
from service.customer_service import (
    list_available_orders,
    get_order_by_id
)
from service.delivery_person_service import (
    add_delivery_person, update_delivery_person_details,
    pick_up_order, deliver_order, assign_delivery_person,
    get_delivery_person_by_id)
from utils.validator import (
    is_valid_email, is_valid_mobile, is_valid_name,
    is_valid_password, is_valid_license, input_validation, update_entity
)

def update_delivery_person():
    """
    Manages the update process for delivery person details based on user input.

    Prompts the user to select the detail to update and performs the update
    if the delivery person is found. Uses `handle_update` for updating specific
    fields of the delivery person.

    The user is prompted to select from updating the name, email, mobile number,
    location, license number, or password. Handles invalid choices and delivery
    person not found scenarios.
    """
    while True:
        try:
            print(DELIVERY_PERSON_UPDATE_CHOICE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric() and len(choice) == ONE and ZERO <= int(choice) <= SIX):
                raise ValueError
            choice = int(choice)

            if choice in range(ONE, SEVEN):
                unique_id = input(INPUT_ID)
                delivery_person = get_delivery_person_by_id(unique_id)
                if delivery_person:
                    if choice == ONE:
                        update_entity(delivery_person, NAME_KEY, INPUT_NAME, is_valid_name, NAME_UPDATED, INVALID_NAME,
                                      update_delivery_person_details)
                    elif choice == TWO:
                        update_entity(delivery_person, EMAIL_KEY, INPUT_EMAIL, is_valid_email, EMAIL_UPDATED,
                                      INVALID_EMAIL, update_delivery_person_details)
                    elif choice == THREE:
                        update_entity(delivery_person, MOBILE_NUMBER_KEY, INPUT_CONTACT, is_valid_mobile,
                                      MOBILE_NUMBER_UPDATED, INVALID_CONTACT, update_delivery_person_details)
                    elif choice == FOUR:
                        update_entity(delivery_person, LOCATION_KEY, INPUT_LOCATION, is_valid_name, LOCATION_UPDATED,
                                      INVALID_LOCATION, update_delivery_person_details)
                    elif choice == FIVE:
                        update_entity(delivery_person, LICENSE_NUMBER_KEY, INPUT_LICENSE_NUMBER, is_valid_license,
                                      LICENSE_NUMBER_UPDATED, INVALID_LICENSE, update_delivery_person_details)
                    elif choice == SIX:
                        update_entity(delivery_person, PASSWORD_KEY, INPUT_PASSWORD, is_valid_password,
                                      PASSWORD_UPDATED, INVALID_PASSWORD, update_delivery_person_details)
                else:
                    logger.warning(UPDATE_DELIVERY_PERSON_NOT_FOUND.format(unique_id=unique_id))
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)




def create_delivery_person():
    """
    Prompts the user to input details for creating a new delivery person and adds them.
    """
    name = input_validation(INPUT_NAME, is_valid_name, INVALID_NAME)
    password = input_validation(INPUT_PASSWORD, is_valid_password, INVALID_PASSWORD)
    email = input_validation(INPUT_EMAIL, is_valid_email, INVALID_EMAIL)
    mobile_number = input_validation(INPUT_CONTACT, is_valid_mobile, INVALID_CONTACT)
    location = input_validation(INPUT_LOCATION, is_valid_name, INVALID_LOCATION)
    license_number = input_validation(INPUT_LICENSE_NUMBER, is_valid_license, INVALID_LICENSE)
    unique_id = add_delivery_person(name.lower(), password, email.lower(), location.lower(), mobile_number,
                                    license_number)
    logger.info(DELIVERY_PERSON_ADDED.format(unique_id=unique_id))


def delivery_person_operations():
    while True:
        try:
            print(DELIVERY_PERSON_CHOICE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == ONE and ZERO <= int(choice) <= SEVEN):
                raise ValueError
            choice = int(choice)
            if choice == ONE:
                create_delivery_person()
            elif choice == TWO:
                update_delivery_person()
            elif choice == THREE:
                unique_id = input(INPUT_DELIVERY_PERSON_ID)
                delivery_person = get_delivery_person_by_id(unique_id)
                if delivery_person:
                    orders = list_available_orders(delivery_person[LOCATION_KEY])
                    if orders:
                        logger.info(AVAILABLE_ORDERS)
                        for order in orders:
                            logger.info(
                                f"Order ID: {order["order_id"]},"
                                f" Customer ID: {order["customer_id"]},"
                                f" Restaurant ID: {order["restaurant_id"]},"
                                f" Food Items: {order["food_items"]}")
                    else:
                        logger.warning(NO_AVAILABLE_ORDERS)
                else:
                    logger.warning(DELIVERY_PERSON_NOT_FOUND.format(unique_id=unique_id))
            elif choice == FOUR:
                unique_id = input(INPUT_DELIVERY_PERSON_ID)
                delivery_person = get_delivery_person_by_id(unique_id)
                if delivery_person:
                    order_id = input(INPUT_ORDER_ID)
                    order = get_order_by_id(order_id)
                    if order and order[STATUS] == STATUS_PLACED:
                        result = assign_delivery_person(
                            delivery_person, order, unique_id, order_id)
                        if isinstance(result, dict):
                            logger.info(
                                ORDER_ASSIGNED_TO_DELIVERY_PERSON.
                                format(order_id=result[ORDER_ID_KEY],
                                       unique_id=unique_id))
                    else:
                        logger.warning(ORDER_NOT_FOUND_OR_NOT_AVAILABLE)
                else:
                    logger.warning(DELIVERY_PERSON_NOT_FOUND.format(unique_id=unique_id))
            elif choice == FIVE:
                unique_id = input(INPUT_DELIVERY_PERSON_ID)
                delivery_person = get_delivery_person_by_id(unique_id)
                if delivery_person:
                    if CURRENT_ORDER_ID_KEY in delivery_person:
                        order_id = delivery_person[CURRENT_ORDER_ID_KEY]
                        order = get_order_by_id(order_id)
                        if order and order[STATUS] == STATUS_ASSIGNED:
                            result = pick_up_order(order)
                            if isinstance(result, dict):
                                logger.info(ORDER_PICKED_BY_DELIVERY_PERSON.
                                            format(order_id=result[ORDER_ID_KEY],
                                                   unique_id=unique_id))
                        else:
                            logger.warning(ORDER_NOT_FOUND_OR_NOT_ASSIGNED)
                    else:
                        logger.warning(DELIVERY_PERSON_HAS_NO_ORDER_TO_PICK)
                else:
                    logger.warning(DELIVERY_PERSON_NOT_FOUND)
            elif choice == SIX:
                delivery_person_id = input(INPUT_DELIVERY_PERSON_ID)
                delivery_person = get_delivery_person_by_id(delivery_person_id)
                if delivery_person:
                    if CURRENT_ORDER_ID_KEY in delivery_person:
                        order_id = delivery_person[CURRENT_ORDER_ID_KEY]
                        order = get_order_by_id(order_id)
                        if order and order[STATUS] == STATUS_IN_TRANSPORT:
                            while True:
                                otp_input = input(INPUT_OTP)
                                result = deliver_order(order, delivery_person, otp_input)
                                if result:
                                    logger.info(ORDER_DELIVERED.format(order_id=result[ORDER_ID_KEY]))
                                    break
                                else:
                                    logger.warning(INVALID_OTP)
                        else:
                            logger.warning(ORDER_NOT_FOUND_OR_NOT_IN_TRANSPORT)
                    else:
                        logger.warning(DELIVERY_PERSON_HAS_NO_ORDER_TO_DELIVER)
                else:
                    logger.warning(DELIVERY_PERSON_NOT_FOUND.format(unique_id=delivery_person_id))
            elif choice == SEVEN:
                unique_id = input(INPUT_DELIVERY_PERSON_ID)
                delivery_person = get_delivery_person_by_id(unique_id)
                if delivery_person:
                    logger.info(delivery_person)
                else:
                    logger.warning(DELIVERY_PERSON_NOT_FOUND.format(unique_id=unique_id))
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)