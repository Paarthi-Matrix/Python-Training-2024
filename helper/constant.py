# 1. Main Menu
LOG_MAIN_MENU_ROLE_SELECTED = "Main menu role selected: {role}"
LOG_ERROR_ROLE_INTEGER = "Role choice should be an integer"
LOG_MAIN_MENU_EXIT = "Main menu option to exit selected"

# 2. Customer Menu
LOG_CUSTOMER_MENU_CHOICE_SELECTED = "Customer menu choice selected: {choice}"
LOG_CUSTOMER_MENU_EXIT = "Customer menu option to exit selected"
LOG_INVALID_CUSTOMER_MENU_CHOICE = "Invalid customer menu choice: {choice}"
VALUE_ERROR_IN_CUSTOMER_MENU = "ValueError in customer menu: {e}"
LOG_EXCEED_LIMIT = "Exceeding limit, Unable to continue process"

# 3. Admin Menu
LOG_ADMIN_MENU_CHOICE_SELECTED = "Admin menu choice selected: {choice}"
LOG_INVALID_ADMIN_MENU_CHOICE = "Invalid admin menu choice: {choice}"
LOG_VALUE_ERROR_IN_ADMIN_MENU = "Invalid input. Please enter an integer value."

# 4. Input Validation
LOG_VALID_INPUT_RECEIVED = "Valid input received: {value}"
LOG_INVALID_INPUT_RECEIVED = "Invalid input received: {value}"

# 5. Customer Registration and Updates
CUSTOMER_REGISTERED = "Customer registered with ID: {customer_detail}"
LOG_CUSTOMER_FOUND_WITH_ID = "Customer found with ID: {customer_id}"
LOG_NO_CUSTOMER_FOUND_WITH_ID = "No customer found with ID: {customer_id}"
LOG_NO_CUSTOMER_FOUND_WITH_NAME = "No customer found with ID: {name}"
LOG_CUSTOMER_PRESENT_WITH_ID = "Customer present with ID: {customer_id}"
LOG_CUSTOMER_NAME_UPDATED = "Customer name updated for ID: {customer_id}"
LOG_CUSTOMER_EMAIL_UPDATED = "Customer email updated for ID: {customer_id}"
LOG_CUSTOMER_PASSWORD_UPDATED = "Customer password updated for ID: {customer_id}"
LOG_CUSTOMER_MOBILE_UPDATED = "Customer mobile updated for ID: {customer_id}"
LOG_CUSTOMER_UPDATED = "Updated customer successfully whose Id: {customer_id}"
LOG_CUSTOMER_REGISTERED_WITH_ID = "Registered customer with ID: {customer_detail}"
BIN_CREATED_WITH_ID = "Bin created for the customer where bin id: {bin_detail}"
LOG_BIN_ALREADY_CREATED = "Bin already created for the customer whose Id: {customer_id}"
LOG_DRIVER_NOT_AVAILABLE = "Driver not available for the given area: {area}"
LOG_INVALID_CUSTOMER_IDENTIFIER = "Invalid customer identifier: {customer_identifier}"
COMPLAINT_REGISTERED = "Complaint registered successfully where Bin Id: {bin_id}"
BIN_REGISTERED = 'Bin Registered Successfully'
CUSTOMER_UPDATED = "customer updated successfully where customer Id: {}"

# 6. Profile Updates
LOG_UPDATE_PROFILE_EXIT = "Update profile option to exit selected"
LOG_INVALID_UPDATE_PROFILE_CHOICE = "Invalid update profile choice: {choice}"
LOG_VALUE_ERROR_IN_UPDATE_PROFILE = "ValueError in update profile: {e}"

