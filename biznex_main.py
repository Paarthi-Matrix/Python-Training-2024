import json
import os

from tabulate import tabulate

from constants.biznex_constants import (
    APPLICATION_STOPPED,
    ASCII_OF_ONE, CHOICE_MIN_LENGTH,
    CONFORMATION_PROMPT, CUSTOMER_CATEGORY_NAME,
    CUSTOMER_VENDOR_CHOICE, END_GREETING_MESSAGE,
    ENTER_COMPANY_NAME, ENTER_COMPANY_TYPE,
    ENTER_DOB,
    ENTER_GENDER, ENTER_PASSWORD, ENTER_USER_ID,
    ENTER_YOUR_EMAIL, ENTER_YOUR_FULL_NAME,
    ENTER_YOUR_PHONE_NUMBER, EXCEPTION_MESSAGE_FOR_USER_CATEGORY,
    FILE_NOT_FOUND, FILE_PATH,
    INPUT_PLACEHOLDER_MESSAGE, INVALID_CONFIRMATION,
    INVALID_DOB, INVALID_EMAIL,
    INVALID_GENDER, INVALID_MESSAGE_FOR_CHOICE,
    INVALID_MESSAGE_FOR_USER_CATEGORY, INVALID_NAME_FORMATE,
    INVALID_PASSWORD, INVALID_PHONE_NUMBER,
    MAIN_MENU_TEXT, NO_USER_FOUND,
    PREVIEW_ENTRIES, REGISTRATION_SUCCESS_PROMPT,
    SELECT_OPTION_1_TO_2, USER_DETAILS_HEADERS,
    USER_DICT_COMPANY_NAME, USER_DICT_COMPANY_SERVICE,
    USER_DICT_COMPANY_TYPE, USER_DICT_DOB,
    USER_DICT_EMAIL, USER_DICT_GENDER,
    USER_DICT_IS_DELETE, USER_DICT_NAME,
    USER_DICT_PHONE_NUMBER, USER_DICT_USER_CATEGORY,
    USER_DICT_USER_ID, USER_DICT_USER_PASSWORD,
    VALID_PASSWORD_PROMPT, VENDOR_CATEGORY_NAME,
    YES, NO, ASCII_OF_FIVE,
)
from custom_exceptions.id_generation_exception import IdGenerationException  # todo naming
from resources.logging_config import logger  # todo naming
from service.user_service import delete_by_id
from user_controller import (
    get_users,
    load_user,
    login_user,
)
from utils.password_utils import hash_password
from utils.user_input_validation import (
    date_of_birth_validation,
    email_validation,
    gender_validation,
    password_validation,
    phone_number_validation,
    user_name_validation,
)


def start_application():
    """
    Starts the main application loop, displaying the main menu and handling user input.
    """
    logger.debug("Application started.")  # todo change to info
    while True:
        print(MAIN_MENU_TEXT)
        choice = input(INPUT_PLACEHOLDER_MESSAGE)

        if ((len(choice) > CHOICE_MIN_LENGTH)
                or (ord(choice) < ASCII_OF_ONE or ord(choice) > ASCII_OF_FIVE)):
            logger.warning("Invalid choice entered: %s", choice)
            print(INVALID_MESSAGE_FOR_CHOICE)
            continue

        if int(choice) == 1:
            register()
        elif int(choice) == 2:
            login()
        elif int(choice) == 3:
            get_all_users()
        elif int(choice) == 4:
            delete_user()
        elif int(choice) == 5:
            logger.info(APPLICATION_STOPPED)
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
        vendor_customer_choice = input(SELECT_OPTION_1_TO_2)
        if ((len(vendor_customer_choice) > CHOICE_MIN_LENGTH)
                or (ord(vendor_customer_choice) < ASCII_OF_ONE
                    or ord(vendor_customer_choice) > ASCII_OF_ONE + 2)):

            logger.warning("Invalid user category choice: %s", vendor_customer_choice)
            print(INVALID_MESSAGE_FOR_USER_CATEGORY)
            continue
        elif ord(vendor_customer_choice) == (ASCII_OF_ONE + 2):
            return
        else:
            break

    customer_details = {}
    flag = True
    while flag:

        while True:
            customer_name = input(ENTER_YOUR_FULL_NAME).strip()
            if user_name_validation(customer_name):
                customer_details[USER_DICT_NAME] = customer_name
                break
            else:
                logger.warning(f"User gave invalid name formate {customer_name}")
                print(INVALID_NAME_FORMATE)

        while True:
            phone_number = input(ENTER_YOUR_PHONE_NUMBER).strip()
            if phone_number_validation(phone_number):
                customer_details[USER_DICT_PHONE_NUMBER] = phone_number
                break
            else:
                logger.warning(f"User gave invalid phone number {phone_number}")
                print(INVALID_PHONE_NUMBER)

        while True:
            email = input(ENTER_YOUR_EMAIL).strip()
            if email_validation(email):
                customer_details[USER_DICT_EMAIL] = email
                break
            else:
                logger.warning(f"User gave invalid email address {email}")
                print(INVALID_EMAIL)

        while True:
            gender = input(ENTER_GENDER).strip()
            if gender_validation(gender):
                customer_details[USER_DICT_GENDER] = gender
                break
            else:
                logger.warning(f"User gave invalid gender {gender}")
                print(INVALID_GENDER)

        while True:
            dob = input(ENTER_DOB).strip()
            if date_of_birth_validation(dob):
                customer_details[USER_DICT_DOB] = dob
                break
            else:
                logger.warning(f"User gave invalid date {dob}")
                print(INVALID_DOB)

        customer_details[USER_DICT_COMPANY_NAME] = input(ENTER_COMPANY_NAME).strip()
        customer_details[USER_DICT_COMPANY_TYPE] = input(ENTER_COMPANY_TYPE).strip()
        customer_details[USER_DICT_COMPANY_SERVICE] = input(USER_DICT_COMPANY_SERVICE.strip())
        while True:
            password = input(VALID_PASSWORD_PROMPT).strip()
            if password_validation(password):
                password = hash_password(password)
                customer_details[USER_DICT_USER_PASSWORD] = password
                break
            else:
                logger.warning(f"User gave invalid password {password}")
                print(INVALID_PASSWORD)

        if int(vendor_customer_choice) == 1:
            customer_details[USER_DICT_USER_CATEGORY] = CUSTOMER_CATEGORY_NAME
        else:
            customer_details[USER_DICT_USER_CATEGORY] = VENDOR_CATEGORY_NAME

        logger.info("User details entered: %s", customer_details)
        print(PREVIEW_ENTRIES)

        for key, value in customer_details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

        while True:
            confirm = input(CONFORMATION_PROMPT).strip().lower()
            if confirm in [YES, NO]:
                if confirm == YES:
                    try:
                        customer_details[USER_DICT_IS_DELETE] = False
                        load_user(customer_details, False)
                    except IdGenerationException as e:
                        logger.exception(e.message)
                        print(EXCEPTION_MESSAGE_FOR_USER_CATEGORY)

                    logger.info(REGISTRATION_SUCCESS_PROMPT, customer_details)
                    flag = False
                    break
                else:
                    logger.info("User chose to re-enter details.")  # TODO make no possibilities
            else:
                logger.warning("Invalid input for confirmation: %s", confirm)
                print(INVALID_CONFIRMATION)


