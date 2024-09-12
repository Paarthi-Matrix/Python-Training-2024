# common
import logging

VENDOR_ID_PREFIX = "VEN"
CUSTOMER_ID_PREFIX = "CUST"
VENDOR_CATEGORY_NAME = "VENDOR"
CUSTOMER_CATEGORY_NAME = "CUSTOMER"
COLUMN_SPACE = 40
FILE_PATH = "C:\\Study Material\\Python-Training-2024\\user_creds\\user_creds"

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
USER_DICT_IS_DELETE = "is_deleted"
USER_DICT_COMPANY_SERVICE = "What Kind of service or product you offer (ex: Grocery, Steel, Electronics)?"
CUSTOMER_ID = "Customer_id"
DATE = "date"

# Quotation form dict keys
FORM_ITEMS = "items"
ADDRESS = "delivery_address"
DELIVERY_DATE = "delivery_date"
PO_STATUS = "po_status"
PO_STATUS_SENT = "Sent"
PO_STATUS_VIEW = "Viewed"
PAYMENT_METHOD = "payment_method"
# exception messages
USER_ID_GENERATION_EXCEPTION_MESSAGE = "user_id generation failed. The user category must be either VENDOR or CUSTOMER"
USER_ID_GENERATION_EXCEPTION_DETAIL_MESSAGE = "The actual user_category is '{data}'. Expected 'VENDOR' or 'CUSTOMER'."

# Constant Numerics
CHOICE_MIN_LENGTH = 1
ASCII_OF_ONE = 49
ASCII_OF_FIVE = 53

