import traceback

from project.config.config import logger
from project.constant.constant import (
    PICK_CHOICE, INPUT_NAME, EXITING, INPUT_EMAIL, INPUT_LOCATION,
    INPUT_CONTACT, INVALID_CHOICE, INPUT_PASSWORD, NAME_UPDATED,
    EMAIL_UPDATED, INPUT_ID, MOBILE_NUMBER_KEY, MOBILE_NUMBER_UPDATED,
    LOCATION_UPDATED, ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, PASSWORD_UPDATED,
    PASSWORD_KEY, CUSTOMER_UPDATE_CHOICE, UPDATE_CUSTOMER_NOT_FOUND,
    INVALID_NAME, INVALID_EMAIL, INVALID_CONTACT, INVALID_LOCATION,
    INVALID_PASSWORD, NAME_KEY, LOCATION_KEY, EMAIL_KEY, RESTAURANT_NOT_FOUND,
    STATUS, STATUS_PENDING, ALREADY_HAVE_PENDING_CART, ITEMS_ADDED_TO_CART,
    NO_VALID_FOOD_ITEMS_RESTAURANT, CUSTOMER_NOT_FOUND, NO_CART_FOUND,
    ADD_CHOICE, REMOVE_CHOICE, ITEMS_REMOVED_FROM_CART,
    NO_VALID_FOOD_ITEMS_CART, INVALID_ADD_OR_REMOVE_ITEM_FROM_CART,
    NO_PENDING_CART, INVALID_CONFIRMATION, INVALID_PAYMENT_MODE, VALUE_YES,
    VALUE_NO, PAYMENT_MODE_CASH, PAYMENT_MODE_UPI, ORDER_PLACED, ORDER_DETAILS,
    ORDER_NOT_PLACED, INVALID_RATING, RATING_UPDATED,
    DELIVERY_PARTNER_NOT_FOUND, CUSTOMER_DELETED, CUSTOMER_ADDED
)
from project.service.customer import (
    get, update, add, get_cart_by_customer, add_to_cart, update_items_to_cart,
    remove_items_from_cart, place_order, get_customer_orders, remove
)
from project.service.delivery import get as get_delivery, update_ratings
from project.service.restaurant import get_all, get_menu, get as get_restaurant
from project.utils.utils import (
    is_valid_email, is_valid_mobile, is_valid_name, is_valid_password,
    update_entity, input_validation, continue_operations
)


def update_customer():
    """
        Manages the update process for customer details based on user input.

        Prompts the user to select the detail to update and performs the update
        if the customer is found. Uses `handle_update` for updating specific
        fields of the customer.

        The user is prompted to select from updating the name, email, mobile number,
        location, or password. Handles invalid choices and customer not found scenarios.
    """
    print(CUSTOMER_UPDATE_CHOICE)
    choice = input(PICK_CHOICE)
    if not (choice.isnumeric() and len(choice) == ONE and ZERO <= int(choice) <= FIVE):
        raise ValueError
    choice = int(choice)

    if choice in range(ONE, SIX):
        unique_id = input(INPUT_ID)
        customer = get(unique_id)
        if customer:
            if choice == ONE:
                update_entity(customer, NAME_KEY, INPUT_NAME, is_valid_name, NAME_UPDATED, INVALID_NAME,
                              update)
            elif choice == TWO:
                update_entity(customer, EMAIL_KEY, INPUT_EMAIL, is_valid_email, EMAIL_UPDATED, INVALID_EMAIL,
                              update)
            elif choice == THREE:
                update_entity(customer, MOBILE_NUMBER_KEY, INPUT_CONTACT, is_valid_mobile,
                              MOBILE_NUMBER_UPDATED, INVALID_CONTACT, update)
            elif choice == FOUR:
                update_entity(customer, LOCATION_KEY, INPUT_LOCATION, is_valid_name, LOCATION_UPDATED,
                              INVALID_LOCATION, update)
            elif choice == FIVE:
                update_entity(customer, PASSWORD_KEY, INPUT_PASSWORD, is_valid_password, PASSWORD_UPDATED,
                              INVALID_PASSWORD, update)
        else:
            logger.warning(UPDATE_CUSTOMER_NOT_FOUND.format(unique_id=unique_id))
    elif choice == ZERO:
        logger.debug(EXITING)
        return
    else:
        logger.warning(INVALID_CHOICE)
    continue_operations(update_customer())


