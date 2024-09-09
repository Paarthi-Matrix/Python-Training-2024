from common.common_constants import (
    PICK_CHOICE, INPUT_NAME, EXITING,
    INPUT_EMAIL, INPUT_LOCATION, INPUT_CONTACT, INVALID_CHOICE,
    INVALID_INPUT, INPUT_PASSWORD, NAME_UPDATED, EMAIL_UPDATED, INPUT_ID,
    MOBILE_NUMBER_KEY, MOBILE_NUMBER_UPDATED,
    LOCATION_UPDATED, STATUS, STATUS_PENDING, ADD_CHOICE,
    REMOVE_CHOICE, ZERO, ONE, TWO,
    THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, ELEVEN,
    TWELVE, PASSWORD_UPDATED, PASSWORD_KEY,
    INVALID_CONFIRMATION, INVALID_PAYMENT_MODE
)
from common.customer_constants import (
    CUSTOMER_UPDATE_CHOICE, UPDATE_CUSTOMER_NOT_FOUND, CUSTOMER_ADDED,
    CUSTOMER_CHOICE, INPUT_CUSTOMER_ID, ALREADY_HAVE_PENDING_CART,
    ITEMS_ADDED_TO_CART, CUSTOMER_NOT_FOUND, NO_CART_FOUND,
    ADD_OR_REMOVE_ITEM_FROM_CART, ITEMS_REMOVED_FROM_CART,
    NO_VALID_FOOD_ITEMS_CART, INVALID_ADD_OR_REMOVE_ITEM_FROM_CART,
    NO_PENDING_CART, CUSTOMER_DELETED, ORDER_NOT_PLACED,
    VALUE_NO, ORDER_DETAILS, ORDER_PLACED, VALUE_YES, PAYMENT_MODE_CASH,
    PAYMENT_MODE_UPI, INPUT_PAYMENT_MODE,
    INPUT_WANT_TO_PLACE_ORDER)
from common.delivery_person_constants import (
    INPUT_DELIVERY_PERSON_ID, INPUT_RATING, RATING_UPDATED,
    INVALID_RATING, DELIVERY_PERSON_NOT_FOUND
)
from common.restaurant_constants import (
    INPUT_RESTAURANT_ID, INVALID_NAME, INVALID_EMAIL,
    INVALID_CONTACT, INVALID_LOCATION, RESTAURANT_NOT_FOUND,
    INVALID_PASSWORD, NAME_KEY, LOCATION_KEY, EMAIL_KEY,
    INPUT_FOOD_NAME_LIST, NO_VALID_FOOD_ITEMS_RESTAURANT
)
from resources.logging_config import logger
from service.customer_service import (
    get_cart_by_customer_id, remove_items_from_cart,
    place_order, add_to_cart, update_items_to_cart, get_by_id,
    remove_customer, update_customer_details, get_all_orders, add_new_customer
)
from service.delivery_person_service import (
    update_ratings, get_delivery_person_by_id)
from service.restaurant_service import (
    find_by_id, get_all_restaurants, get_restaurant_menu)