# 7. Admin Actions
LOG_ADMIN_CREATED = "Admin created successfully"
LOG_UNAUTHORIZED_ADMIN_CREATION_ATTEMPT = "Unauthorized admin creation attempt"
DRIVER_REGISTERED = "Driver successfully registered with Id: {driver_detail}"
LOG_ADMIN_AUTHORIZATION = "You are Unauthorized"
LOG_NO_DRIVER_FOUND = "NO driver added yet"
LOG_RECYCLER_REGISTERED = "Recycler registered successfully where Id: {recycler_id}"
LOG_RECYCLER_UNAUTHORIZED = "Unauthorized Entry"
LOG_RECYCLER_ALREADY_REGISTERED = "Recycler already registered"
WASTAGE_WEIGHT_CALCULATED = "Total waste: {} kg, Bio-degradable waste: {} kg, Non-bio-degradable waste: {} kg"
LOG_CALCULATED_PROFIT = "Profit has been calculated and credited to the respective bin owners"
LOG_RATE_CALCULATED = "Rate Calculated according the respective wastage kilograms"
DICT_ADMIN_ID = "admin_id"
DATA_FILE = r"C:\Users\ranjithkumar.radhakr\PycharmProjects\user_detail\user_detail"
WASTAGE_REPORT = "wastage_report"
LOG_COST_OF_WASTAGE = "Cost of wastage retrieved successfully where Id: {wastage_id}"
TOTAL_PROFIT_CALCULATED = "Total profit calculated as {total_profit} after credited the customer profits"

# 8. Customer Search and Deletion
LOG_END_SEARCH = "Search has been ended"
LOG_INVALID_SEARCH_CUSTOMER_CHOICE = "Invalid search customer choice: {search_choice}"
CUSTOMER_DELETED_WITH_ID = "Customer deleted with ID: {customer_id}"
NO_DRIVER = "No driver found for this area: {area}"
LOG_DOOR_NO = "Door number already exists for this area: {area}"
LOG_ERROR_DELETING_CUSTOMER = "Error deleting customer with ID: {customer_id}"

# 9. Miscellaneous
LOG_NO_CUSTOMER_SIGNED_UP = "No customers signed up"
LOG_REDIRECTING_HOME = "Redirecting you to home"
LOG_APPLICATION_END = "Application Stop..Thank You"
LOG_FILE_LOCATION = r"C:\Users\ranjithkumar.radhakr\PycharmProjects\Garbage_Collector_logs"
LOG_EXCEPTION = "Unknown Exception arise: {e} "

# 10. Error
# Constants for Error Messages
ERROR_INVALID_NAME = "Name should only contain lowercase, uppercase letters, and spaces."
ERROR_INVALID_AREA = "Area Invalid: "
ERROR_INVALID_DOOR_NO = "Enter valid door no: "
LOG_ERROR_INVALID_LOCALITY = "Enter valid locality: "
ERROR_INVALID_LANDMARK = "Enter the valid landmark"
ERROR_INVALID_CITY = "Enter the valid city (Chennai)"
ERROR_COMPLAINT_INVALID = "Invalid complaint"
ERROR_INVALID_LOAD = "Load should be Low, High"
ERROR_INVALID_WASTAGE = "Invalid wastage type."
ERROR_INVALID_STATUS = "Status should be either COMPLETED, INCOMPLETE."
ERROR_INVALID_CYCLE_PERIOD = "Cycle period should be daily"
LOG_ERROR_INVALID_WASTAGE_TYPE = "It should be Bio-Degradable, Non Bio-degradable, Both"
ERROR_INVALID_EMAIL = "Email should contain lowercase letters, numbers, and end with the suffix (@gmail.com)."
ERROR_INVALID_PASSWORD = (
    "Password must be at least 8 characters long, contain one uppercase letter, one lowercase "
    "letter, one number, and no spaces.")
ERROR_INVALID_MOBILE = "Mobile number should have 10 digits, and start with 6, 7, 8, or 9."
LOG_USER_ALREADY_REGISTERED_EMAIL = "User already registered by email: {email}"
LOG_USER_ALREADY_REGISTERED_PASSWORD = "User already registered by password: {password}"
LOG_USER_ALREADY_REGISTERED_AREA = "User already registered for area: {area}"

#10. Driver
LOG_BIN_UPDATED = "Work report added successfully for bin"
NO_WORK_REPORT = "No work reports added yet"
LOG_BIN_STATUS_COMPLETED = "Bin status already completed for bin  Id: {bin_id}"
LOG_INVALID_WEIGHT = "Invalid weight. The weight must be between 1 and 100 kg."
LOG_WORK_REPORT_INCOMPLETE = "Work report already Incomplete for Id: {bin_id}"
DRIVER = 'driver_detail'
WORK_REPORT = 'work_report'
COMPLAINTS = "complaints"
REGISTER_STATUS = "status"
REGISTERED = "Registered"
TOTAL_WEIGHTAGE = "Total_weightage"

