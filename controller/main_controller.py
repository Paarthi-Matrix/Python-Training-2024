from constants.biznex_constants import (
    ASCII_OF_ONE,
    ASCII_OF_EIGHT,
    CUSTOMER_CATEGORY_NAME,
    CHOICE_MIN_LENGTH,
    CUSTOMER_VENDOR_CHOICE,
    END_GREETING_MESSAGE,
    INPUT_PLACEHOLDER_MESSAGE,
    INVALID_MESSAGE_FOR_CHOICE,
    INVALID_MESSAGE_FOR_USER_CATEGORY,
    MAIN_MENU_TEXT,
    USER_DICT_USER_ID,
    USER_DICT_USER_PASSWORD,
    VENDOR_CATEGORY_NAME,
    INVALID_MESSAGE_FOR_SEARCH_OPTION,
    ASCII_OF_FIVE,
)
from dao.user_dao import get_by_user_id
from resources.logging_config import logger
from service.user_service import update_password
from user_controller import display_all_users, delete_user, login_user, register_user, get_by_attribute


def start_application():
    """
    Starts the main application loop, displaying the main menu and handling user input.
    """
    logger.debug("Application started.")
    while True:
        print(MAIN_MENU_TEXT)
        choice = input(INPUT_PLACEHOLDER_MESSAGE)

        if ((len(choice) > CHOICE_MIN_LENGTH)
                or (ord(choice) < ASCII_OF_ONE or ord(choice) > ASCII_OF_EIGHT)):
            logger.warning("Invalid choice entered: %s", choice)
            print(INVALID_MESSAGE_FOR_CHOICE)
            continue

        # Handle choices
        if int(choice) == 1:
            logger.info("User chose to register.")
            register()
        elif int(choice) == 2:
            logger.info("User chose to login.")
            login()
        elif int(choice) == 3:
            logger.info("User chose to display all users.")
            print_all_users()
        elif int(choice) == 4:
            logger.info("User chose option 4.")
            change_password()
        elif int(choice) == 5:
            logger.info("User chose option 5.")
            pass
        elif int(choice) == 6:
            logger.info("User chose to delete a user.")
            delete()
        elif int(choice) == 7:
            logger.info("User chose to search.")
            search()
        elif int(choice) == 8:
            logger.info("User chose to exit.")
            print(END_GREETING_MESSAGE)
            break


def register():
    """
    Registers a new user (CUSTOMER or VENDOR) by collecting their details and confirming.
    """
    logger.debug("Entering registration process.")
    while True:
        print(CUSTOMER_VENDOR_CHOICE)
        vendor_customer_choice = input("Select any one option 1 or 2: ")
        if ((len(vendor_customer_choice) > 1)
                or (ord(vendor_customer_choice) < ASCII_OF_ONE
                    or ord(vendor_customer_choice) > ASCII_OF_ONE + 1)):

            logger.warning("Invalid user category choice: %s", vendor_customer_choice)
            print(INVALID_MESSAGE_FOR_USER_CATEGORY)
            continue
        else:
            break

    customer_details = {}
    flag = True
    while flag:
        customer_details["name"] = input("Your full name: ").strip()
        customer_details["phone_number"] = input("Phone Number: ").strip()
        customer_details["email"] = input("Email Address: ").strip()
        customer_details["gender"] = input("Gender (e.g., Male, Female, Others): ").strip()
        customer_details["date_of_birth"] = input("Date of Birth (e.g., DD/MM/YYYY): ").strip()
        customer_details["company_name"] = input("Company Name: ").strip()
        customer_details["company_type"] = input("Company Type (e.g., LLC, Corporation, Small scale): ").strip()
        customer_details["password"] = input(
            "Password (Must be 8 characters long. Use special characters like (!@#$) ): ").strip()

        if int(vendor_customer_choice) == 1:
            customer_details["user_category"] = CUSTOMER_CATEGORY_NAME
        else:
            customer_details["user_category"] = VENDOR_CATEGORY_NAME

        logger.info("User details entered: %s", customer_details)

        print("\nPlease review the details entered:")
        for key, value in customer_details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

        while True:
            confirm = input("\nAre these details correct? (yes/no): ").strip().lower()
            if confirm in ['yes', 'no']:
                if confirm == 'yes':
                    register_user(customer_details)
                    logger.info("User registered successfully: %s", customer_details)
                    flag = False
                    break
                else:
                    logger.info("User chose to re-enter details.")
                    print("\nLet's try entering the details again.")
            else:
                logger.warning("Invalid input for confirmation: %s", confirm)
                print("Invalid input. Please enter 'yes' or 'no'.")


