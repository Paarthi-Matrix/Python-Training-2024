import uuid
from Utils.constants import LOAN_PENDING, LOAN_APPROVED, LOAN_REJECTED
from Utils.constants import POOL_NOT_FOUND, ERROR_REQUEST, MSG_LOAN_APPROVAL
from Utils.constants import ERROR_LOAN_APPROVAL, MSG_LOAN_REJECTED
from Utils.log_configuration import setup_logger

logger = setup_logger()

loans = {}


def request_loan(user_id, amount, pools):
    try:
        if any(loan['user_id'] == user_id for loan in loans.values()):
            logger.warning("User {} already has a pending loan.".format(user_id))
            return "User already has a pending loan."
        if pools.get('current_pool') and pools['current_pool'].get("total_funds", 0) > amount:
            loan_id = f"loan_{str(uuid.uuid4())}"
            loans[loan_id] = {
                "user_id": user_id,
                "amount": amount,
                "status": LOAN_PENDING
            }
            logger.info("Your loan request has been successfully initiated and the loan id is {}".format(loan_id))
            return loan_id
        else:
            logger.info(POOL_NOT_FOUND)
            return POOL_NOT_FOUND
    except ValueError:
        logger.error(ERROR_REQUEST)
        return None


def accept_loan(loan_id):
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
    try:
        if loan_id in loans:
            loans[loan_id]['status'] = LOAN_REJECTED
            logger.info(MSG_LOAN_REJECTED.format(loan_id, loans[loan_id]['user_id']))
            return True
        return False
    except ValueError:
        logger.error(ERROR_LOAN_APPROVAL)
        return False
