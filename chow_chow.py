import traceback

from constant.constant import (
    INPUT_OTP, INPUT_ORDER_ID, DELIVERY_PARTNER_CHOICE, ROLE, NINE, TEN,
    ELEVEN, TWELVE, CUSTOMER_CHOICE, INPUT_CUSTOMER_ID,
    ADD_OR_REMOVE_ITEM_FROM_CART, INPUT_DELIVERY_PARTNER_ID, INPUT_RATING,
    INPUT_FOOD_NAME_LIST
)
from config.config import logger
from constant.constant import (
    PICK_CHOICE, EXITING, INVALID_CHOICE, INVALID_INPUT, INPUT_ID, ZERO, ONE,
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, INPUT_RESTAURANT_ID,
    INPUT_FOOD_PRICE, INPUT_FOOD_NAME, RESTAURANT_CHOICE, INPUT_NAME,
    INPUT_PASSWORD, INPUT_EMAIL, INPUT_CONTACT, INPUT_LOCATION,
    INPUT_WANT_TO_PLACE_ORDER, INPUT_PAYMENT_MODE, INPUT_LICENSE_NUMBER,
    INPUT_ALTERNATE_CONTACT
)
from controller.customer import (
    create_customer, update_customer, get_all_restaurants, get_restaurant_menu,
    add_food_to_cart, view_cart, update_cart, place_my_order, rating_delivery,
    show_my_orders, remove_customer, show_my_details
)
from controller.delivery import (
    create_delivery, update_delivery, get_available_orders,
    assign_delivery, pick_order, complete_order, get_my_details
)
from controller.restaurant import (
    update_restaurant, create_restaurant, add_food_to_restaurant,
    fetch_restaurant_menu, update_food_item, remove_food_item,
    get_restaurant, remove_restaurant
)
from validation.validation import (
    continue_operations
)