# Menu helper
MAIN_MENU = """
==================================
        WELCOME TO THE SYSTEM      
==================================
Please select your role:
----------------------------------
1. Customer
2. Admin
3. Driver
4. Recycler
5. Exit
----------------------------------
Enter your choice (1-5): 
"""

CUSTOMER_MENU = """
==================================
          CUSTOMER MENU           
==================================
Please select an option:
----------------------------------
1. Sign Up Customer
2. Register Bin
3. Raise Complaint
4. View Profits
5. My Profile
6. Bin Details
7. Exit
----------------------------------
Enter your choice (1-7): 
"""

ADMIN_MENU = """
==================================
            ADMIN MENU            
==================================
Please select an option:
----------------------------------
1. Sign Up Admin
2. Sign Up Driver
3. Search Customer
4. Delete Customer
5. Update Customer
6. Search Driver
7. View Work reports
8. View Complaints
9. Register Recycler
10. Report to Recycler
11. View Cost of Garbage
12. Calculate Profit
13. Exit
----------------------------------
Enter your choice (1-13): 
"""

DRIVER_MENU = """
==================================
          DRIVER MENU           
==================================
Please select an option:
----------------------------------
1. My Profile
2. My Bins
3. Add Work Report
4. Work Reports
5. Complaints
6. Exit
----------------------------------
Enter your choice (1-6): 
"""

UPDATE_CUSTOMER_MENU = """
==================================
         UPDATE PROFILE          
==================================
Please select a detail to update:
----------------------------------
1. Update name
2. Update email
3. Update password
4. Update mobile
5. Exit
----------------------------------
Enter your choice (1-5): 
"""

SEARCH_CUSTOMER_MENU = """
==================================
          SEARCH CUSTOMER         
==================================
Search by:
----------------------------------
1. Search by First Name or Last Name
2. Search by Id
3. Find All
4. Exit
----------------------------------
Enter your choice (1-4): 
"""

RECYCLER_MENU = """
==================================
          RECYCLER MENU           
==================================
Please select an option:
----------------------------------
1. Check Wastage
2. Calculate Rate
----------------------------------
Enter your choice (1-4): 
"""

# prompt helper
PROMPT_CUSTOMER_NAME = "Enter the customer name: "
PROMPT_CUSTOMER_AREA = "Enter the area: "
PROMPT_CUSTOMER_DOOR_NO = "Enter the door no: "
PROMPT_ADMIN_NAME = "Enter the admin name: "
PROMPT_DRIVER_NAME = "Enter the driver name: "
PROMPT_RECYCLER_NAME = "Enter the recycler name: "
PROMPT_BIN_STATUS = "Enter the Bin Status(COMPLETED or INCOMPLETE): "
PROMPT_BIN_COMPLETED = "COMPLETED"
PROMPT_BIN_INCOMPLETE = "INCOMPLETE"
PROMPT_DRIVER_AREA = "Enter the area where driver to be enrolled: "
PROMPT_EMAIL = "Enter the email: "
PROMPT_BIN_ID = "Enter the Bin Id: "
PROMPT_RAISE_COMPLAINT = "Enter your complaint:"
PROMPT_WASTAGE_TYPE = "BOTH"
PROMPT_BIO_DEGRADABLE = "BIO-DEGRADABLE"
PROMPT_BIO_DEGRADABLE_WASTE = "Enter the weight for Bio-degradable waste (kg): "
PROMPT_NON_BIO_DEGRADABLE = "NON BIO-DEGRADABLE"
PROMPT_NON_BIO_DEGRADABLE_WASTE = "Enter the weight for Non Bio-degradable waste (kg): "
PROMPT_CUSTOMER_LOCALITY = "Enter the locality: "
PROMPT_CUSTOMER_LANDMARK = "Enter the landmark: "
PROMPT_CUSTOMER_CITY = "Enter the City: "
PROMPT_CUSTOMER_CYCLE_PERIOD = "Enter the cycle period(Daily): "
PROMPT_CUSTOMER_LOAD = "Enter the Load Type(Low or High): "
PROMPT_CUSTOMER_WASTAGE_TYPE = "Enter the wastage type(Bio-degradable or Non Nio-degradable or Both): "
PROMPT_PASSWORD = "Enter the password: "
PROMPT_MOBILE = "Enter the mobile number: "
PROMPT_ACCOUNT_NO = "Enter the account number: "
PROMPT_CUSTOMER_ID = "Enter the Customer Id: "
PROMPT_NAME_TO_UPDATE = "Enter the name to update: "
PROMPT_EMAIL_TO_UPDATE = "Enter the email to update: "
PROMPT_PASSWORD_TO_UPDATE = "Enter the password to update: "
PROMPT_MOBILE_TO_UPDATE = "Enter the mobile number to update: "
PROMPT_CHOICE = "Enter your choice:"
PROMPT_ROLE = "Choose the Role:"
PROMPT_SEARCH_NAME = "Enter the name to search:"
PROMPT_SEARCH_CUSTOMER_ID = "Enter the customer Id:"
PROMPT_CONTINUE_PROCESS = "Do you want to continue? (YES or NO)"
PROMPT_YES = "YES"
PROMPT_NO = "NO"