def create_customer(name: str, password: str, email: str, mobile_number: str, location: str):
    """
    Prompts the user to input details for creating a new customer and adds them.
    """
    result = {}
    try:
        customer_name = input_validation(name, is_valid_name, INVALID_NAME)
        customer_password = input_validation(password, is_valid_password, INVALID_PASSWORD)
        customer_email = input_validation(email, is_valid_email, INVALID_EMAIL)
        customer_mobile_number = input_validation(mobile_number, is_valid_mobile, INVALID_CONTACT)
        customer_location = input_validation(location, is_valid_name, INVALID_LOCATION)
        if customer_name != name:
            result.setdefault(400, []).append(customer_name)
        if customer_password != password:
            result.setdefault(400, []).append(customer_password)
        if customer_email != email:
            result.setdefault(400, []).append(customer_email)
        if customer_mobile_number != mobile_number:
            result.setdefault(400, []).append(customer_mobile_number)
        if customer_location != location:
            result.setdefault(400, []).append(customer_location)
        if not result:
            customer_id = add(name.lower(), password, email.lower(),
                              mobile_number, location.lower())
            result[200] = CUSTOMER_ADDED.format(customer_id=customer_id)
            return result
        else:
            return result
    except ValueError as ve:
        logger.error(f"Value Error Occurred: {str(ve)}\n{traceback.format_exc()}")
        result[400] = "Incorrect Value"
        return result


def get_all_restaurants():
    return get_all()


def get_restaurant_menu(restaurant_id: str):
    result = {}
    restaurant_menu = get_menu(restaurant_id)
    if restaurant_menu:
        result[200] = restaurant_menu
        return result
    else:
        result[404] = RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id)
        return result


def add_food_to_cart(customer_id: str, restaurant_id: str, food_item_names: list):
    result = {}
    customer = get(customer_id)
    if customer:
        existing_cart = get_cart_by_customer(customer_id)
        if existing_cart and existing_cart[STATUS] == STATUS_PENDING:
            logger.warning(ALREADY_HAVE_PENDING_CART)
            result[409] = ALREADY_HAVE_PENDING_CART
            return result
        else:
            restaurant = get_restaurant(restaurant_id)
            if restaurant:
                added_cart = add_to_cart(customer_id, restaurant, restaurant_id, food_item_names)
                if added_cart:
                    logger.info(ITEMS_ADDED_TO_CART.format(food_item_names=food_item_names))
                    result[200] = ITEMS_ADDED_TO_CART
                    return result
                else:
                    logger.warning(NO_VALID_FOOD_ITEMS_RESTAURANT)
                    result[404] = NO_VALID_FOOD_ITEMS_RESTAURANT
                    return result
            else:
                logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
                result[404] = RESTAURANT_NOT_FOUND
                return result
    else:
        logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
        result[404] = CUSTOMER_NOT_FOUND
        return result


def view_cart(customer_id: str):
    result = {}
    cart = get_cart_by_customer(customer_id)
    if cart:
        logger.info(f"Cart ID {cart['id']} for Customer {customer_id}")
        result[200] = cart
        return result
    else:
        logger.warning(NO_CART_FOUND.format(customer_id=customer_id))
        result[404] = NO_CART_FOUND
        return result


