from common.common_constants import (
    AUTH_CUSTOMER, AUTH_RESTAURANT, EXIT_APPLICATION,
    PICK_CHOICE, INPUT_NAME, EXITING,
    INPUT_EMAIL, INPUT_LOCATION, INPUT_CONTACT, INVALID_CHOICE
)
from common.customer_constants import (
    ADD_CUSTOMER, SEARCH_RESTAURANT, PLACE_ORDER,
    CANCEL_ORDER, SHOW_MY_ORDER
)
from common.restaurant_constants import (
    ADD_RESTAURANT, ADD_FOOD_ITEM, SHOW_MENU,
    UPDATE_FOOD_ITEM, REMOVE_FOOD_ITEM, INPUT_RESTAURANT_ID,
    RESTAURANT_CONTACT_COUNT, INPUT_FOOD_PRICE, INPUT_FOOD_NAME
)
from controller.customer_controller import CustomerController
from controller.restaurant_controller import (
    add_restaurant, add_food_item, get_menu,
    update_food_item, delete_food_item
)
from utils.validator import is_valid_email

customer_controller = CustomerController()


def pick_role():
    print(AUTH_CUSTOMER)
    print(AUTH_RESTAURANT)
    print(EXIT_APPLICATION)


def customer_choice():
    print(ADD_CUSTOMER)
    print(SEARCH_RESTAURANT)
    print(PLACE_ORDER)
    print(CANCEL_ORDER)
    print(SHOW_MY_ORDER)
    print(EXIT_APPLICATION)


def restaurant_choice():
    print(ADD_RESTAURANT)
    print(ADD_FOOD_ITEM)
    print(SHOW_MENU)
    print(UPDATE_FOOD_ITEM)
    print(REMOVE_FOOD_ITEM)
    print(EXIT_APPLICATION)


def customer_operations():
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
                print(INVALID_CHOICE)
        except ValueError:
            print("Invalid Input Enter your Choice"
                  " as Numeric Value Between 0 to 6")


def restaurant_operations():
    while True:
        try:
            restaurant_choice()
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == 1 and 0 <= int(choice) <= 5):
                raise ValueError
            choice = int(choice)
            if choice == 1:
                name = input(INPUT_NAME)
                email = input(INPUT_EMAIL)
                if not is_valid_email(email):
                    raise ValueError
                contact_count = input(RESTAURANT_CONTACT_COUNT)
                if not (contact_count.isnumeric() and len(contact_count) == 1
                        and 1 <= int(contact_count) <= 2):
                    raise ValueError("Enter Your choice as numeric")
                contact_numbers = []
                for _ in range(int(contact_count)):
                    contact_number = input(INPUT_CONTACT)
                    contact_numbers.append(contact_number.lower())
                location = input(INPUT_LOCATION)
                id = add_restaurant(
                    name, email, contact_numbers, location
                )
                print(f"Restaurant '{name}' created successfully"
                      f" with ID {id}.")
            elif choice == 2:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                name = input(INPUT_FOOD_NAME)
                price = float(input(INPUT_FOOD_PRICE))
                is_added = add_food_item(
                    restaurant_id, name, price
                )
                print(
                    f"Food Item Added Successfully to Restaurant with"
                    f" id :{restaurant_id}"
                ) if is_added else print(
                    "Unable to Save Food Item"
                )
            elif choice == 3:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                print(get_menu(restaurant_id))
            elif choice == 4:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                name = input(INPUT_FOOD_NAME)
                price = float(input(INPUT_FOOD_PRICE))
                updated = update_food_item(restaurant_id, name, price)
                if updated is None:
                    print(f"Restaurant with this id:"
                          f" {restaurant_id} not found to update")
                elif updated:
                    print(f"Food item with name: {name}"
                          f" updated Successfully")
                else:
                    print(f"Food item with this name: {name}"
                          f" not found to update")
            elif choice == 5:
                restaurant_id = input(INPUT_RESTAURANT_ID)
                name = input(INPUT_FOOD_NAME)
                is_deleted = delete_food_item(restaurant_id, name)
                print(is_deleted)
            elif choice == 0:
                print(EXITING)
                break
            else:
                print(INVALID_CHOICE)
        except ValueError:
            print("Invalid Input Enter your Choice"
                  " as Numeric Value Between 0 to 5")


def chow_now():
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
                print(INVALID_CHOICE)
        except ValueError:
            print("Invalid Input Enter your Choice"
                  " as Numeric Value Between 0 to 2")


if __name__ == "__main__":
    chow_now()