# user input validation regex
NAME_VALIDATION_REGEX = r"^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
PHONE_NUMBER_VALIDATION_REGEX = r"^\d{10}$"
EMAIL_VALIDATION_REGEX = r"^(\w+)\d+@(?:gmail|ymail)\.(?:com|in)$"
DOB_VALIDATION_REGEX = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
PASSWORD_VALIDATION_REGEX = r"^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$"
NUMBER_REGEX = r"^-?\d+(\.\d+)?$"

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
|    4 - Delete User                              |
|    5 - Exit Application                         |
==================================================
"""
CUSTOMER_QUOTATION_EDIT = """
==== Kindly enter the field you need to edit ===
| 1 . Email
| 2 . Phone Number
| 3 . Items
| 4 . Delivery date
| 5 . Address
| 6.  Edit items and their quantities
| 7.  Save
"""

CUSTOMER_MENU = """
===================================================
|                                                 |
|           Welcome back dear customer            |
|                                                 |
==================================================
|    Kindly give the choice to continue:          |
|    1 - Warehouse Management                     |
|    2 - Vendor & P2P Management                  |
|    3 - Back                                     |              
==================================================
"""

VENDOR_MENU = """
===================================================
|                                                 |
|           Welcome back dear vendor              |
|                                                 |
==================================================
|    Kindly give the choice to continue:          |
|    1 - View Customer quotation                  |
|    2 - Give Quotation                           |
|    3 - Update purchase order status             |
|    4 - Get purchase order                       |
|    5 - Back                                     |
==================================================
"""

PO_STATUS_UPDATE_PROMPT = """
|=============================|
|   Enter the status options  |
|=============================|
| 1 . Product shipped         |
| 2 . PO cancelled            |
| 3 . Processing              |
| 4 . Out for delivery        |
| 5 . Delivered               |                   |
===============================
"""

PO_STATUS_ITEM_SHIPPED = "Item shipped"
PO_STATUS_CANCELLED = "Cancelled"
PO_STATUS_PROCESSING = "Processing"
PO_STATUS_OUT_FOR_DELIVERY = "Out for delivery"
PO_STATUS_DELIVERED = "Delivered"

WAREHOUSE_MANAGEMENT = """
1. View Warehouse
2. Add item to warehouse
3. Delete Item from warehouse
4. Update stocks
5. Create A Ware House.
6. Back
"""

VENDOR_P2P_MANAGEMENT = """
1. Request Quotation 
2. View active vendor quotations
3. Issue Purchase Order
4. View Purchase order 
5. Edit Quotation
6. Edit Purchase order 
7. View all vendor quotations
8. Back
"""

APPLICATION_STOPPED = "Application stopped"
SELECT_OPTION_1_TO_2 = "Select any one option 1 or 2: "
ENTER_YOUR_FULL_NAME = "Your full name (First name and Last name) Last name must not be initial: "
ENTER_YOUR_PHONE_NUMBER = "Phone Number: "
ENTER_YOUR_EMAIL = "Your email address: "
ENTER_VENDOR_MAIL_ID = "Enter vendor mail id"
ENTER_GENDER = "Gender (e.g., Male, Female, Others): "
ENTER_DOB = "Date of Birth (e.g., DD/MM/YYYY): "
ENTER_COMPANY_NAME = "Company Name: "
ENTER_COMPANY_TYPE = "Company Type (e.g., LLC, Corporation, Small scale): "
ENTER_USER_EMAIL = "Enter your E-mail: "
ENTER_PASSWORD = "Enter your password: "
YES = "yes"
NO = "no"
ENTER_CUSTOMER_QUOTATION_ID = "Enter your customer quotation id to continue"
ENTER_VENDOR_QUOTATION_ID = "Enter the vendor quotation id to continue:"
ENTER_YOUR_CHOICE = "Enter your choice"
ENTER_YOUR_WAREHOUSE_ID = "Enter the warehouse id to proceed"
ENTER_YOUR_VENDOR_ID = "Enter the vendor id"
ENTER_YOUR_USER_ID = "Enter your User ID: "
ENTER_ITEMS = "Enter item name (or 'done' to finish): "
ENTER_DELIVERY_DATE = "Enter the delivery date (DD/MM/YYYY): "
ENTER_DELIVERY_ADDRESS = "Enter the delivery address: "
ENTER_PAYMENT_METHOD = "Enter the payment method (bank transfer, credit card, cheque): "
ENTER_PO_NUMBER = "Enter the purchase order number"
ENTER_PHONE_NUMBER = "Enter phone number: "
INVALID_NUMBER_ERROR = "User gave invalid quantity. Must be a number"
SUCCESSFUL_QUOTATION_UPDATE = "Quotation details updated successfully"
STATUS = "Status"
STATUS_SENT = "Sent"
STATUS_PROCESSING = "Processing"
STATUS_SEEN = "Seen"
STATUS_INACTIVE = "Inactive"
DONE = 'done'
VENDOR_ID = "vendor_id"
VENDOR_QUOTATION_ID = "vendor_quotation_id"
CUSTOMER_QUOTATION_ID = "customer_quotation_id"
TOTAL_PRICE = "total_price"
QUANTITY_NOT_ZERO = "Please enter a valid quantity (integer). And must not be 0"
PAST_DELIVERY_DATE = "The delivery date cannot be in the past. Please enter a future date."

INVALID_MESSAGE_FOR_CHOICE = "Invalid input. Please enter the numbers only (1 to 8)!"
INVALID_MESSAGE_FOR_USER_CATEGORY = "Invalid input. Please enter the numbers only (1 to 2)!"
INVALID_MESSAGE_FOR_SEARCH_OPTION = "Invalid input. Please enter the numbers only (1 to 4)!"
INPUT_PLACEHOLDER_MESSAGE = "Please select an option (1-5): "
INVALID_PAYMENT_METHOD = ("Invalid payment method. Please enter one of the following: bank transfer, credit card, "
                          "cheque.")
END_GREETING_MESSAGE = "Thank you!..."
CUSTOMER_VENDOR_CHOICE = """
Do you wish to register as customer or vendor? 
1 - Customer
2 - Vendor
3 - Back
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
8. What Kind of service or product you offer (ex: Grocery, Steel, Electronics)? 
9. Password (Must be 8 characters long. Used some special characters like (!@#$) ):
"""

# Prompt Messages
VALID_PASSWORD_PROMPT = "Password (Must be 8 characters long. Use special characters like (!@#$) ): "
PREVIEW_ENTRIES = "\nPlease review the details entered:"
CONFORMATION_PROMPT = "\nAre these details correct? (yes/no): "
REGISTRATION_SUCCESS_PROMPT = "User registered successfully: %s"
RE_ENTER_THE_FORM = "\nLet's try entering the details again."
ITEM_NAME_PROMPT = "Enter the item name"
ITEM_QUANTITY_PROMPT = "Enter the item's Quantity can be in units"
CRITICAL_LEVEL_PROMPT = "Enter the critical unit where you will be notified in case of low stock of this item"
ITEM_NUMBER_PROMPT = "Enter the item number to be continue"
ITEM_DELETION_PROMPT = "Item deleted successfully!"
QUANTITY_TO_BE_CHANGES = "Enter the quantity to be increased. To decrease give in negative "

# Invalid Error messages
INVALID_CREDENTIAL_MESSAGE = "Invalid credentials. Check the user name and password"
EXCEPTION_MESSAGE_FOR_USER_CATEGORY = "Invalid user category. Kindly check the user_category."
INVALID_NAME_FORMATE = ("Invalid name format. The name contains First name and last name. "
                        "Last name must not be initial.")
INVALID_PHONE_NUMBER = "Invalid phone number format. Please enter a valid phone number."
INVALID_EMAIL = "Invalid email format. Please enter a valid email address."
INVALID_GENDER = "Invalid gender. Please enter Male, Female, or Others."
INVALID_DOB = "Invalid date of birth format. Please enter in DD/MM/YYYY format."
INVALID_PASSWORD = "Invalid password. Please ensure it's 8 characters long and contains special characters (!@#$)."
INVALID_CONFIRMATION = "Invalid input. Please enter 'yes' or 'no'."
INVALID_ITEM_QUANTITY = "Invalid item quantity, Must be a number"
INVALID_CRITICAL_LEVEL = "Invalid critical level for the item. It must be a number and greater than the item quantity"

# keys for warehouse dict
ITEM_NAME = "item_name"
ITEM_QUANTITY = "item_quantity"
ITEM_STATUS = "item_status"
ITEM_CRITICAL_LEVEL = "critical_level"
CUSTOMER_QUOTATION_NUMBER = "customer_quotation_number"

# Warehouse constants
ITEM_STATUS_AVAILABLE = "Available"
ITEM_STATUS_NOT_AVAILABLE = "Not available"
ITEM_STATUS_CRITICAL = "Critically low stock"
DELIVERY_ADDRESS = "delivery_address"
# loggers message
INVALID_CRITICAL_LEVEL_LOGGER = ("User entered invalid critical level, it must be a number and greater than the item "
                                 "quantity")
WAREHOUSE_ITEM_ZERO_LOGGER = "The changes in item will make the item quantity below zero(0)"
VALID_PAYMENT_METHODS = ["bank transfer", "credit card", "cheque"]
CUSTOMER_QUOTATION_ITEM_HEADERS = ['Item ID', 'Item Name', 'Item Quantity', 'Item Status', 'Critical Level']
USER_DETAILS_HEADERS = ['User ID', 'Name', 'Phone Number', 'Email', 'Gender', 'Date of Birth', 'Company Name',
                        'Company Type', 'Service/Product Offered', 'User Category', 'Is Deleted']
FILE_NOT_FOUND = "File not found to load the data to dictionary"
NO_USER_FOUND = "No users found in the database."
NO_ACTIVE_QUOTATION = "No active quotations available"
YOUR_ACTIVE_QUOTATIONS = "Your Active Quotations are listed below"
SELECT_ONE_QUOTATION = "Select one quotation to generate your quotation"
ENTER_TOTAL_PRICE = "Enter the total price"
VALID_TOTAL_PRICE_ERROR = "User entered invalid total price. Must be number"
INVALID_DATE_FORMATE = "Invalid date format. Please enter the date in 'DD/MM/YYYY' format."
GENDER_CATEGORY = ["male", "female", "others"]
PURCHASE_ORDER_EDIT = """
|=============================|
|                             |
| 1 . Change delivery address | 
| 2 . Update PO status        |
| 3 . Update payment method   |
| 4 . Save                    |
|=============================|
"""

CUSTOMER_QUOTATION_HEADERS = [CUSTOMER_QUOTATION_ID, VENDOR_ID, USER_DICT_NAME, USER_DICT_EMAIL, USER_DICT_PHONE_NUMBER,
                              USER_DICT_COMPANY_NAME, STATUS, FORM_ITEMS,
                              DELIVERY_DATE, DELIVERY_ADDRESS]
VENDOR_QUOTATION_HEADERS = [VENDOR_QUOTATION_ID, CUSTOMER_QUOTATION_ID, USER_DICT_NAME, USER_DICT_EMAIL,
                            USER_DICT_PHONE_NUMBER, TOTAL_PRICE, DATE, VENDOR_ID, STATUS]
LOGGER_LEVEL = logging.DEBUG
INVALID_CHOICE_OF_MAIN = "Invalid choice Please enter the numbers from 1 to 5 only"
NAME_ERROR = "user_name_error"
PHONE_NUMBER_ERROR = "phone_number_error"
EMAIL_ERROR = "email_error"
GENDER_ERROR = "gender_error"
DOB_ERROR = "dob_error"
PASSWORD_ERROR = "password_error"
USER_DETAILS_COUNT = 11
INVALID_ENTRIES = "Invalid entries"
UNAUTHORIZED_USER = "Some Un authorized user accessed"
UNEXPECTED_ERROR = "Somthing went wrong"
LOG_FILE_PATH = "C:\Study Material"
ANONYMOUS_CATEGORY = "Anonymous"
LOOP_LIMIT = 3
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NOT_FOUND_CODE = 404
BAD_REQUEST_CODE = 400
UN_PROCESSABLE_ENTITY = 422
OK_STATUS = 200
INVALID_DELTA = "Invalid delta value. Must be a number"
ITEM_UPDATED = "Item successfully updated"
VENDOR_EMAIL = "vendor_email"
VENDOR_QUOTATION_NOT_FOUND = "No vendor quotation is available for your given quotation"
STATUS_VIEWED = "viewed"

