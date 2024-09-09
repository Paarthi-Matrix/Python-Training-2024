# 1. Main Menu
LOG_MAIN_MENU_ROLE_SELECTED = "Main menu role selected: {role}"
LOG_ERROR_ROLE_INTEGER = "Role choice should be an integer"
LOG_ERROR_CHOICE_RANGE_1_4 = "Choice should range between 1 to 4"
LOG_ERROR_CHOICE_RANGE_1_3 = "Choice should range between 1 to 3"
LOG_MAIN_MENU_EXIT = "Main menu option to exit selected"

# 2. Customer Menu
LOG_CUSTOMER_MENU_CHOICE_SELECTED = "Customer menu choice selected: {choice}"
LOG_ERROR_CHOICE_RANGE_1_5 = "Choice should range between 1 to 5"
LOG_CUSTOMER_MENU_EXIT = "Customer menu option to exit selected"
LOG_INVALID_CUSTOMER_MENU_CHOICE = "Invalid customer menu choice: {choice}"
LOG_VALUE_ERROR_IN_CUSTOMER_MENU = "ValueError in customer menu: {e}"

# 3. Admin Menu
LOG_ADMIN_MENU_CHOICE_SELECTED = "Admin menu choice selected: {choice}"
LOG_ERROR_CHOICE_RANGE_1_13 = "Choice should range between 1 to 13"
LOG_ERROR_CHOICE_RANGE_1_6 = "Choice should range between 1 to 6"
LOG_INVALID_ADMIN_MENU_CHOICE = "Invalid admin menu choice: {choice}"
LOG_VALUE_ERROR_IN_ADMIN_MENU = "Invalid input. Please enter an integer value."

# 4. Input Validation
LOG_VALID_INPUT_RECEIVED = "Valid input received: {value}"
LOG_INVALID_INPUT_RECEIVED = "Invalid input received: {value}"

# 5. Customer Registration and Updates
LOG_CUSTOMER_REGISTERED = "Customer registered with ID: {generated_id}"
LOG_CUSTOMER_FOUND_WITH_ID = "Customer found with ID: {customer_id}"
LOG_NO_CUSTOMER_FOUND_WITH_ID = "No customer found with ID: {customer_id}"
LOG_NO_CUSTOMER_FOUND_WITH_NAME = "No customer found with ID: {name}"
LOG_CUSTOMER_PRESENT_WITH_ID = "Customer present with ID: {customer_id}"
LOG_CUSTOMER_NAME_UPDATED = "Customer name updated for ID: {customer_id}"
LOG_CUSTOMER_EMAIL_UPDATED = "Customer email updated for ID: {customer_id}"
LOG_CUSTOMER_PASSWORD_UPDATED = "Customer password updated for ID: {customer_id}"
LOG_CUSTOMER_MOBILE_UPDATED = "Customer mobile updated for ID: {customer_id}"
LOG_CUSTOMER_UPDATED = "Updated customer successfully whose Id: {customer_id}"
LOG_CUSTOMER_REGISTERED_WITH_ID = "Registered customer with ID: {customer_id}"
LOG_BIN_CREATED_WITH_ID = "Bin created for the customer where bin id: {bin_id}"
LOG_BIN_ALREADY_CREATED = "Bin already created for the customer whose Id: {customer_id}"
LOG_DRIVER_NOT_AVAILABLE = "Driver not available for the given area: {area}"
LOG_INVALID_CUSTOMER_IDENTIFIER = "Invalid customer identifier: {customer_identifier}"
LOG_COMPLAINT_REGISTERED = "Complaint registered successfully where Bin Id: {bin_id}"

# 6. Profile Updates
LOG_UPDATE_PROFILE_EXIT = "Update profile option to exit selected"
LOG_INVALID_UPDATE_PROFILE_CHOICE = "Invalid update profile choice: {choice}"
LOG_VALUE_ERROR_IN_UPDATE_PROFILE = "ValueError in update profile: {e}"

