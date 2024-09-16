from Controllers.user_controller import user_creation_controller, user_login_controller, add_money_controller


def user_menu():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    user_id = user_creation_controller(username, password, email)
    if user_id:
        print("User created with ID: {}".format(user_id))

        if user_login_controller(username, password):
            print("Login successful.")
            amount = float(input("Enter amount to add: "))
            if add_money_controller(user_id, amount):
                print("Money added successfully.")
            else:
                print("Failed to add money.")
        else:
            print("Login failed.")
