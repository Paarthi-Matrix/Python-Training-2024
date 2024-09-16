from Views.user_view import user_menu
from Views.admin_view import admin_menu


def main_menu():
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
            break
        else:
            print("Invalid choice.")