# 7. Admin Actions
LOG_ADMIN_CREATED_WITH_ID = "Admin created with ID: {register_status}"
LOG_UNAUTHORIZED_ADMIN_CREATION_ATTEMPT = "Unauthorized admin creation attempt"
LOG_DRIVER_REGISTERED = "Driver successfully registered with Id: {driver_id}"
LOG_ADMIN_AUTHORIZATION = "You are Unauthorized"
LOG_NO_DRIVER_FOUND = "NO driver added yet"
LOG_RECYCLER_REGISTERED = "Recycler registered successfully where Id: {recycler_id}"
LOG_RECYCLER_UNAUTHORIZED = "Unauthorized Entry"
LOG_RECYCLER_ALREADY_REGISTERED = "Recycler already registered"
LOG_WASTAGE_WEIGHT_CALCULATED = "Total waste: {} kg, Bio-degradable waste: {} kg, Non-bio-degradable waste: {} kg"
LOG_CALCULATED_PROFIT = "Profit has been calculated and credited to the respective bin owners"
LOG_RATE_CALCULATED = "Rate Calculated according the respective wastage kilograms"
# 8. Customer Search and Deletion
LOG_END_SEARCH = "Search has been ended"
LOG_INVALID_SEARCH_CUSTOMER_CHOICE = "Invalid search customer choice: {search_choice}"
LOG_CUSTOMER_DELETED_WITH_ID = "Customer deleted with ID: {customer_id}"
LOG_NO_DRIVER = "No driver found for this area: {area}"
LOG_DOOR_NO = "Door number already exists for this area: {area}"
LOG_ERROR_DELETING_CUSTOMER = "Error deleting customer with ID: {customer_id}"

# 9. Miscellaneous
LOG_NO_CUSTOMER_SIGNED_UP = "No customers signed up"
LOG_REDIRECTING_HOME = "Redirecting you to home"
LOG_APPLICATION_END = "Application Stop..Thank You"

# 10. Error
# Constants for Error Messages
LOG_ERROR_INVALID_NAME = "Name should only contain lowercase, uppercase letters, and spaces."
LOG_ERROR_INVALID_AREA = "Enter valid area: "
LOG_ERROR_INVALID_DOOR_NO = "Enter valid door no: "
LOG_ERROR_INVALID_LOCALITY = "Enter valid locality: "
LOG_ERROR_INVALID_LANDMARK = "Enter the valid landmark"
LOG_ERROR_INVALID_CITY = "Enter the valid city (Chennai)"
LOG_ERROR_COMPLAINT_INVALID = "Enter the Valid complaint"
LOG_ERROR_INVALID_LOAD = "Load should be Low, High"
LOG_ERROR_INVALID_WASTAGE = "Invalid wastage type."
LOG_ERROR_INVALID_STATUS = "Status should be either COMPLETED, INCOMPLETE, or IN PROGRESS."
LOG_ERROR_INVALID_CYCLE_PERIOD = "Cycle period should be daily"
LOG_ERROR_INVALID_WASTAGE_TYPE = "It should be Bio-Degradable, Non Bio-degradable, Both"
LOG_ERROR_INVALID_EMAIL = "Email should contain lowercase letters, numbers, and end with the suffix (@gmail.com)."
LOG_ERROR_INVALID_PASSWORD = (
    "Password must be at least 8 characters long, contain one uppercase letter, one lowercase "
    "letter, one number, and no spaces.")
LOG_ERROR_INVALID_MOBILE = "Mobile number should have 10 digits, and start with 6, 7, 8, or 9."
LOG_USER_ALREADY_REGISTERED_EMAIL = "User already registered by email: {email}"
LOG_USER_ALREADY_REGISTERED_PASSWORD = "User already registered by password: {password}"
LOG_USER_ALREADY_REGISTERED_AREA = "User already registered for area: {area}"

#10. Driver
LOG_BIN_UPDATED = "Work report added successfully where Bin Id: {bin_id}"
LOG_WORK_REPORT = "No work reports added yet"
LOG_BIN_STATUS_COMPLETED = "Bin status already completed for bin  Id: {bin_id}"
LOG_INVALID_WEIGHT = "Invalid weight. The weight must be between 1 and 100 kg."
LOG_WORK_REPORT_INCOMPLETE = "Work report already Incomplete for Id: {bin_id}"
