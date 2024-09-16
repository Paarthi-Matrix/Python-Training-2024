from Controllers.loan_controller import request_loan_controller, approve_loan_controller, reject_loan_controller
from Services.pool_service import create_new_pool, contribute, get_pool_balance


def admin_menu():
    while True:
        print("1. Create New Pool")
        print("2. Contribute to Pool")
        print("3. Get Pool Balance")
        print("4. Request Loan")
        print("5. Approve Loan")
        print("6. Reject Loan")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_new_pool()
        elif choice == '2':
            user_id = input("Enter user ID: ")
            amount = float(input("Enter amount to contribute: "))
            if contribute(user_id, amount):
                print("Contribution successful.")
            else:
                print("Contribution failed.")
        elif choice == '3':
            balance = get_pool_balance()
            if balance is not None:
                print(f"Pool Balance: {balance}")
            else:
                print("Failed to fetch pool balance.")
        elif choice == '4':
            user_id = input("Enter user ID: ")
            amount = float(input("Enter loan amount: "))
            loan_id = request_loan_controller(user_id, amount, pools={})
            if loan_id:
                print(f"Loan requested with ID: {loan_id}")
            else:
                print("Loan request failed.")
        elif choice == '5':
            loan_id = input("Enter loan ID to approve: ")
            if approve_loan_controller(loan_id):
                print("Loan approved.")
            else:
                print("Failed to approve loan.")
        elif choice == '6':
            loan_id = input("Enter loan ID to reject: ")
            if reject_loan_controller(loan_id):
                print("Loan rejected.")
            else:
                print("Failed to reject loan.")
        elif choice == '7':
            break
        else:
            print("Invalid choice.")
