from controller.loan import request_amount, sanction, deny
from controller.user import sign_in, login, add_amount


from constant.constant import (MAIN_CHOICE, USER_CHOICE, EXIT, INVALID_CHOICE, ONE, TWO, THREE, FOUR, FIVE,
                               USER_LOGIN_SUCCESS, MAIN_MENU, ADD_AMT_SUCCESS, ADD_AMT_FAILURE,
                               ADD_AMT_CONTRIBUTE, CONTRIBUTION_FAILURE, INPUT_LOAN_AMT, LOAN_REQUEST_FAIL,
                               USER_MENU, ADMIN_MENU, INPUT_USERNAME, INPUT_PASS, INPUT_EMAIL, INPUT_AMT,
                               CONTRIBUTION_SUCCESS, LOAN_REQUEST, EXIT_MAIN, DISPLAY_BALANCE, ERROR_BALANCE,
                               LOGIN_FAIL, USER_CREATION_FAIL, POOL_CREATION_SUCCESS, POOL_BALANCE,
                               POOL_BALANCE_FAIL, INPUT_LOAN_APPROVE, INPUT_LOAN_REJECT, LOAN_APPROVE_SUCCESS,
                               LOAN_APPROVE_FAILURE, LOAN_REJECT_SUCCESS, LOAN_REJECT_FAILURE)

from service.pool import create_new, contribute_current, get_pool_balance
from service.user import get_user_balance


def main_menu():
    """
    Initial main menu when user enters the application:
    User can enter the input as 1-3 as string type.
    '1' - Redirects to the User menu function
    '2' - Redirects to the Admin menu function
    '3' - Exits from the application
    :return: Returns a function of other menu as per user's choice
    """
    print(MAIN_MENU)

    while True:
        choice = input(MAIN_CHOICE)
        if choice == ONE:
            user_menu()
        elif choice == TWO:
            admin_menu()
        elif choice == THREE:
            print(EXIT)
            break
        else:
            print(INVALID_CHOICE)


def user_menu():
    """
    Flow of User Menu:
    * After selecting the user option in the main menu, the user_menu gets input username, password, and email.
    * User created with ID. And logs in the user menu where options are given.
    * User can then choose to add money, contribute to pool, request a loan, check balance, or exit.
    :return: None
    """
    try:
        username = input(INPUT_USERNAME)
        password = input(INPUT_PASS)
        email = input(INPUT_EMAIL)

        user_id = sign_in(username, password, email)
        if user_id:
            if login(username, password):
                print(USER_LOGIN_SUCCESS.format(user_id))
                while True:
                    print(USER_MENU)
                    choice = input(USER_CHOICE)

                    if choice == ONE:
                        amount = float(input(INPUT_AMT))
                        if add_amount(user_id, amount):
                            print(ADD_AMT_SUCCESS)
                        else:
                            print(ADD_AMT_FAILURE)
                    elif choice == TWO:
                        amount = float(input(ADD_AMT_CONTRIBUTE))
                        if contribute_current(user_id, amount):
                            print(CONTRIBUTION_SUCCESS)
                        else:
                            print(CONTRIBUTION_FAILURE)
                    elif choice == THREE:
                        amount = float(input(INPUT_LOAN_AMT))
                        loan_id = request_amount(user_id, amount)
                        if loan_id:
                            print(LOAN_REQUEST.format(loan_id))
                        else:
                            print(LOAN_REQUEST_FAIL)
                    elif choice == FOUR:
                        balance = get_user_balance(user_id)
                        if balance is not None:
                            print(DISPLAY_BALANCE.format(balance))
                        else:
                            print(ERROR_BALANCE)
                    elif choice == FIVE:
                        print(EXIT_MAIN)
                        print(MAIN_MENU)
                        break
                    else:
                        print(INVALID_CHOICE)
            else:
                print(LOGIN_FAIL)
        else:
            print(USER_CREATION_FAIL)
    except ValueError as e:
        print(f"Error: {e}")


def admin_menu():
    """
    Admin Menu Console:
    - Admin user can select the choice from 1-5 as a string data type.
    '1' - Admin creates a new pool.
    '2' - Admin gets the pool balance.
    '3' - Admin can approve loan requests.
    '4' - Admin can reject loan requests.
    '5' - Exit application.
    :return: None
    """
    while True:
        print(ADMIN_MENU)
        choice = input(USER_CHOICE)

        try:
            if choice == ONE:
                create_new()
                print(POOL_CREATION_SUCCESS)
            elif choice == TWO:
                balance = get_pool_balance()
                if balance is not None:
                    print(POOL_BALANCE.format(balance))
                else:
                    print(POOL_BALANCE_FAIL)
            elif choice == THREE:
                loan_id = input(INPUT_LOAN_APPROVE)
                if sanction(loan_id):
                    print(LOAN_APPROVE_SUCCESS)
                else:
                    print(LOAN_APPROVE_FAILURE)
            elif choice == FOUR:
                loan_id = input(INPUT_LOAN_REJECT)
                if deny(loan_id):
                    print(LOAN_REJECT_SUCCESS)
                else:
                    print(LOAN_REJECT_FAILURE)
            elif choice == FIVE:
                print(EXIT_MAIN)
                print(MAIN_MENU)
                break
            else:
                print(INVALID_CHOICE)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    """
    Initial function call of the application
    - Main menu is called here where the user is then allowed to enter choice.
    """
    main_menu()