from utils.validator import (
    is_valid_email, is_valid_mobile, is_valid_name,
    is_valid_password, update_entity, input_validation
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
    while True:
        try:
            print(CUSTOMER_UPDATE_CHOICE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric() and len(choice) == ONE and ZERO <= int(choice) <= FIVE):
                raise ValueError
            choice = int(choice)

            if choice in range(ONE, SIX):
                unique_id = input(INPUT_ID)
                customer = get_by_id(unique_id)
                if customer:
                    if choice == ONE:
                        pass
                    elif choice == TWO:
                        update_entity(customer, NAME_KEY, INPUT_NAME, is_valid_name, NAME_UPDATED, INVALID_NAME,
                                      update_customer_details)
                        update_entity(customer, EMAIL_KEY, INPUT_EMAIL, is_valid_email, EMAIL_UPDATED, INVALID_EMAIL,
                                      update_customer_details)
                    elif choice == THREE:
                        update_entity(customer, MOBILE_NUMBER_KEY, INPUT_CONTACT, is_valid_mobile,
                                      MOBILE_NUMBER_UPDATED, INVALID_CONTACT, update_customer_details)
                    elif choice == FOUR:
                        update_entity(customer, LOCATION_KEY, INPUT_LOCATION, is_valid_name, LOCATION_UPDATED,
                                      INVALID_LOCATION, update_customer_details)
                    elif choice == FIVE:
                        update_entity(customer, PASSWORD_KEY, INPUT_PASSWORD, is_valid_password, PASSWORD_UPDATED,
                                      INVALID_PASSWORD, update_customer_details)
                else:
                    logger.warning(UPDATE_CUSTOMER_NOT_FOUND.format(unique_id=unique_id))
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)


def create_customer():
    """
    Prompts the user to input details for creating a new customer and adds them.
    """
    name = input_validation(INPUT_NAME, is_valid_name, INVALID_NAME)
    password = input_validation(INPUT_PASSWORD, is_valid_password, INVALID_PASSWORD)
    email = input_validation(INPUT_EMAIL, is_valid_email, INVALID_EMAIL)
    mobile_number = input_validation(INPUT_CONTACT, is_valid_mobile, INVALID_CONTACT)
    location = input_validation(INPUT_LOCATION, is_valid_name, INVALID_LOCATION)
    customer_id = add_new_customer(name.lower(), password, email.lower(),
                                   mobile_number, location.lower())
    logger.info(CUSTOMER_ADDED.format(customer_id=customer_id))


