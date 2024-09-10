from common.constant import (
    PICK_CHOICE, INPUT_NAME, EXITING,
    INPUT_EMAIL, INPUT_LOCATION, INPUT_CONTACT, INVALID_CHOICE,
    INVALID_INPUT, INPUT_ALTERNATE_CONTACT,
    INPUT_PASSWORD, NAME_UPDATED, EMAIL_UPDATED, INPUT_ID,
    MOBILE_NUMBER_UPDATED, LOCATION_UPDATED, ZERO, ONE, TWO,
    THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, PASSWORD_UPDATED, PASSWORD_KEY,
    INPUT_RESTAURANT_ID, INPUT_FOOD_PRICE, INPUT_FOOD_NAME,
    RESTAURANT_ADDED_SUCCESSFULLY, INVALID_NAME, INVALID_EMAIL,
    INVALID_CONTACT, INVALID_LOCATION, UNABLE_TO_ADD_FOOD,
    FOOD_ADDED_SUCCESSFULLY, FOOD_ALREADY_EXISTS,
    RESTAURANT_NOT_FOUND, FOOD_UPDATED_SUCCESSFULLY,
    FOOD_NOT_FOUND, FOOD_DELETED_SUCCESSFULLY,
    RESTAURANT_CHOICE, INVALID_PASSWORD, NAME_KEY,
    LOCATION_KEY, EMAIL_KEY, RESTAURANT_DELETED,
    RESTAURANT_UPDATE_CHOICE, UPDATE_RESTAURANT_NOT_FOUND,
    INVALID_PRICE, CONTACT_KEY
)
from resources.config import logger
from service.restaurant_service import (
    get, remove,update, add, add_food_item,
    get_menu, update_food_item_details, delete_food_item_details
)
from utils.utils import (
    is_valid_email, is_valid_mobile, is_valid_name,
    is_valid_password, update_entity, input_validation
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


def create_restaurant():
    """
    Prompts the user to input details for creating a new restaurant and adds it.
    """
    name = input_validation(INPUT_NAME, is_valid_name, INVALID_NAME)
    password = input_validation(INPUT_PASSWORD, is_valid_password, INVALID_PASSWORD)
    email = input_validation(INPUT_EMAIL, is_valid_email, INVALID_EMAIL)
    contact_numbers = []
    primary_contact = input_validation(INPUT_CONTACT, is_valid_mobile, INVALID_CONTACT)
    contact_numbers.append(primary_contact)
    alternate_contact = input_validation(INPUT_ALTERNATE_CONTACT,
                                         lambda value: value.isnumeric() and int(value) == ZERO or is_valid_mobile(
                                             value),
                                         INVALID_CONTACT)
    if alternate_contact.isnumeric() and int(alternate_contact) != ZERO:
        contact_numbers.append(alternate_contact)
    location = input_validation(INPUT_LOCATION, is_valid_name, INVALID_LOCATION)
    unique_id = add(name.lower(), password, email.lower(), contact_numbers, location.lower())
    logger.info(RESTAURANT_ADDED_SUCCESSFULLY.format(name=name, id=unique_id))


def restaurant_operations():
    """
    Handles restaurant operations based on user input.

    This function continuously prompts the user to select and perform
    restaurant-related operations such as adding a restaurant,
    managing food items, showing the menu, or exiting the application.
    It validates user input and logs any errors or warnings.
    """
    while True:
        try:
            print(RESTAURANT_CHOICE)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == ONE and ZERO <= int(choice) <= EIGHT):
                raise ValueError
            choice = int(choice)
            if choice == ONE:
                create_restaurant()
            elif choice == TWO:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant = get(restaurant_id)
                if restaurant:
                    while True:
                        name = input(INPUT_FOOD_NAME)
                        if is_valid_name(name):
                            break
                        else:
                            logger.warning(INVALID_NAME)
                    while True:
                        price = input(INPUT_FOOD_PRICE)
                        if price.isnumeric():
                            break
                        else:
                            logger.warning(INVALID_PRICE)
                    is_added = add_food_item(
                        restaurant_id, name.lower(), float(price)
                    )
                    if is_added:
                        logger.info(FOOD_ADDED_SUCCESSFULLY.
                                    format(restaurant_id=restaurant_id))
                    else:
                        logger.warning(FOOD_ALREADY_EXISTS.format(name=name))
                else:
                    logger.warning(UNABLE_TO_ADD_FOOD.
                                   format(restaurant_id=restaurant_id))
            elif choice == THREE:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant_menu = get_menu(restaurant_id)
                logger.info(
                    restaurant_menu
                ) if restaurant_menu else logger.warning(
                    RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
            elif choice == FOUR:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant = get(restaurant_id)
                if restaurant:
                    while True:
                        name = input(INPUT_FOOD_NAME)
                        if is_valid_name(name):
                            break
                        else:
                            logger.warning(INVALID_NAME)
                    while True:
                        price = input(INPUT_FOOD_PRICE)
                        if price.isnumeric():
                            break
                        else:
                            logger.warning(INVALID_PRICE)
                    updated = update_food_item_details(restaurant_id, name.lower(), float(price))
                    if updated:
                        logger.info(FOOD_UPDATED_SUCCESSFULLY.format(name=name))
                    else:
                        logger.warning(FOOD_NOT_FOUND)
                else:
                    logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
            elif choice == FIVE:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant = get(restaurant_id)
                if restaurant:
                    while True:
                        name = input(INPUT_FOOD_NAME)
                        if is_valid_name(name):
                            break
                        else:
                            logger.warning(INVALID_NAME)
                    is_deleted = delete_food_item_details(restaurant_id, name.lower())
                    if is_deleted:
                        logger.info(FOOD_DELETED_SUCCESSFULLY)
                    else:
                        logger.warning(FOOD_NOT_FOUND.format(name=name))
                else:
                    logger.warning(RESTAURANT_NOT_FOUND.format(
                        restaurant_id=restaurant_id
                    ))
            elif choice == SIX:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant = get(restaurant_id)
                if restaurant:
                    logger.info(restaurant)
                else:
                    logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
            elif choice == SEVEN:
                unique_id = input(INPUT_RESTAURANT_ID)
                is_deleted = remove(unique_id)
                if is_deleted:
                    logger.info(RESTAURANT_DELETED.format(unique_id=unique_id))
                else:
                    logger.warning(RESTAURANT_NOT_FOUND.format(restaurant_id=unique_id))
            elif choice == EIGHT:
                update_restaurant()
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)
