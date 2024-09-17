from constant.constant import (USER_LOAN_SUCCESS, ERROR_LOAN_REQUEST, ERROR_REQUEST_LOAN, LOAN_REJECTED,
                               MSG_LOAN_APPROVAL, LOAN_APPROVED,ERROR_LOAN_APPROVAL, MSG_LOAN_REJECTED,
                               ERROR_LOAN_REJECT)
from service.loan import request_loan, accept_loan, reject_loan
from resources.log_configuration import setup_logger


logger = setup_logger()


def request_loan_controller(user_id, amount, pools):
    """
    Controller of request loan:
    - Calls the function request loan from service
    - Checks fo the loan_id if available
    :param user_id: uuid generated
    :param amount: value of amount to be added
    :param pools: pools to be added into
    :return: returns success message
    """
    try:
        loan_id = request_loan(user_id, amount, pools)
        if loan_id:
            logger.info(USER_LOAN_SUCCESS.format(loan_id))
            return USER_LOAN_SUCCESS
        return ERROR_LOAN_REQUEST
    except ValueError:
        logger.error(ERROR_REQUEST_LOAN)
        return ERROR_REQUEST_LOAN


def approve_loan_controller(loan_id):
    """
    Approval loan:
    -Admin access only
    -Service request recevies controller.
    -User can approve their pending loan request here
    :param loan_id: Loan id
    :return: returns success or error message
    """
    try:
        if accept_loan(loan_id):
            logger.info(MSG_LOAN_APPROVAL.format(loan_id, "user"))
            return LOAN_APPROVED
        return ERROR_LOAN_APPROVAL
    except ValueError:
        logger.error(ERROR_LOAN_APPROVAL)
        return ERROR_LOAN_APPROVAL


def reject_loan_controller(loan_id):
    """
    Admin reject loan functionality
    - Loan_id is entered from service called here
    - If reject function is true, error message or success message is displayed
    :param loan_id: loan_id generated
    :return: returns success message
    """
    try:
        if reject_loan(loan_id):
            logger.info(MSG_LOAN_REJECTED.format(loan_id, "user"))
            return LOAN_REJECTED
        return ERROR_LOAN_REJECT
    except ValueError:
        logger.error(ERROR_LOAN_REJECT)
        return ERROR_LOAN_REJECT
