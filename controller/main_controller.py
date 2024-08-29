from constants.biznex_constants import (
    ASCII_OF_EIGHT,
    ASCII_OF_ONE,
    CHOICE_MIN_LENGTH,
    CUSTOMER_CATEGORY_NAME,
    CUSTOMER_VENDOR_CHOICE,
    END_GREETING_MESSAGE,
    INPUT_PLACEHOLDER_MESSAGE,
    INVALID_MESSAGE_FOR_CHOICE,
    INVALID_MESSAGE_FOR_SEARCH_OPTION,
    INVALID_MESSAGE_FOR_USER_CATEGORY,
    MAIN_MENU_TEXT,
    USER_DICT_COMPANY_NAME,
    USER_DICT_COMPANY_TYPE,
    USER_DICT_DOB,
    USER_DICT_EMAIL,
    USER_DICT_GENDER,
    USER_DICT_NAME,
    USER_DICT_PHONE_NUMBER,
    USER_DICT_USER_ID,
    USER_DICT_USER_PASSWORD,
    VENDOR_CATEGORY_NAME, EXCEPTION_MESSAGE_FOR_USER_CATEGORY, USER_DICT_USER_CATEGORY
)

from custom_exceptions.id_generation_exception import IdGenerationException
from dao.user_dao import get_by_user_id
from resources.logging_config import logger
from service.user_service import update_password
from user_controller import (
    delete_user,
    display_all_users,
    get_by_attribute,
    login_user,
    register_user
)
from utils.user_input_validation import (
    user_name_validation,
    password_validation,
    email_validation,
    date_of_birth_validation,
    gender_validation,
    phone_number_validation
)


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
    Validations for input fields are done.
    For more in formation on input validation see :class:`user_input_validation`
    in the module mod:`utils`
    """
    logger.debug("Entering registration process.")
    while True:
        print(CUSTOMER_VENDOR_CHOICE)
        vendor_customer_choice = input("Select any one option 1 or 2: ")
        if ((len(vendor_customer_choice) > CHOICE_MIN_LENGTH)
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

        while True:
            customer_name = input("Your full name: ").strip()
            if user_name_validation(customer_name):
                customer_details[USER_DICT_NAME] = customer_name
                break
            else:
                logger.warning(f"User gave invalid name formate {customer_name}")
                print("Invalid name format. Please enter a valid full name.")

        while True:
            phone_number = input("Phone Number: ").strip()
            if phone_number_validation(phone_number):
                customer_details[USER_DICT_PHONE_NUMBER] = phone_number
                break
            else:
                logger.warning(f"User gave invalid phone number {phone_number}")
                print("Invalid phone number format. Please enter a valid phone number.")

        while True:
            email = input("Email Address: ").strip()
            if email_validation(email):
                customer_details[USER_DICT_EMAIL] = email
                break
            else:
                logger.warning(f"User gave invalid email address {email}")
                print("Invalid email format. Please enter a valid email address.")

        while True:
            gender = input("Gender (e.g., Male, Female, Others): ").strip()
            if gender_validation(gender):
                customer_details[USER_DICT_GENDER] = gender
                break
            else:
                logger.warning(f"User gave invalid gender {gender}")
                print("Invalid gender. Please enter Male, Female, or Others.")

        while True:
            dob = input("Date of Birth (e.g., DD/MM/YYYY): ").strip()
            if date_of_birth_validation(dob):
                customer_details[USER_DICT_DOB] = dob
                break
            else:
                logger.warning(f"User gave invalid date {dob}")
                print("Invalid date of birth format. Please enter in DD/MM/YYYY format.")

        customer_details[USER_DICT_COMPANY_NAME] = input("Company Name: ").strip()
        customer_details[USER_DICT_COMPANY_TYPE] = input("Company Type (e.g., LLC, Corporation, "
                                                         "Small scale): ").strip()

        while True:
            password = input("Password (Must be 8 characters long."
                             " Use special characters like (!@#$) ): ").strip()
            if password_validation(password):
                customer_details[USER_DICT_USER_PASSWORD] = password
                break
            else:
                logger.warning(f"User gave invalid password {password}")
                print("Invalid password. Please ensure it's 8 characters long "
                      " and contains special characters (!@#$).")

        if int(vendor_customer_choice) == 1:
            customer_details[USER_DICT_USER_CATEGORY] = CUSTOMER_CATEGORY_NAME
        else:
            customer_details[USER_DICT_USER_CATEGORY] = VENDOR_CATEGORY_NAME

        logger.info("User details entered: %s", customer_details)

        print("\nPlease review the details entered:")
        for key, value in customer_details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

        while True:
            confirm = input("\nAre these details correct? (yes/no): ").strip().lower()
            if confirm in ['yes', 'no']:
                if confirm == 'yes':
                    try:
                        register_user(customer_details)
                    except IdGenerationException as e:
                        logger.exception(e.message)
                        print(EXCEPTION_MESSAGE_FOR_USER_CATEGORY)

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


def print_data(user_details, is_header=True):
    """
    Prints the data in tabular formate on to the console
    """
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
        return

    new_password = input("Enter your new password: ").strip()
    user[USER_DICT_USER_PASSWORD] = new_password

    update_password(user)
    logger.info(f"Password for user ID {user_id} has been updated successfully.")


if __name__ == "__main__":
    start_application()
