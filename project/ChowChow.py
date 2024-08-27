from controller.CustomerController import CustomerController
from controller.RestaurantController import RestaurantController

customer_controller = CustomerController()
restaurant_controller = RestaurantController()


def pick_role():
    print("Enter 1 if you're a Customer: ")
    print("Enter 2 if you're a Restaurant Owner: ")
    print("Enter 0 to Exit...")


def customer_choice():
    print("Enter 1 to Create Customer: ")
    print("Enter 2 to Search Restaurant by Food: ")
    print("Enter 3 to Search Restaurant by Name: ")
    print("Enter 4 Place Order: ")
    print("Enter 5 Cancel Order: ")
    print("Enter 6 Show My Orders: ")
    print("Enter 0 to Exit...")


def restaurant_choice():
    print("Enter 1 to Add Restaurant: ")
    print("Enter 2 to Add Food Item to Restaurant: ")
    print("Enter 3 to Show Restaurant Menu: ")
    print("Enter 4 to Update Restaurant Food Menu: ")
    print("Enter 5 to Remove Food Item from Restaurant: ")
    print("Enter 0 to Exit...")


def customer_operations():
    while True:
        try:
            customer_choice()
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                name = input("Enter Your Name: ")
                email = input("Enter Your Email: ")
                mobile_number = input("Enter Your MobileNumber: ")
                location = input("Enter Your Location: ")
                customer = customer_controller.add_new_customer(
                    name, email, mobile_number, location
                )
                print(customer)
            elif choice == 0:
                print("Exiting....")
                break
            else:
                print("Invalid Choice Enter the Valid input")
        except ValueError:
            print("Invalid Input Enter your Choice as Numeric Value")


def restaurant_operations():
    while True:
        try:
            restaurant_choice()
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                name = input("Enter Your Restaurant Name: ")
                email = input("Enter Your Restaurant Email Id: ")
                contact_number = input(
                    "Enter Your Restaurant Contact Number: "
                )
                location = input("Enter Your Restaurant location: ")
                restaurant = restaurant_controller.add_new_restaurant(
                    name, email, contact_number, location
                )
                print(restaurant)
            elif choice == 2:
                restaurant_id = input("Enter Your Restaurant Id")
                name = input("Enter the Food Item Name: ")
                price = float(input("Enter the Food Item Price: "))
                food_item = restaurant_controller.add_food_item_to_restaurant(
                    restaurant_id, name, price
                )
                print(f"Food Item Added Successfully to Restaurant with id :"
                      f"{restaurant_id}") if food_item else print(
                    "Unable to Save Food Item"
                )
            else:
                print("Invalid Choice Enter the Valid Input")
        except ValueError:
            print("Invalid Input Enter your Choice as Numeric Value")


def chow_now():
    while True:
        try:
            pick_role()
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                customer_operations()
            elif choice == 2:
                restaurant_operations()
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid Choice, Enter the valid input..")
        except ValueError:
            print("Invalid Input Enter your Choice as Numeric Value")


if __name__ == "__main__":
    chow_now()
