# common
VENDOR_ID_PREFIX = "VEN"
CUSTOMER_ID_PREFIX = "CUST"
VENDOR_CATEGORY_NAME = "VENDOR"
CUSTOMER_CATEGORY_NAME = "CUSTOMER"
COLUMN_SPACE = 40

#  user dict key names
USER_DICT_NAME = "name"
USER_DICT_PHONE_NUMBER = "phone_number"
USER_DICT_EMAIL = "email"
USER_DICT_GENDER = "gender"
USER_DICT_DOB = "date_of_birth"
USER_DICT_COMPANY_NAME = "company_name"
USER_DICT_COMPANY_TYPE = "company_type"
USER_DICT_USER_CATEGORY = "user_category"
USER_DICT_USER_ID = "user_id"
USER_DICT_USER_PASSWORD = "password"

# exception messages
USER_ID_GENERATION_EXCEPTION_MESSAGE = "user_id generation failed. The user category must be either VENDOR or CUSTOMER"
USER_ID_GENERATION_EXCEPTION_DETAIL_MESSAGE = "The actual user_category is '{data}'. Expected 'VENDOR' or 'CUSTOMER'."

# Constant Numerics
CHOICE_MIN_LENGTH = 1
ASCII_OF_ONE = 49
ASCII_OF_FIVE = 53
ASCII_OF_EIGHT = 57


# user input validation regex
NAME_VALIDATION_REGEX = r"^[A-Za-z\s]{2,50}$"
PHONE_NUMBER_VALIDATION_REGEX = r"^\d{10}$"
EMAIL_VALIDATION_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"
DOB_VALIDATION_REGEX = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
PASSWORD_VALIDATION_REGEX = r"^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$"


# Print Menu and UI components
MAIN_MENU_TEXT = """
===================================================
|                                                 |
|                      BizNex                     |
|                                                 |
==================================================
|    Kindly give the choice to continue:          |
|    1 - Register User                            |
|    2 - Login User                               |
|    3 - View User                                |
|    4 - Change Password                          |
|    5 - Give Quotation to customer               |
|    6 - Delete User                              |
|    7 - Search User                              |
|    8 - Exit Application                         |
==================================================
"""
INVALID_MESSAGE_FOR_CHOICE = "Invalid input. Please enter the numbers only (1 to 8)!"
INVALID_MESSAGE_FOR_USER_CATEGORY = "Invalid input. Please enter the numbers only (1 to 2)!"
INVALID_MESSAGE_FOR_SEARCH_OPTION = "Invalid input. Please enter the numbers only (1 to 4)!"
INPUT_PLACEHOLDER_MESSAGE = "Please select an option (1-8): "
END_GREETING_MESSAGE = "Thank you!..."
CUSTOMER_VENDOR_CHOICE = """
Do you wish to register as customer or vendor? 
1 - Customer
2 - Vendor
"""
USER_FORM_INPUTS = """
Please enter the following details:

1. Your full name:
2. Phone Number:
3. Email Address:
4. Gender (e.g., Male, Female, Others):
5. Date of Birth (e.g., DD/MM/YYYY):
6. Company Name:
7. Company Type (e.g., LLC, Corporation, Small scale):
8. Password (Must be 8 characters long. Used some special characters like (!@#$) ):
"""
INVALID_CREDENTIAL_MESSAGE = "Invalid credentials. Check the user name and password"
EXCEPTION_MESSAGE_FOR_USER_CATEGORY = "Invalid user category. Kindly check the user_category."
