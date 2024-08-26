from controller.CustomerController import CustomerController
from controller.RestaurantController import RestaurantController

customer_controller = CustomerController()
restaurant_controller = RestaurantController()


def pick_role():
    print("Enter 1 if you're a Customer: ")
    print("Enter 2 if you're a Restaurant Owner: ")


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


def chow_now():
    pick_role()
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        while True:
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
                print("Invalid Choice")

    elif choice == 2:
        while True:
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
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    chow_now()
