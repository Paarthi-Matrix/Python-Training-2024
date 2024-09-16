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

#User Related ERRORS
ERROR_USER_EXISTS = "The user {} already exists"
ERROR_USER_CREATION = "Error Creating User: {} with error: {}"
ERROR_USER_LOGIN = "Please enter the correct username or password."
ERROR_USER_NOT_FOUND = "User not found!"
INVALID_CREDENTIALS = "Username and password doesn't match. Please try again!"
ERROR_ADD_MONEY = "Error adding money."

#Loan Related Details
LOAN_PENDING = "Pending"
LOAN_APPROVED = "Approved"
LOAN_REJECTED = "Rejected"
POOL_NOT_FOUND = "No active pool found"
ERROR_REQUEST = "We have encountered an error while requesting your loan"
MSG_LOAN_APPROVAL = "The loan {} requested by {} has been successfully approved"
ERROR_LOAN_APPROVAL = "Error accepting the loan"
MSG_LOAN_REJECTED = "The loan {} requested by {} has been successfully rejected"

"""Pool related details"""
POOL_THRESHOLD = 10000
MSG_POOL_CREATION = "New pool has been created with the id {}"
POOL_BALANCE = "The total funds available in the pool is {}"
ERROR_POOL_BALANCE = "Error displaying the pool balance"
ERROR_POOL_CONTRIBUTION = "Error contributing to the pool"