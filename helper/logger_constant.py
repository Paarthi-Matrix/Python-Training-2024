# 1. Main Menu
LOG_MAIN_MENU_ROLE_SELECTED = "Main menu role selected: {role}"
LOG_ERROR_ROLE_INTEGER = "Role choice should be an integer"
LOG_ERROR_CHOICE_RANGE_1_4 = "Choice should range between 1 to 4"
LOG_MAIN_MENU_EXIT = "Main menu option to exit selected"

# 2. Customer Menu
LOG_CUSTOMER_MENU_CHOICE_SELECTED = "Customer menu choice selected: {choice}"
LOG_ERROR_CHOICE_RANGE_1_5 = "Choice should range between 1 to 5"
LOG_CUSTOMER_MENU_EXIT = "Customer menu option to exit selected"
LOG_INVALID_CUSTOMER_MENU_CHOICE = "Invalid customer menu choice: {choice}"
LOG_VALUE_ERROR_IN_CUSTOMER_MENU = "ValueError in customer menu: {e}"

# 3. Admin Menu
LOG_ADMIN_MENU_CHOICE_SELECTED = "Admin menu choice selected: {choice}"
LOG_ERROR_CHOICE_RANGE_1_6 = "Choice should range between 1 to 6"
LOG_INVALID_ADMIN_MENU_CHOICE = "Invalid admin menu choice: {choice}"
LOG_VALUE_ERROR_IN_ADMIN_MENU = "ValueError in admin menu: {e}"

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
LOG_CUSTOMER_UPDATED = "Updated customer {customer_id}: set {field} to {value}"
LOG_CUSTOMER_REGISTERED_WITH_ID = "Registered customer with ID: {customer_id}"
LOG_INVALID_CUSTOMER_IDENTIFIER = "Invalid customer identifier: {customer_identifier}"

# 6. Profile Updates
LOG_UPDATE_PROFILE_EXIT = "Update profile option to exit selected"
LOG_INVALID_UPDATE_PROFILE_CHOICE = "Invalid update profile choice: {choice}"
LOG_VALUE_ERROR_IN_UPDATE_PROFILE = "ValueError in update profile: {e}"

# 7. Admin Actions
LOG_ADMIN_CREATED_WITH_ID = "Admin created with ID: {admin_id}"
LOG_UNAUTHORIZED_ADMIN_CREATION_ATTEMPT = "Unauthorized admin creation attempt"

# 8. Customer Search and Deletion
LOG_END_SEARCH = "Search has been ended"
LOG_INVALID_SEARCH_CUSTOMER_CHOICE = "Invalid search customer choice: {search_choice}"
LOG_CUSTOMER_DELETED_WITH_ID = "Customer deleted with ID: {customer_id}"
LOG_ERROR_DELETING_CUSTOMER = "Error deleting customer with ID: {customer_id}"

# 9. Miscellaneous
LOG_NO_CUSTOMER_SIGNED_UP = "No customers signed up"
LOG_REDIRECTING_HOME = "Redirecting you to home"
LOG_APPLICATION_END = "Application Stop..Thank You"

# 10. Error
# Constants for Error Messages
LOG_ERROR_INVALID_NAME = "Name should only contain lowercase, uppercase letters, and spaces."
LOG_ERROR_INVALID_EMAIL = "Email should contain lowercase letters, numbers, and end with the suffix (@gmail.com)."
LOG_ERROR_INVALID_PASSWORD = (
    "Password must be at least 8 characters long, contain one uppercase letter, one lowercase "
    "letter, one number, and no spaces.")
LOG_ERROR_INVALID_MOBILE = "Mobile number should have 10 digits, and start with 6, 7, 8, or 9."
