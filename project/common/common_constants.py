# Regex
EMAIL_REGEX = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
MOBILE_NUMBER_REGEX = r"^[6-9]\d{9}$"
NAME_REGEX = r"^[A-Za-z\s\-']+$"
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
LICENSE_REGEX =r'^[A-Z]{2}[0-9]{2}[0-9]{4}[0-9]{7}$|^[A-Z]{2}[0-9]{13}$'

LOCATION_REGEX = r"\b(?:Adyar|Anna Nagar|T. Nagar|Velachery|Nungambakkam|Kodambakkam|Mylapore|Besant Nagar|Royapettah|Triplicane|Guindy|Saidapet|Chromepet|Tambaram|Perungudi|Pallavaram|Thiruvanmiyur|Sholinganallur|Vadapalani|Kotturpuram|Egmore|Ambattur|Ashok Nagar|Alwarpet|Thiruvottiyur|Porur|Perambur|Teynampet|Mount Road|Mandaveli|Kottivakkam|Madipakkam|Kovilambakkam|Kandanchavadi|Aminjikarai|Taramani|Ramapuram|Padi)\b"


# Auth
AUTHORIZATION = '''
==================================
          WELCOME TO CHOWNOW       
==================================
Please select your role:
----------------------------------
1. Customer
2. Restaurant Owner
3. Delivery Person
0. Exit
----------------------------------
Enter your choice (0-3): '''

# Common Prompts
EXITING = "Exiting...."

# Pick Choice
PICK_CHOICE = "Enter Your Choice: "
INVALID_CHOICE = "Invalid Choice, Enter the valid input.."

# Variable Constants
INPUT_ID = "Enter Your id:"
INPUT_NAME = "Enter the Name: "
INPUT_EMAIL = "Enter the Email: "
INPUT_CONTACT = "Enter the Mobile Number: "
INPUT_ALTERNATE_CONTACT = "Enter your alternate contact number (optional, Enter 0 to skip): "
INPUT_LOCATION = "Enter the Location: "
INPUT_LICENSE_NUMBER = "Enter your license number: "
INPUT_PASSWORD = '''
Please enter a strong password that meets the following requirements:
- At least 8 characters long.
- Contains at least one uppercase letter (A-Z).
- Contains at least one lowercase letter (a-z).
- Contains at least one number (0-9).
- Contains at least one special character (e.g., @$!%*?&).
Example: P@ssw0rd1
'''
INPUT_OTP = "Enter OTP to verify delivery: "
# error messages
INVALID_INPUT = "Invalid Input"
ENTER_CHOICE_AS_NUMERIC = "Enter Your choice as numeric either 1 or 2"
INVALID_OTP = "Invalid OTP."
INVALID_CONFIRMATION = "Invalid choice enter Either yes or no"
INVALID_PAYMENT_MODE = "Invalid Choice enter Either Upi or Cash"
#success messages
NAME_UPDATED = "Name updated Successfully"
EMAIL_UPDATED = "Email updated Successfully"
MOBILE_NUMBER_UPDATED = "Mobile Number  updated Successfully"
LOCATION_UPDATED = "Location updated Successfully"
LICENSE_NUMBER_UPDATED = "License number updated Successfully"
PASSWORD_UPDATED = "password updated Successfully"

# common keys
PASSWORD_KEY = "password"
MOBILE_NUMBER_KEY = "mobile_number"
LICENSE_NUMBER_KEY = "license_number"
AVAILABLE_ORDERS = "Available Orders: "
NO_AVAILABLE_ORDERS = "No available orders."
STATUS = "status"
STATUS_PENDING = "pending"
STATUS_PLACED = "Placed"
STATUS_IN_TRANSPORT = "In Transport"
STATUS_ASSIGNED = "Assigned"
ORDER_ID_KEY = "order_id"

# choices
ADD_CHOICE = "add"
REMOVE_CHOICE = "remove"
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
ELEVEN = 11
TWELVE = 12
ZERO = 0