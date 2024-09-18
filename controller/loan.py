from constant.constant import (USER_LOAN_SUCCESS, ERROR_LOAN_REQUEST, ERROR_REQUEST_LOAN, LOAN_REJECTED,
                               LOAN_APPROVED, ERROR_LOAN_APPROVAL, ERROR_LOAN_REJECT)

from service.loan import request_money, accept, reject


def request_amount(user_id, amount):
    """
    Controller of request loan:
    - Calls the function request loan from service
    - Checks fo the loan_id if available
    :param user_id: uuid generated
    :param amount: value of amount to be added
    :return: returns success message
    """
    try:
        loan_id = request_money(user_id, amount)
        if loan_id:
            return USER_LOAN_SUCCESS
        return ERROR_LOAN_REQUEST
    except ValueError:
        return ERROR_REQUEST_LOAN


def sanction(loan_id):
    """
    Approval loan:
    -Admin access only
    -Service request receives controller.
    -User can approve their pending loan request here
    :param loan_id: Loan id
    :return: returns success or error message
    """
    try:
        if accept(loan_id):
            return LOAN_APPROVED
        return ERROR_LOAN_APPROVAL
    except ValueError:
        return ERROR_LOAN_APPROVAL


def deny(loan_id):
    """
    Admin reject loan functionality
    - Loan_id is entered from service called here
    - If reject function is true, error message or success message is displayed
    :param loan_id: loan_id generated
    :return: returns success message
    """
    try:
        if reject(loan_id):
            return LOAN_REJECTED
        return ERROR_LOAN_REJECT
    except ValueError:
        return ERROR_LOAN_REJECT
