from Services.loan_service import request_loan, accept_loan, reject_loan


def request_loan_controller(user_id, amount, pools):
    return request_loan(user_id, amount, pools)


def approve_loan_controller(loan_id):
    return accept_loan(loan_id)


def reject_loan_controller(loan_id):
    return reject_loan(loan_id)