def login():
    """
    Handles user login by collecting login credentials and authenticating the user.
    """
    logger.debug("Entering login process.")
    login_credential = {
        USER_DICT_USER_ID: input(ENTER_USER_ID).strip(),
        USER_DICT_USER_PASSWORD: input(ENTER_PASSWORD).strip()
    }
    login_user(login_credential)


def get_all_users():
    """
       Retrieves all users and displays their data.

       This function fetches all user records by calling the `get_users` function
       and then displays the user data using the `display_user_data` function.
    """
    users = get_users()
    display_user_data(users)


def delete_user():
    user_id = input(ENTER_USER_ID)
    if delete_by_id(user_id):
        logger.info(f"User {user_id} deleted successfully")
    else:
        logger.error(f"User id {user_id} is not found in database")


def display_user_data(data):
    """
    Displays user data in a tabular format.

    Parameters:
        data (dict): A dictionary containing user information with the user ID as the key.
    """
    table_data = []
    for user_id, user_info in data.items():
        row = [
            user_id,
            user_info.get(USER_DICT_NAME, ''),
            user_info.get(USER_DICT_PHONE_NUMBER, ''),
            user_info.get(USER_DICT_EMAIL, ''),
            user_info.get(USER_DICT_GENDER, ''),
            user_info.get(USER_DICT_DOB, ''),
            user_info.get(USER_DICT_COMPANY_NAME, ''),
            user_info.get(USER_DICT_COMPANY_TYPE, ''),
            user_info.get(USER_DICT_COMPANY_SERVICE, ''),
            user_info.get(USER_DICT_USER_CATEGORY, ''),
            user_info.get(USER_DICT_IS_DELETE, ''),
        ]
        table_data.append(row)

    print(tabulate(table_data, USER_DETAILS_HEADERS, tablefmt="grid"))


def print_data(user_details, is_header=True):
    """
    Prints the data in tabular formate on to the console
    """
    try:
        headers = list(user_details[next(iter(user_details))].keys())
    except StopIteration:
        logger.error(NO_USER_FOUND)
        return

    print(" | ".join(f"{header.replace('_', ' ').title():<30}" for header in headers))
    print("=" * (len(headers) * 30))

    for user_id, details in user_details.items():
        print(" | ".join(f"{str(details[header]):<30}" for header in headers))


def get_user_from_file():
    """
        Yields user details from a JSON file, one user at a time.

        This function reads user details from a file specified by `FILE_PATH`. It checks if the file exists
        and is readable before attempting to open it. For each line in the file, it tries to parse the line
        as JSON and yields the resulting user details. If there is an error decoding the JSON, it logs the
        error and skips to the next line. If the file does not exist or is not readable, or if any other
        unexpected error occurs, it logs the appropriate error message.

        Yields:
            dict: A dictionary containing user details parsed from the JSON file.
    """
    file_path = FILE_PATH  # todo move this to .env
    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        return
    if not os.access(file_path, os.R_OK):
        logger.error(f"File is not readable: {file_path}")
        return
    try:
        with open(file_path, "r") as file:
            for user_details in file:
                try:
                    user = json.loads(user_details.strip())
                    yield user
                except json.JSONDecodeError as e:
                    logger.error(f"Error decoding JSON: {e}")
                    continue  # Skip invalid JSON lines
    except FileNotFoundError:
        logger.fatal(FILE_NOT_FOUND)
    except Exception as e:
        logger.fatal(f"An unexpected error occurred: {e}")


def load_users():
    for user in get_user_from_file():
        load_user(user, True)


if __name__ == "__main__":
    load_users()
    start_application()