def delivery_operations():
    print(DELIVERY_PARTNER_CHOICE)
    choice = input(PICK_CHOICE)
    if not (choice.isnumeric()
            and len(choice) == ONE and ZERO <= int(choice) <= SEVEN):
        raise ValueError
    choice = int(choice)
    if choice == ONE:
        name = input(INPUT_NAME)
        password = input(INPUT_PASSWORD)
        email = input(INPUT_EMAIL)
        mobile_number = input(INPUT_CONTACT)
        location = input(INPUT_LOCATION)
        license_number = input(INPUT_LICENSE_NUMBER)
        result = create_delivery(name, password, email, mobile_number, location, license_number)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: Bad Request,\n message: {value}")
    elif choice == TWO:
        update_delivery()
    elif choice == THREE:
        unique_id = input(INPUT_DELIVERY_PARTNER_ID)
        result = get_available_orders(unique_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message:{value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == FOUR:
        unique_id = input(INPUT_DELIVERY_PARTNER_ID)
        order_id = input(INPUT_ORDER_ID)
        result = assign_delivery(unique_id, order_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message:{value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == FIVE:
        unique_id = input(INPUT_DELIVERY_PARTNER_ID)
        result = pick_order(unique_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message:{value}")
        if key == 204:
            print(f"status: 204,\n success: NO CONTENT,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == SIX:
        delivery_partner_id = input(INPUT_DELIVERY_PARTNER_ID)
        otp = input(INPUT_OTP)
        result = complete_order(delivery_partner_id, otp)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message:{value}")
        if key == 204:
            print(f"status: 204,\n success: NO CONTENT,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: Bad Request,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
        if key == 409:
            print(f"status: 409,\n error: CONFLICT,\n message: {value}")
    elif choice == SEVEN:
        unique_id = input(INPUT_DELIVERY_PARTNER_ID)
        result = get_my_details(unique_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message:{value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == ZERO:
        return
    else:
        logger.warning(INVALID_CHOICE)
    continue_operations(delivery_operations)


def customer_operations():
    """
    Handles customer operations based on user input.

    This function continuously prompts the user to select and
    perform customer-related operations such as adding
    a new customer or exiting the application.
    It validates user input and logs any errors or warnings.
    """
    print(CUSTOMER_CHOICE)
    choice = input(PICK_CHOICE)
    if not (choice.isnumeric()
            and ONE <= len(choice) <= TWO and ZERO <= int(choice) <= TWELVE):
        raise ValueError
    choice = int(choice)
    if choice == ONE:
        name = input(INPUT_NAME)
        password = input(INPUT_PASSWORD)
        email = input(INPUT_EMAIL)
        mobile_number = input(INPUT_CONTACT)
        location = input(INPUT_LOCATION)
        result = create_customer(name, password, email, mobile_number, location)
        key, value = result.popitem()
        if key == 400:
            print(f"status: 400,\n error: Bad Request,\n message: {value}")
        elif key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
    elif choice == TWO:
        print(get_all_restaurants())
    elif choice == THREE:
        restaurant_id = input(INPUT_RESTAURANT_ID)
        result = get_restaurant_menu(restaurant_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        elif key == 404:
            print(f"status: 404,\n error: NOT FOUND,"
                  f"\n message: {value}")
    elif choice == FOUR:
        customer_id = input(INPUT_CUSTOMER_ID)
        restaurant_id = input(INPUT_RESTAURANT_ID)
        food_item_names = input(INPUT_FOOD_NAME_LIST).split(", ")
        result = add_food_to_cart(customer_id, restaurant_id, food_item_names)
        key, value = result.popitem()
        if key == 409:
            print(f"status: 409,\n error: CONFLICT,\n message: {value}")
        elif key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        elif key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == FIVE:
        customer_id = input(INPUT_CUSTOMER_ID)
        result = view_cart(customer_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        elif key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == SIX:
        customer_id = input(INPUT_CUSTOMER_ID)
        edit_choice = input(ADD_OR_REMOVE_ITEM_FROM_CART).lower()
        food_item_names = input(INPUT_FOOD_NAME_LIST).lower().split(", ")
        result = update_cart(customer_id, edit_choice, food_item_names)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        elif key == 204:
            print(f"status: 204,\n success: NO CONTENT,\n message: {value}")
        elif key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
        elif key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == SEVEN:
        customer_id = input(INPUT_CUSTOMER_ID)
        confirm = input(INPUT_WANT_TO_PLACE_ORDER)
        payment_mode = input(INPUT_PAYMENT_MODE)
        result = place_my_order(customer_id, confirm, payment_mode)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
        if key == 409:
            print(f"status: 409,\n error: CONFLICT,\n message: {value}")
    elif choice == EIGHT:
        delivery_partner_id = input(INPUT_DELIVERY_PARTNER_ID)
        rating = input(INPUT_RATING)
        result = rating_delivery(delivery_partner_id, rating)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == NINE:
        customer_id = input(INPUT_ID)
        result = show_my_orders(customer_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == TEN:
        update_customer()
    elif choice == ELEVEN:
        customer_id = input(INPUT_CUSTOMER_ID)
        result = remove_customer(customer_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == TWELVE:
        customer_id = input(INPUT_CUSTOMER_ID)
        result = show_my_details(customer_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == ZERO:
        return
    else:
        logger.warning(INVALID_CHOICE)
    continue_operations(customer_operations)


def restaurant_operations():
    """
    Handles restaurant operations based on user input.

    This function continuously prompts the user to select and perform
    restaurant-related operations such as adding a restaurant,
    managing food items, showing the menu, or exiting the application.
    It validates user input and logs any errors or warnings.
    """
    print(RESTAURANT_CHOICE)
    choice = input(PICK_CHOICE)
    if not (choice.isnumeric()
            and len(choice) == ONE and ZERO <= int(choice) <= EIGHT):
        raise ValueError
    choice = int(choice)
    if choice == ONE:
        name = input(INPUT_NAME)
        password = input(INPUT_PASSWORD)
        email = input(INPUT_EMAIL)
        primary_contact = input(INPUT_CONTACT)
        alternate_contact = input(INPUT_ALTERNATE_CONTACT)
        location = input(INPUT_LOCATION)
        result = create_restaurant(name, password, email, primary_contact, alternate_contact, location)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
    elif choice == TWO:
        restaurant_id = input(INPUT_RESTAURANT_ID)
        name = input(INPUT_FOOD_NAME)
        price = input(INPUT_FOOD_PRICE)
        result = add_food_to_restaurant(restaurant_id, name, price)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
        if key == 409:
            print(f"status: 409,\n error: CONFLICT,\n message: {value}")
    elif choice == THREE:
        restaurant_id = input(INPUT_RESTAURANT_ID)
        result = fetch_restaurant_menu(restaurant_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == FOUR:
        restaurant_id = input(INPUT_RESTAURANT_ID)
        name = input(INPUT_FOOD_NAME)
        price = input(INPUT_FOOD_PRICE)
        result = update_food_item(restaurant_id, name, price)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == FIVE:
        restaurant_id = input(INPUT_RESTAURANT_ID)
        name = input(INPUT_FOOD_NAME)
        result = remove_food_item(restaurant_id, name)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 400:
            print(f"status: 400,\n error: BAD REQUEST,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == SIX:
        restaurant_id = input(INPUT_RESTAURANT_ID)
        result = get_restaurant(restaurant_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == SEVEN:
        unique_id = input(INPUT_RESTAURANT_ID)
        result = remove_restaurant(unique_id)
        key, value = result.popitem()
        if key == 200:
            print(f"status: 200,\n success: OK,\n message: {value}")
        if key == 404:
            print(f"status: 404,\n error: NOT FOUND,\n message: {value}")
    elif choice == EIGHT:
        update_restaurant()
    elif choice == ZERO:
        return
    else:
        logger.warning(INVALID_CHOICE)
    continue_operations(restaurant_operations)


def chow_now():
    """
    Main function to start the application and handle role selection.

    This function allows the user to pick a role (customer or restaurant)
    and then directs them to the appropriate set of operations.
    The function continues to loop until the user decides to exit the application.
    """
    access = True
    while access:
        try:
            print(ROLE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == ONE and ZERO <= int(choice) <= THREE):
                raise ValueError
            choice = int(choice)
            match choice:
                case 1:
                    customer_operations()
                case 2:
                    restaurant_operations()
                case 3:
                    delivery_operations()
                case 0:
                    print(EXITING)
                    break
                case _:
                    print(INVALID_CHOICE)
        except ValueError as ve:
            logger.error(f"Invalid Input {str(ve)}\n{traceback.format_exc()}")
            print(f"Invalid Input {str(ve)}\n{traceback.format_exc()}")
        except KeyError as ke:
            logger.error(f"Invalid Input {str(ke)}\n{traceback.format_exc()}")


if __name__ == "__main__":
    chow_now()
