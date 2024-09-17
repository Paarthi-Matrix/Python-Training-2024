import traceback

from config.config import logger
from constant.constant import (
    PICK_CHOICE, INPUT_NAME, EXITING, INPUT_EMAIL, INPUT_LOCATION,
    INPUT_CONTACT, INVALID_CHOICE, INVALID_INPUT, INPUT_PASSWORD,
    NAME_UPDATED, EMAIL_UPDATED, INPUT_ID, MOBILE_NUMBER_UPDATED,
    LOCATION_UPDATED, ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX,
    PASSWORD_UPDATED, PASSWORD_KEY, RESTAURANT_ADDED_SUCCESSFULLY,
    INVALID_NAME, INVALID_EMAIL, INVALID_CONTACT, INVALID_LOCATION,
    INVALID_PASSWORD, NAME_KEY, LOCATION_KEY, EMAIL_KEY,
    RESTAURANT_UPDATE_CHOICE, UPDATE_RESTAURANT_NOT_FOUND, CONTACT_KEY,
    UNABLE_TO_ADD_FOOD, INVALID_PRICE, FOOD_ADDED_SUCCESSFULLY,
    FOOD_ALREADY_EXISTS, RESTAURANT_NOT_FOUND, FOOD_UPDATED_SUCCESSFULLY,
    FOOD_NOT_FOUND, FOOD_DELETED_SUCCESSFULLY, RESTAURANT_DELETED
)
from service.restaurant import (
    get, update, add, add_food_item, get_menu, update_food_item_details,
    delete_food_item_details, remove
)
from validation.validation import (
    is_valid_email, is_valid_mobile, is_valid_name,
    is_valid_password, update_entity, input_validation, is_valid_location
)


def update_restaurant():
    """
    Manages the update process for restaurant details based on user input.

    Prompts the user to select the detail to update and performs the update
    if the restaurant is found. Uses `handle_update` for updating specific
    fields of the restaurant.

    The user is prompted to select from updating the name, email, contact number,
    location, or password. Handles invalid choices and restaurant not found scenarios.
    """
    while True:
        try:
            print(RESTAURANT_UPDATE_CHOICE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == ONE and ZERO <= int(choice) <= FIVE):
                raise ValueError
            choice = int(choice)

            if choice in range(ONE, SIX):
                unique_id = input(INPUT_ID)
                restaurant = get(unique_id)
                if restaurant:
                    if choice == ONE:
                        update_entity(restaurant, NAME_KEY, INPUT_NAME, is_valid_name, NAME_UPDATED, INVALID_NAME,
                                      update)
                    elif choice == TWO:
                        update_entity(restaurant, EMAIL_KEY, INPUT_EMAIL, is_valid_email, EMAIL_UPDATED, INVALID_EMAIL,
                                      update)
                    elif choice == THREE:
                        update_entity(restaurant, CONTACT_KEY, INPUT_CONTACT, is_valid_mobile, MOBILE_NUMBER_UPDATED,
                                      INVALID_CONTACT, update)
                    elif choice == FOUR:
                        update_entity(restaurant, LOCATION_KEY, INPUT_LOCATION, is_valid_name, LOCATION_UPDATED,
                                      INVALID_LOCATION, update)
                    elif choice == FIVE:
                        update_entity(restaurant, PASSWORD_KEY, INPUT_PASSWORD, is_valid_password, PASSWORD_UPDATED,
                                      INVALID_PASSWORD, update)
                else:
                    logger.warning(UPDATE_RESTAURANT_NOT_FOUND.format(unique_id=unique_id))
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)


def create_restaurant(name, password, email, primary_contact, alternate_contact, location):
    """
    Prompts the user to input details for creating a new restaurant and adds it.
    """
    result = {}
    try:
        restaurant_name = input_validation(name, is_valid_name, INVALID_NAME)
        restaurant_password = input_validation(password, is_valid_password, INVALID_PASSWORD)
        restaurant_email = input_validation(email, is_valid_email, INVALID_EMAIL)
        contact_numbers = []
        restaurant_primary_contact = input_validation(primary_contact, is_valid_mobile, INVALID_CONTACT)
        contact_numbers.append(primary_contact)
        restaurant_alternate_contact = input_validation(alternate_contact,
                                                        lambda value: value.isnumeric() and int(
                                                            value) == ZERO or is_valid_mobile(
                                                            value),
                                                        INVALID_CONTACT)
        if alternate_contact.isnumeric() and int(alternate_contact) != ZERO:
            contact_numbers.append(alternate_contact)
        restaurant_location = input_validation(location, is_valid_location, INVALID_LOCATION)
        if restaurant_name != name:
            result.setdefault(400, []).append(restaurant_name)
        if restaurant_password != password:
            result.setdefault(400, []).append(restaurant_password)
        if restaurant_email != email:
            result.setdefault(400, []).append(restaurant_email)
        if restaurant_primary_contact != primary_contact:
            result.setdefault(400, []).append(restaurant_primary_contact)
        if restaurant_alternate_contact != alternate_contact:
            result.setdefault(400, []).append(restaurant_alternate_contact)
        if restaurant_location != location:
            result.setdefault(400, []).append(restaurant_location)
        if not result:
            unique_id = add(name.lower(), password, email.lower(), contact_numbers, location.lower())
            logger.info(RESTAURANT_ADDED_SUCCESSFULLY.format(name=name, id=unique_id))
            result[200] = RESTAURANT_ADDED_SUCCESSFULLY.format(name=name, id=unique_id)
            return result
        else:
            return result
    except ValueError as ve:
        logger.error(f"Value Error Occurred: {str(ve)}\n{traceback.format_exc()}")
        result[400] = "Incorrect Value"
        return result


