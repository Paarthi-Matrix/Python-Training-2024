from service.customer_service import (search_customer, register_customer,
                                      get_all_customer, remove_customer, is_customer_present,
                                      update_customer)
from util.validation import (is_valid_name, is_valid_email,
                             is_valid_password, is_valid_mobile)

from admin_controller import register_admin


def get_valid_input(prompt, validation_func, error_message):
    """Helper function to get and validate input."""
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)


def collect_customer_details():
    customer_name = get_valid_input(
        "Enter the customer name: ",
        is_valid_name,
        "Name should only contain lowercase, uppercase letters, and spaces."
    )

    customer_email = get_valid_input(
        "Enter the email: ",
        is_valid_email,
        "Email should contain lowercase letters, numbers, "
        "and end with the suffix (@gmail.com)."
    )

    password = get_valid_input(
        "Enter the password: ",
        is_valid_password,
        "Password must be at least 8 characters long, contain one uppercase "
        "letter, one lowercase letter, one number, and no spaces."
    )

    mobile_no = get_valid_input(
        "Enter the mobile number: ",
        is_valid_mobile,
        "Mobile number should have 10 digits, and start with 6, 7, 8, or 9."
    )

    account_no = input("Enter the account number: ")

    return customer_name, customer_email, password, mobile_no, account_no


def customer():
    try:
        while True:
            print("Pick your choice")
            print("1. Sign Up Customer")
            print("2. Register Bin")
            print("3. Raise Complaint")
            print("4. Exit")

            choice = int(input("Enter your choice:"))
            if choice >= 1 and choice <= 4:
                print("hello")
                if choice == 1:
                    """(customer_name, customer_email, password,
                     mobile_no, account_no) = customer_validation()"""
                    customer_name, customer_email, password, mobile_no, account_no = collect_customer_details()
                    generated_id = register_customer(
                        customer_name, customer_email, password, mobile_no, account_no
                    )
                    print("Customer registered successfully with ID", generated_id)
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    print("Redirect to Home")
                    break
            else:
                print("Choice should ranges between 1 to 4")
    except ValueError:
        raise ValueError


def update_profile():
    try:
        customer_id = input("Enter the Customer Id:")
        if is_customer_present(customer_id):
            while True:
                print("Choose your choice:")
                print("1. Update name")
                print("2. Update email")
                print("3. Update password")
                print("4. Update mobile")
                print("5. Exit")
                choice = int(input("Enter your choice:"))
                if choice >= 1 and choice <= 5:
                    if choice == 1:
                        name = input("Enter the name to update:")
                        update_customer(customer_id, name, "name")
                        print("Customer detail successfully updated for Id:", customer_id)
                    elif choice == 2:
                        email = input("Enter the email to update:")
                        update_customer(customer_id, email, "email")
                        print("Customer detail successfully updated for Id:", customer_id)
                    elif choice == 3:
                        password = input("Enter the password to update:")
                        update_customer(customer_id, password, "password")
                        print("Customer detail successfully updated for Id:", customer_id)
                    elif choice == 4:
                        mobile = input("Enter the mobile number to update:")
                        update_customer(customer_id, mobile, "mobile")
                        print("Customer detail successfully updated for Id:", customer_id)
                    elif choice == 5:
                        print("Redirect to home")
                        break
                else:
                    print("Enter the choice ranges between (1-5)")
        else:
            print("No Customer found by this Id: ", customer_id)
    except ValueError:
        raise ValueError


def admin():
    try:
        while True:
            print("Pick your choice")
            print("1. Sign Up Admin")
            print("2. Sign Up Driver")
            print("3. Search Customer")
            print("4. Delete Customer")
            print("5. Update Customer")
            print("6. Exit")

            choice = int(input("Enter the choice"))
            if choice >= 1 and choice <= 6:
                if choice == 1:
                    name = input("Enter the name:")
                    email = input("Enter the email:")
                    password = input("Enter the password:")

                    admin_id = register_admin(name, email, password)
                    if admin_id is None:
                        print("Unauthorized, Not allowed to sign up as Admin")
                    else:
                        print("Admin successfully created by this Id: ", admin_id)
                elif choice == 2:
                    pass
                elif choice == 3:
                    while True:
                        print()
                        print("Pick the choice below to search by")
                        print("1. Search by First Name or Last Name")
                        print("2. Search by Id")
                        print("3. Search All")
                        print("4. End the Search")
                        search_choice = int(input("Enter your choice: "))
                        if 1 <= search_choice <= 4:
                            if search_choice == 1:
                                name = input("Enter the name to search:")
                                customers = search_customer(name)
                                if customers is None:
                                    print("No customer found by this name: ", name)
                                else:
                                    for detail in customers:
                                        for key in detail:
                                            print(key, "-", detail[key])
                            elif search_choice == 2:
                                customer_id = input("Enter the customer Id:")
                                customer_detail = search_customer(customer_id)
                                if customer_detail is None:
                                    print("No customer found by this Id: ", customer_id)
                                else:
                                    for detail in customer_detail:
                                        print(detail, "-", customer_detail[detail])
                            elif search_choice == 3:
                                for customer_detail in get_all_customer():
                                    if customer_detail is None:
                                        print("No customers signed up yet")
                                    else:
                                        for key, value in customer_detail.items():
                                            print(key, "-", value)
                            elif search_choice == 4:
                                print("You have ended the search")
                                break
                        else:
                            print("Enter the choice ranges between (1-5)")

                elif choice == 4:
                    customer_id = input("Enter the customer Id:")
                    result = remove_customer(customer_id)
                    if result is None:
                        print("Customer deleted successfully with Id:", customer_id)
                    else:
                        print("No customer found by this Id:", customer_id)

                elif choice == 5:
                    update_profile()
                elif choice == 6:
                    print("Redirecting you to home")
                    break
            else:
                print("Choice should ranges between 1 to 6")
    except ValueError:
        raise ValueError


def main():
    try:
        while True:
            print("Enter the choice:")
            print("1. Customer")
            print("2. Admin")
            print("3. Driver")
            print("4. Exit")
            role = int(input("Choose the Role:"))

            if role >= 1 and role <= 4:
                if role == 1:
                    customer()
                elif role == 2:
                    admin()
                elif role == 3:
                    pass
                elif role == 4:
                    print("Thank You")
                    break
            else:
                print("Choice should ranges between 1 to 4")
    except ValueError:
        print("Role choice should be integer")


if __name__ == "__main__":
    main()
