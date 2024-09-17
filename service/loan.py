import uuid


from constant.constant import (LOAN_PENDING, LOAN_APPROVED, LOAN_REJECTED, POOL_NOT_FOUND, ERROR_REQUEST,
                               MSG_LOAN_APPROVAL, USER_PENDING_LOAN, ERROR_LOAN_APPROVAL, MSG_LOAN_REJECTED,
                               USER_LOAN_SUCCESS)
from resource.log_configuration import setup_logger

logger = setup_logger()

loans = {}


def request_loan(user_id, amount, pools):
    """
    User Can request loan:
    - User enters the user login, selects request loan choice in console
    - Function checks if the entered amount is greater than the amount in pool
    - If amount requested is less than pool balance, loan request gets approved
    - Else loan creation does not occur
    :param user_id: Entered as string, generated uuid
    :param amount: Float value entered
    :return: Returns the loan_id
    """
    try:
        if any(loan['user_id'] == user_id for loan in loans.values()):
            logger.warning(USER_PENDING_LOAN.format(user_id))
            return USER_PENDING_LOAN.format(user_id)
        if pools.get('current_pool') and pools['current_pool'].get("total_funds", 0) > amount:
            loan_id = f"loan_{str(uuid.uuid4())}"
            loans[loan_id] = {
                "user_id": user_id,
                "amount": amount,
                "status": LOAN_PENDING
            }
            logger.info(USER_LOAN_SUCCESS.format(loan_id))
            return loan_id
        else:
            logger.info(POOL_NOT_FOUND)
            return POOL_NOT_FOUND
    except ValueError:
        logger.error(ERROR_REQUEST)
        return None


def accept_loan(loan_id):
    """
    Admin Controller:
    - Admin enters and accepts the loan by entering loan id
    - Checks if the loan id is available in the loan dict
    - If loan id doesnt exists value error is handled
    :param loan_id: Generated UUID
    :return: Returns Loan_id
    """
    try:
        if loan_id in loans:
            loans[loan_id]['status'] = LOAN_APPROVED
            logger.info(MSG_LOAN_APPROVAL.format(loan_id, loans[loan_id]['user_id']))
            return True
        return False
    except ValueError:
        logger.error(ERROR_LOAN_APPROVAL)
        return False


def reject_loan(loan_id):
    """
    Reject Loan requested by user
    - Admin rejects the users loan request by entering the loan_id
    - if entered loan_id is not available in loan dict, value error is handled
    :param loan_id: loan_id generated UUID
    :return: Returns True or False
    """
    try:
        if loan_id in loans:
            loans[loan_id]['status'] = LOAN_REJECTED
            logger.info(MSG_LOAN_REJECTED.format(loan_id, loans[loan_id]['user_id']))
            return True
        return False
    except ValueError:
        logger.error(ERROR_LOAN_APPROVAL)
        return False
