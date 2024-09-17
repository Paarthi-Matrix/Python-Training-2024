from controller.user import user_creation_controller, user_login_controller, add_money_controller
from controller.loan import request_loan_controller, approve_loan_controller, reject_loan_controller
from service.pool import create_new_pool, contribute, get_pool_balance
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
    print("Welcome to IDEAS2IT Lending System")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    while True:
        choice = input("Enter choice: ")
        if choice == '1':
            user_menu()
        elif choice == '2':
            admin_menu()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def user_menu():
    """
    Flow of User Menu:
    * After selecting the user option in the main menu, the user_menu gets input username, password, and email.
    * User created with ID. And logs in the user menu where options are given.
    * User can then choose to add money, contribute to pool, request a loan, check balance, or exit.
    :return: None
    """
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")

        user_id = user_creation_controller(username, password, email)
        if user_id:
            print("User created with ID: {}".format(user_id))

            if user_login_controller(username, password):
                print("Login successful.")
                while True:
                    print(" USER MENU ")
                    print("-----------------------------")
                    print("1. Add Money")
                    print("2. Contribute to Pool")
                    print("3. Request Loan")
                    print("4. Check Balance")
                    print("5. Exit")
                    print("-----------------------------")

                    choice = input("Enter choice (1-5): ")

                    if choice == '1':
                        amount = float(input("Enter amount to add: "))
                        if add_money_controller(user_id, amount):
                            print("Money added successfully.")
                        else:
                            print("Failed to add money.")
                    elif choice == '2':
                        amount = float(input("Enter amount to contribute: "))
                        if contribute(user_id, amount):
                            print("Contribution successful.")
                        else:
                            print("Failed to contribute.")
                    elif choice == '3':
                        amount = float(input("Enter loan amount: "))
                        loan_id = request_loan_controller(user_id, amount, pools={})
                        if loan_id:
                            print(f"Loan requested with ID: {loan_id}")
                        else:
                            print("Loan request failed.")
                    elif choice == '4':
                        balance = get_user_balance(user_id)
                        if balance is not None:
                            print(f"Your Balance: {balance}")
                        else:
                            print("Failed to fetch balance.")
                    elif choice == '5':
                        print("Exiting to main menu.")
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 5.")
            else:
                print("Login failed.")
        else:
            print("User creation failed.")
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
        print(" ADMIN MENU ")
        print("-----------------------------")
        print("1. Create New Pool")
        print("2. Get Pool Balance")
        print("3. Approve Loan")
        print("4. Reject Loan")
        print("5. Exit")
        print("-----------------------------")

        choice = input("Enter choice (1-5): ")

        try:
            if choice == '1':
                create_new_pool()
                print("New pool created successfully.")
            elif choice == '2':
                balance = get_pool_balance()
                if balance is not None:
                    print(f"Pool Balance: {balance}")
                else:
                    print("Failed to fetch pool balance.")
            elif choice == '3':
                loan_id = input("Enter loan ID to approve: ")
                if approve_loan_controller(loan_id):
                    print("Loan approved successfully.")
                else:
                    print("Failed to approve loan.")
            elif choice == '4':
                loan_id = input("Enter loan ID to reject: ")
                if reject_loan_controller(loan_id):
                    print("Loan rejected successfully.")
                else:
                    print("Failed to reject loan.")
            elif choice == '5':
                print("Exiting to main menu.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    """
    Initial function call of the application
    - Main menu is called here where the user is then allowed to enter choice.
    """
    main_menu()
