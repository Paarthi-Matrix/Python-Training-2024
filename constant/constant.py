#regex
USERNAME_REGEX = r'^[a-zA-Z0-9_]{3,30}$'
PASSWORD_REGEX = r'^[a-zA-Z0-9@#$%^&+=]{6,30}$'
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

#Logger constants
LOG_FILE = "lending_system.log"
LOG_FORMATTER = "%(asctime)s - %(levelname)s - %(message)s"

#User Related Messages
INITIAL_BALANCE = 0
USER_MONEY_ADDED = "{} added to the user_id : {}"
USER_CONTRIBUTION = "The user {} has successfully contributed {} to the pool"
INSUFFICIENT_FUND = "The user {} has insufficient funds to contribute to the pool"
USER_BALANCE = "Your balance is currently {}"
ERROR_BALANCE_CHECK = "Error checking the balance for the user"
ERROR_LOAN_REQUEST = "Loan request unsuccessful"


#User Related ERRORS
ERROR_USER_EXISTS = "The user {} already exists"
ERROR_USER_CREATION = "Error creating user {}"
ERROR_USER_LOGIN = "Please enter the correct username or password."
ERROR_USER_NOT_FOUND = "User not found!"
INVALID_CREDENTIALS = "Username and password doesn't match. Please try again!"
ERROR_ADD_MONEY = "Error adding money."

#Loan Related Details
LOAN_PENDING = "Loan Pending"
LOAN_APPROVED = "Loan Approved"
LOAN_REJECTED = "Loan Rejected"
POOL_NOT_FOUND = "No active pool found"
ERROR_REQUEST_LOAN = "We have encountered an error while requesting your loan"
MSG_LOAN_APPROVAL = "The loan {} requested by {} has been successfully approved"
ERROR_LOAN_APPROVAL = "Error accepting the loan"
MSG_LOAN_REJECTED = "The loan {} requested by {} has been successfully rejected"
ERROR_LOAN_REJECT = "Error rejecting the loan"

#Pool related details
POOL_THRESHOLD = 10000
MSG_POOL_CREATION = "New pool has been created with the id {}"
ERROR_POOL_BALANCE = "Error displaying the pool balance"
ERROR_POOL_CONTRIBUTION = "Error contributing to the pool"

#User related messages
USER_PENDING_LOAN = "User {} already has a pending loan."
USER_LOAN_SUCCESS = "Your loan request has been successfully initiated and the loan id is {}"
USER_CONTRIBUTION_SUCCESS = "The user {} has successfully contributed {} to the pool"
USER_CONTRIBUTION_FAILURE = "The user {} has insufficient funds to contribute to the pool"
USER_NOT_FOUND = "User not found!"
USER_CREATION_SUCCESS = "User {} has been created with ID {} successfully"
USER_LOGIN_SUCCESS = "User {} has been successfully logged in"
ERROR_USER_PASS = "Invalid username or password"
USER_CREATED = "User created with ID: {}"
POOL_INSUFFICIENT_FUND = "Pool has insufficient fund"


#main function constants
MAIN_CHOICE = "Enter choice: (1,3) "
USER_CHOICE = "Enter choice (1-5): "
EXIT = "Exiting the application."
INVALID_CHOICE = "Invalid choice!"
INPUT_USERNAME = "Enter username: "
INPUT_PASS = "Enter password: "
INPUT_EMAIL = "Enter email: "
INPUT_AMT = "Enter amount to add: "
INPUT_LOAN_APPROVE = "Enter loan ID to approve: "
INPUT_LOAN_REJECT = "Enter loan ID to reject: "
ADD_AMT_SUCCESS = "Money added successfully."
ADD_AMT_FAILURE = "Failed to add money."
ADD_AMT_CONTRIBUTE = "Enter amount to contribute: "
CONTRIBUTION_SUCCESS = "Contribution successful."
CONTRIBUTION_FAILURE = "Failed to contribute."
INPUT_LOAN_AMT = "Enter loan amount: "
LOAN_REQUEST = "Loan requested with ID: {}"
LOAN_REQUEST_FAIL = "Loan request failed."
EXIT_MAIN = "Exiting to main menu."
DISPLAY_BALANCE = "Your Balance: {}"
ERROR_BALANCE = "Failed to fetch balance."
LOGIN_FAIL = "Login failed."
USER_CREATION_FAIL = "User creation failed."
POOL_CREATION_SUCCESS = "New pool created successfully."
POOL_BALANCE = "The total funds available in the pool is {}"
POOL_BALANCE_FAIL = "Failed to fetch pool balance."
LOAN_APPROVE_SUCCESS = "Loan approved successfully."
LOAN_APPROVE_FAILURE = "Failed to approve loan."
LOAN_REJECT_SUCCESS = "Loan rejected successfully."
LOAN_REJECT_FAILURE = "Failed to reject loan."

ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'

MAIN_MENU = '''   -----------------------------------
    WELCOME TO IDEAS2IT LENDING SYSTEM
   -----------------------------------
    1. User
    2. Admin
    3. Exit
    ----------------------------------'''

USER_MENU = '''   --------------------------------
             USER MENU
   --------------------------------
    1. Add Money
    2. Contribute to Pool
    3. Request Loan
    4. Check Balance
    5. Exit
   --------------------------------'''

ADMIN_MENU = '''   --------------------------------
             ADMIN MENU
    --------------------------------
    1. Create New Pool
    2. Get Pool Balance
    3. Approve Loan
    4. Reject Loan
    5. Exit
    --------------------------------'''