def login():
    """
    Handles user login by collecting login credentials and authenticating the user.
    """
    logger.debug("Entering login process.")
    login_credential = {
        USER_DICT_USER_ID: input("Enter your username: ").strip(),
        USER_DICT_USER_PASSWORD: input("Enter your password: ").strip()
    }
    login_user(login_credential)


def print_all_users():
    """
    Displays all users stored in the system. If no users are found, it notifies the user.
    """
    print_data(display_all_users())


def print_data(user_details):
    try:
        headers = list(user_details[next(iter(user_details))].keys())
    except StopIteration:
        logger.info("No users found in the database.")
        print("No user found in database!")
        return

    print(" | ".join(f"{header.replace('_', ' ').title():<30}" for header in headers))
    print("=" * (len(headers) * 30))

    for user_id, details in user_details.items():
        print(" | ".join(f"{str(details[header]):<30}" for header in headers))


def delete():
    """
    Deletes a user from the system.
    """
    logger.debug("Entering delete user process.")
    delete_user()


def search():
    """
    Allows the user to search for users based on different criteria.
    """
    search_options = {
        "1": "user_id",
        "2": "name",
        "3": "email",
        "4": "phone_number",
        "5": "quit"
    }

    while True:
        print(" 1 - Search By user id")
        print(" 2 - Search By name")
        print(" 3 - Search By e-mail")
        print(" 4 - Search By phone number")
        print(" 5 - Quit Search")

        choice = input("Select any of the above options: ").strip()

        if choice not in search_options:
            logger.warning("Invalid choice entered: %s", choice)
            print(INVALID_MESSAGE_FOR_SEARCH_OPTION)
            continue

        if choice == "5":
            print("Quitting search...")
            logger.debug("Quitting search..")
            break

        attribute_name = search_options[choice]
        search_term = input(f"Enter the value to search for {attribute_name}: ").strip()

        if not search_term:
            logger.warning("Empty search term entered for attribute: %s", attribute_name)
            print("Search term cannot be empty. Please try again.")
            continue

        search_result = get_by_attribute(attribute_name, search_term)
        print(search_result)


def change_password():
    """
    Updates the user's password.

    The function will prompt the user for their user ID and old password.
    If the old password is correct, the user will be prompted to enter a new password.
    The new password will then be updated in the system. If the old password is incorrect,
    an error message will be displayed, and the user will be prompted to try again.
    """
    user_id = input("Enter your user ID: ").strip()
    old_password = input("Enter your old password: ").strip()
    user = get_by_user_id(user_id)

    if user is None:
        logger.error(f"User ID {user_id} not found.")
        print("User ID not found. Please try again.")
        return

    if user[USER_DICT_USER_PASSWORD] != old_password:
        logger.warning(f"User ID {user_id} entered an incorrect old password.")
        print("Incorrect old password. Please try again.")
        return

    new_password = input("Enter your new password: ").strip()
    user[USER_DICT_USER_PASSWORD] = new_password

    update_password(user)
    logger.info(f"Password for user ID {user_id} has been updated successfully.")
    print("Your password has been updated successfully.")


if __name__ == "__main__":
    start_application()
