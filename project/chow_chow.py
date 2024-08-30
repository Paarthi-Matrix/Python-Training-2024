from common.common_constants import (
    PICK_CHOICE, INPUT_NAME, EXITING,
    INPUT_EMAIL, INPUT_LOCATION, INPUT_CONTACT, INVALID_CHOICE,
    INVALID_INPUT, ENTER_CHOICE_AS_NUMERIC, AUTHORIZATION
)
from common.customer_constants import (
    CUSTOMER_CHOICE
)
from common.restaurant_constants import (
    INPUT_RESTAURANT_ID,
    RESTAURANT_CONTACT_COUNT, INPUT_FOOD_PRICE, INPUT_FOOD_NAME,
    RESTAURANT_ADDED_SUCCESSFULLY, INVALID_NAME, INVALID_EMAIL,
    INVALID_CONTACT, INVALID_LOCATION, UNABLE_TO_ADD_FOOD,
    FOOD_ADDED_SUCCESSFULLY, FOOD_ALREADY_EXISTS,
    RESTAURANT_NOT_FOUND, FOOD_UPDATED_SUCCESSFULLY,
    FOOD_NOT_FOUND, FOOD_DELETED_SUCCESSFULLY, RESTAURANT_CHOICE
)
from controller.customer_controller import CustomerController
from controller.restaurant_controller import (
    add_restaurant, add_food_item, get_menu,
    update_food_item, delete_food_item
)
from resources.logging_config import logger
from utils.validator import is_valid_email, is_valid_mobile, is_valid_name

customer_controller = CustomerController()


def pick_role():
    """
    Displays the options for selecting a role: Customer, Restaurant, or Exit.

    This function prints out the choices for the user to either authenticate
    as a customer,authenticate as a restaurant, or exit the application.
    """
    print(AUTHORIZATION)


def customer_choice():
    """
    Displays the available operations for a customer.

    This function prints out the options for customer-related operations
    such as adding a new customer,searching for a restaurant,
    placing an order, canceling an order, showing orders,
    or exiting the application.
    """
    print(CUSTOMER_CHOICE)


def restaurant_choice():
    """
    Displays the available operations for a restaurant.

    This function prints out the options for restaurant-related operations
    such as adding a new restaurant,adding a food item, showing the menu,
    updating a food item, removing a food item, or exiting the application.
    """
    print(RESTAURANT_CHOICE)


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
            customer_choice()
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == 1 and 0 <= int(choice) <= 6):
                raise ValueError
            choice = int(choice)
            if choice == 1:
                name = input(INPUT_NAME)
                email = input(INPUT_EMAIL)
                contact_number = input(INPUT_CONTACT)
                location = input(INPUT_LOCATION)
                customer = customer_controller.add_new_customer(
                    name, email, contact_number, location
                )
                print(customer)
            elif choice == 0:
                print(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError as ve:
            logger.error(INVALID_INPUT)


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
            restaurant_choice()
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == 1 and 0 <= int(choice) <= 5):
                raise ValueError
            choice = int(choice)
            if choice == 1:
                while True:
                    name = input(INPUT_NAME)
                    if is_valid_name(name):
                        break
                    else:
                        logger.warning(INVALID_NAME)
                while True:
                    email = input(INPUT_EMAIL)
                    if is_valid_email(email):
                        break
                    else:
                        logger.warning(INVALID_EMAIL)
                while True:
                    contact_count = input(RESTAURANT_CONTACT_COUNT)
                    if (contact_count.isnumeric() and len(contact_count) == 1
                            and 1 <= int(contact_count) <= 2):
                        break
                    else:
                        logger.warning(ENTER_CHOICE_AS_NUMERIC)
                contact_numbers = []
                count = 0
                while count < int(contact_count):
                    contact_number = input(INPUT_CONTACT)
                    if is_valid_mobile(contact_number):
                        contact_numbers.append(contact_number.lower())
                        count += 1
                    else:
                        logger.warning(INVALID_CONTACT)
                    if len(contact_numbers) == int(contact_count):
                        break
                while True:
                    location = input(INPUT_LOCATION)
                    if is_valid_name(location):
                        break
                    else:
                        logger.warning(INVALID_LOCATION)
                id = add_restaurant(
                    name, email, contact_numbers, location
                )
                logger.info(RESTAURANT_ADDED_SUCCESSFULLY.format(name=name, id=id))
            elif choice == 2:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                while True:
                    name = input(INPUT_FOOD_NAME)
                    if is_valid_name(name):
                        break
                    else:
                        logger.warning(INVALID_NAME)
                price = float(input(INPUT_FOOD_PRICE))
                is_added = add_food_item(
                    restaurant_id, name, price
                )
                if is_added is None:
                    logger.warning(UNABLE_TO_ADD_FOOD.
                                   format(restaurant_id=restaurant_id))
                elif is_added:
                    logger.info(FOOD_ADDED_SUCCESSFULLY.
                                format(restaurant_id=restaurant_id))
                else:
                    logger.warning(FOOD_ALREADY_EXISTS.format(name=name))
            elif choice == 3:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                restaurant_menu = get_menu(restaurant_id)
                logger.info(
                    restaurant_menu
                ) if restaurant_menu else logger.warning(
                    RESTAURANT_NOT_FOUND.format(restaurant_id=restaurant_id))
            elif choice == 4:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                while True:
                    name = input(INPUT_FOOD_NAME)
                    if is_valid_name(name):
                        break
                    else:
                        logger.warning(INVALID_NAME)
                price = float(input(INPUT_FOOD_PRICE))
                updated = update_food_item(restaurant_id, name, price)
                if updated is None:
                    logger.warning(RESTAURANT_NOT_FOUND)
                elif updated:
                    logger.info(FOOD_UPDATED_SUCCESSFULLY.format(name=name))
                else:
                    logger.warning(FOOD_NOT_FOUND)
            elif choice == 5:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                while True:
                    name = input(INPUT_FOOD_NAME)
                    if is_valid_name(name):
                        break
                    else:
                        logger.warning(INVALID_NAME)
                is_deleted = delete_food_item(restaurant_id, name)
                if is_deleted is None:
                    logger.warning(RESTAURANT_NOT_FOUND.format(
                        restaurant_id=restaurant_id
                    ))
                elif is_deleted:
                    logger.info(FOOD_DELETED_SUCCESSFULLY)
                else:
                    logger.warning(FOOD_NOT_FOUND.format(name=name))
            elif choice == 0:
                print(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError as e:
            logger.error(INVALID_INPUT)


def chow_now():
    """
    Main function to start the application and handle role selection.

    This function allows the user to pick a role (customer or restaurant)
    and then directs them to the appropriate set of operations.
    The function continues to loop until the user decides to exit the application.
    """
    while True:
        try:
            pick_role()
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == 1 and 0 <= int(choice) <= 2):
                raise ValueError
            choice = int(choice)
            if choice == 1:
                customer_operations()
            elif choice == 2:
                restaurant_operations()
            elif choice == 0:
                print(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError as e:
            logger.error(INVALID_INPUT)


if __name__ == "__main__":
    chow_now()