def add_food_to_restaurant(restaurant_id: str, name, price):
    result = {}
    restaurant = get(restaurant_id)
    if not restaurant:
        logger.warning(UNABLE_TO_ADD_FOOD.
                       format(restaurant_id=restaurant_id))
        result[404] = UNABLE_TO_ADD_FOOD.format(restaurant_id=restaurant_id)
        return result
    food_item_name = input_validation(name, is_valid_name, INVALID_NAME)
    food_item_price = input_validation(price, lambda value: value.isnumeric(), INVALID_PRICE)
    if food_item_name != name:
        result.setdefault(400, []).append(food_item_name)
    if food_item_price != price:
        result.setdefault(400, []).append(food_item_price)
    if not result:
        is_added = add_food_item(
            restaurant_id, name.lower(), float(price)
        )
        if is_added:
            logger.info(FOOD_ADDED_SUCCESSFULLY.
                        format(restaurant_id=restaurant_id))
            result[200] = FOOD_ADDED_SUCCESSFULLY.format(restaurant_id=restaurant_id)
            return result
        else:
            logger.warning(FOOD_ALREADY_EXISTS.format(name=name))
            result[409] = FOOD_ALREADY_EXISTS.format(name=name)
            return result
    else:
        return result


def fetch_restaurant_menu(restaurant_id: str):
    result = {}
    restaurant_menu = get_menu(restaurant_id)
    if restaurant_menu:
        logger.info(restaurant_menu)
        result[200] = restaurant_menu
        return result
    else:
        logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
        result[404] = RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id)
        return result


def update_food_item(restaurant_id: str, name, price):
    result = {}
    restaurant = get(restaurant_id)
    if not restaurant:
        logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
        result[404] = RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id)
        return result
    food_item_name = input_validation(name, is_valid_name, INVALID_NAME)
    food_item_price = input_validation(price, price.isnumeric, INVALID_PRICE)
    if food_item_name != name:
        result.setdefault(400, []).append(food_item_name)
    if food_item_price != price:
        result.setdefault(400, []).append(food_item_price)
    if not result:
        is_updated = update_food_item_details(restaurant_id, name.lower(), float(price))
        if is_updated:
            logger.info(FOOD_UPDATED_SUCCESSFULLY.format(name=name))
            result[200] = FOOD_UPDATED_SUCCESSFULLY.format(name=name)
            return result
        else:
            logger.warning(FOOD_NOT_FOUND)
            result[404] = FOOD_NOT_FOUND
            return result
    else:
        return result


def remove_food_item(restaurant_id: str, name):
    result = {}
    restaurant = get(restaurant_id)
    if not restaurant:
        logger.warning(RESTAURANT_NOT_FOUND.format(
            restaurant_id=restaurant_id
        ))
        result[404] = RESTAURANT_NOT_FOUND.format(
            restaurant_id=restaurant_id)
        return result
    food_item_name = input_validation(name, is_valid_name, INVALID_NAME)
    if food_item_name != name:
        result.setdefault(400, []).append(food_item_name)
    is_deleted = delete_food_item_details(restaurant_id, name.lower())
    if is_deleted:
        logger.info(FOOD_DELETED_SUCCESSFULLY)
        result[200] = FOOD_DELETED_SUCCESSFULLY
        return result
    else:
        logger.warning(FOOD_NOT_FOUND.format(name=name))
        result[404] = FOOD_NOT_FOUND.format(name=name)
        return result


def get_restaurant(restaurant_id: str):
    result = {}
    restaurant = get(restaurant_id)
    if restaurant:
        logger.info(restaurant)
        result[200] = restaurant
        return result
    else:
        logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
        result[404] = RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id)
        return result


def remove_restaurant(unique_id: str):
    result = {}
    is_deleted = remove(unique_id)
    if is_deleted:
        logger.info(RESTAURANT_DELETED.format(unique_id=unique_id))
        result[200] = RESTAURANT_DELETED.format(unique_id=unique_id)
        return result
    else:
        logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=unique_id))
        result[404] = RESTAURANT_NOT_FOUND.format(restaurant_id=unique_id)
        return result