def update_cart(customer_id: str, edit_choice: str, food_item_names: list):
    result = {}
    cart = get_cart_by_customer(customer_id)
    if cart and cart[STATUS] == STATUS_PENDING:
        if edit_choice == ADD_CHOICE:
            added_items = update_items_to_cart(food_item_names, cart)
            if added_items:
                logger.info(ITEMS_ADDED_TO_CART)
                result[200] = ITEMS_ADDED_TO_CART.format(food_item_names=added_items)
                return result
            else:
                logger.warning(NO_VALID_FOOD_ITEMS_RESTAURANT)
                result[204] = NO_VALID_FOOD_ITEMS_RESTAURANT
                return result
        elif edit_choice == REMOVE_CHOICE:
            removed_items = remove_items_from_cart(food_item_names, cart)
            if removed_items:
                logger.info(ITEMS_REMOVED_FROM_CART)
                result[200] = ITEMS_REMOVED_FROM_CART.format(removed_items=removed_items)
            else:
                logger.warning(NO_VALID_FOOD_ITEMS_CART)
                result[404] = NO_VALID_FOOD_ITEMS_CART
                return result
        else:
            logger.warning(INVALID_ADD_OR_REMOVE_ITEM_FROM_CART)
            result[400] = INVALID_ADD_OR_REMOVE_ITEM_FROM_CART
            return result
    else:
        logger.warning(NO_PENDING_CART)
        result[404] = NO_PENDING_CART
        return result


def place_my_order(customer_id: str, confirm: str, payment_mode: str):
    result = {}
    cart = get_cart_by_customer(customer_id)
    if not (cart and cart[STATUS] == STATUS_PENDING):
        logger.warning(NO_PENDING_CART)
        result[404] = NO_PENDING_CART
        return result
    if not (confirm.lower() == VALUE_YES or confirm.lower() == VALUE_NO):
        logger.warning(INVALID_CONFIRMATION)
        result.setdefault(400, []).append(INVALID_CONFIRMATION)
    if not (payment_mode.lower() == PAYMENT_MODE_CASH or payment_mode.lower() == PAYMENT_MODE_UPI):
        logger.warning(INVALID_PAYMENT_MODE)
        result.setdefault(400, []).append(INVALID_PAYMENT_MODE)
    if not result:
        if confirm.lower() == VALUE_YES:
            order = place_order(cart, customer_id, payment_mode)
            logger.info(ORDER_PLACED)
            result[200] = ORDER_DETAILS.format(order=order)
            return result
        elif confirm.lower() == VALUE_NO:
            logger.warning(ORDER_NOT_PLACED)
            result[409] = ORDER_NOT_PLACED
            return result
        else:
            logger.warning(INVALID_CHOICE)
            result[400] = INVALID_CHOICE
            return result
    else:
        return result


def rating_delivery(delivery_partner_id: str, rating):
    result = {}
    delivery_partner = get_delivery(delivery_partner_id)
    if not delivery_partner:
        logger.warning(DELIVERY_PARTNER_NOT_FOUND.format(unique_id=delivery_partner_id))
        result[404] = DELIVERY_PARTNER_NOT_FOUND.format(unique_id=delivery_partner_id)
        return result
    if not (rating.isnumeric() and len(rating) == ONE and ONE <= int(rating) <= FIVE):
        logger.warning(INVALID_RATING)
        result[400] = INVALID_RATING
        return result
    is_updated = update_ratings(int(rating), delivery_partner)
    if is_updated:
        logger.info(RATING_UPDATED)
        result[200] = RATING_UPDATED
        return result


def show_my_orders(customer_id):
    result = {}
    customer = get(customer_id)
    if not customer:
        logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
        result[404] = CUSTOMER_NOT_FOUND.format(customer_id=customer_id)
        return result
    orders = get_customer_orders(customer)
    result[200] = f"Customer '{customer['name']}' Orders: {orders}"
    return result


def remove_customer(customer_id):
    result = {}
    is_deleted = remove(customer_id)
    if is_deleted:
        logger.info(CUSTOMER_DELETED.format(customer_id=customer_id))
        result[200] = CUSTOMER_DELETED.format(customer_id=customer_id)
        return result
    else:
        logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
        result[404] = CUSTOMER_NOT_FOUND.format(customer_id=customer_id)
        return result


def show_my_details(customer_id):
    result = {}
    customer = get(customer_id)
    if customer:
        logger.info(customer)
        result[200] = customer
        return result
    else:
        logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
        result[404] = CUSTOMER_NOT_FOUND.format(customer_id=customer_id)
        return result