def customer_operations():
    """
    Handles customer operations based on user input.

    This function continuously prompts the user to select and
    perform customer-related operations such as adding
    a new customer or exiting the application.
    It validates user input and logs any errors or warnings.
    """
    while True:
        try:
            print(CUSTOMER_CHOICE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and ONE <= len(choice) <= TWO and ZERO <= int(choice) <= TWELVE):
                raise ValueError
            choice = int(choice)
            if choice == ONE:
                create_customer()
            elif choice == TWO:
                logger.info(get_all_restaurants())
            elif choice == THREE:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant_menu = get_restaurant_menu(restaurant_id)
                logger.info(
                    restaurant_menu
                ) if restaurant_menu else logger.warning(
                    RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
            elif choice == FOUR:
                customer_id = input(INPUT_CUSTOMER_ID)
                customer = get_by_id(customer_id)
                if customer:
                    existing_cart = get_cart_by_customer_id(customer_id)
                    if existing_cart and existing_cart[STATUS] == STATUS_PENDING:
                        logger.warning(ALREADY_HAVE_PENDING_CART)
                    else:
                        restaurant_id = input(INPUT_RESTAURANT_ID)
                        restaurant = find_by_id(restaurant_id)
                        if restaurant:
                            food_item_names = input(INPUT_FOOD_NAME_LIST).split(", ")
                            added_cart = add_to_cart(customer_id, restaurant, restaurant_id, food_item_names)
                            if added_cart:
                                logger.info(ITEMS_ADDED_TO_CART.format(food_item_names=food_item_names))
                            else:
                                logger.warning(NO_VALID_FOOD_ITEMS_RESTAURANT)
                        else:
                            logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
                else:
                    logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
            elif choice == FIVE:
                customer_id = input(INPUT_CUSTOMER_ID)
                cart = get_cart_by_customer_id(customer_id)
                if cart:
                    logger.info(f"Cart ID {cart['id']} for Customer {customer_id}: {cart}")
                else:
                    logger.warning(NO_CART_FOUND.format(customer_id=customer_id))
            elif choice == SIX:
                customer_id = input(INPUT_CUSTOMER_ID)
                cart = get_cart_by_customer_id(customer_id)
                if cart and cart[STATUS] == STATUS_PENDING:
                    edit_choice = input(ADD_OR_REMOVE_ITEM_FROM_CART).lower()
                    if edit_choice == ADD_CHOICE:
                        food_item_names = input(INPUT_FOOD_NAME_LIST).split(", ")
                        added_items = update_items_to_cart(food_item_names, cart)
                        if added_items:
                            logger.info(ITEMS_ADDED_TO_CART)
                        else:
                            logger.warning(NO_VALID_FOOD_ITEMS_RESTAURANT)
                    elif edit_choice == REMOVE_CHOICE:
                        food_item_names = input(INPUT_FOOD_NAME_LIST).split(", ")
                        removed_items = remove_items_from_cart(food_item_names, cart)
                        if removed_items:
                            logger.info(ITEMS_REMOVED_FROM_CART)
                        else:
                            logger.warning(NO_VALID_FOOD_ITEMS_CART)
                    else:
                        logger.warning(INVALID_ADD_OR_REMOVE_ITEM_FROM_CART)
                else:
                    logger.warning(NO_PENDING_CART)
            elif choice == SEVEN:
                customer_id = input(INPUT_CUSTOMER_ID)
                cart = get_cart_by_customer_id(customer_id)
                if cart and cart[STATUS] == STATUS_PENDING:
                    while True:
                        confirm = input(INPUT_WANT_TO_PLACE_ORDER)
                        if confirm.lower() == VALUE_YES or confirm.lower() == VALUE_NO:
                            break
                        else:
                            logger.warning(INVALID_CONFIRMATION)
                    while True:
                        payment_mode = input(INPUT_PAYMENT_MODE)
                        if payment_mode.lower() == PAYMENT_MODE_CASH or payment_mode.lower() == PAYMENT_MODE_UPI:
                            break
                        else:
                            logger.warning(INVALID_PAYMENT_MODE)
                    if confirm.lower() == VALUE_YES:
                        order = place_order(cart, customer_id, payment_mode)
                        logger.info(ORDER_PLACED)
                        logger.info(ORDER_DETAILS.format(order=order))
                    elif confirm.lower() == VALUE_NO:
                        logger.warning(ORDER_NOT_PLACED)
                    else:
                        logger.warning(INVALID_CHOICE)
                else:
                    logger.warning(NO_PENDING_CART)
            elif choice == EIGHT:
                delivery_person_id = input(INPUT_DELIVERY_PERSON_ID)
                delivery_person = get_delivery_person_by_id(delivery_person_id)
                if delivery_person:
                    while True:
                        rating = input(INPUT_RATING)
                        if rating.isnumeric() and len(rating) == ONE and ONE <= int(rating) <= FIVE:
                            break
                        else:
                            logger.warning(INVALID_RATING)
                    is_updated = update_ratings(int(rating), delivery_person)
                    if is_updated:
                        logger.info(RATING_UPDATED)
                else:
                    logger.warning(DELIVERY_PERSON_NOT_FOUND.format(unique_id=delivery_person_id))
            elif choice == NINE:
                customer_id = input(INPUT_ID)
                customer = get_by_id(customer_id)
                if customer:
                    orders = get_all_orders()
                    logger.info(
                        f"Customer '{customer['name']}' Orders: {[orders[order_id] for order_id in customer['orders']]}")
                else:
                    logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
            elif choice == TEN:
                update_customer()
            elif choice == ELEVEN:
                customer_id = input(INPUT_CUSTOMER_ID)
                is_deleted = remove_customer(customer_id)
                if is_deleted:
                    logger.info(CUSTOMER_DELETED.format(customer_id=customer_id))
                else:
                    logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
            elif choice == TWELVE:
                customer_id = input(INPUT_CUSTOMER_ID)
                customer = get_by_id(customer_id)
                if customer:
                    logger.info(customer)
                else:
                    logger.warning(CUSTOMER_NOT_FOUND.format(customer_id=customer_id))
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)