# regex helper
REGEX_VALIDATE_STATUS = r'^(COMPLETED|INCOMPLETE)$'
REGEX_VALIDATE_WASTAGE_TYPE = r'^(Bio-degradable|Non Bio-degradable|Both)$'
REGEX_VALIDATE_DOOR_N0 = r'^([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-2][0-9]{3}|3000)$'
REGEX_VALID_COMPLAINT = r'^([a-zA-Z\s]+)'

# Number Constant
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
THIRTEEN = 13
HUNDRED = 100
TWENTY = 20
FIFTY = 50

# User constants
ADMIN_REGISTERED = "Admin successfully registered"
NO_CUSTOMER_SIGNED_UP = "No customers signed up"
CUSTOMER_REMOVED = "Deleted customer successfully"
UPDATED_CUSTOMER = "Customer updated successfully"
RECYCLER_REGISTERED = "Recycler registered successfully"
PROMPT_BIO_WASTE_WEIGHT = "Bio waste weightage(KG): "
PROMPT_NON_BIO_WASTE_WEIGHT = "Non Bio waste weightage(KG): "
PROMPT_TOTAL_WASTE = "Total waste:"
WORK_REPORT_ADDED = "Work report added successfully"
ADMIN_UNAUTHORIZED = "Unauthorized..Invalid Credentials"
ADMIN_ALREADY_REGISTERED = "Admin already registered"

# Choice Ranges
CHOICE_RANGE_1_13 = "Choice should range between 1 to 13"
CHOICE_RANGE_1_6 = "Choice should range between 1 to 6"
CHOICE_RANGE_1_4 = "Choice should range between 1 to 4"
CHOICE_RANGE_1_3 = "Choice should range between 1 to 3"
CHOICE_RANGE_1_7 = "Choice should range between 1 to 7"
CHOICE_RANGE_1_5 = "Choice should range between 1 to 5"

# Dict constants
IS_DELETED = 'is_deleted'
DICT_NAME = "name"
DICT_EMAIL = "email"
DICT_PASSWORD = "password"
DICT_MOBILE = "mobile_no"
CUSTOMER_ID = 'customer_id'
DRIVER_EMAIL = 'driver_email'
AREA = "area"
DOOR_NO = "door_no"
BIO_WASTE = "bio-weight"
BIO_WASTE_WEIGHT = "bio_waste_weight"
NON_BIO_WASTE_WEIGHT = "non_bio_waste_weight"
PROFIT_BIO_WASTE = "profit_bio-weight"
PROFIT_NON_BIO_WASTE = "profit_non_bio-weight"
NON_BIO_WASTE = "non_bio-weight"
DATE_TIME = "date_time"
CUSTOMER_WORK_REPORT = 'work_reports'
CUSTOMER_DETAILS = 'customer_details'
STATUS = "status"
COMPLAINT_STATUS = "pending"
BIN_ID = 'bin_id'
BIN_DETAILS = 'bin_details'
PASSWORD = "password"
CUSTOMER_UPDATE = "customer_update"
RECYCLED = "Recycled"
YES = "Yes"
NO = "No"
TOTAL_WASTE = "total_waste"
TOTAL_PROFIT = "total_profit"
COST_OF_BIO_WASTE = "cost_of_bio_degradable"
COST_OF_NON_BIO_WASTE = "cost_of_non_bio_degradable"
