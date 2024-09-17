# Regex
EMAIL_REGEX = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
MOBILE_NUMBER_REGEX = r"^[6-9]\d{9}$"
NAME_REGEX = r"^[A-Za-z\s\-']+$"
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
LICENSE_REGEX = r'^[A-Z]{2}[0-9]{2}[0-9]{4}[0-9]{7}$|^[A-Z]{2}[0-9]{13}$'
LOCATION_REGEX = r"\b(?:Adyar|Anna Nagar|T. Nagar|Velachery|Nungambakkam|Kodambakkam|Mylapore|Besant Nagar|Royapettah|Triplicane|Guindy|Saidapet|Chromepet|Tambaram|Perungudi|Pallavaram|Thiruvanmiyur|Sholinganallur|Vadapalani|Kotturpuram|Egmore|Ambattur|Ashok Nagar|Alwarpet|Thiruvottiyur|Porur|Perambur|Teynampet|Mount Road|Mandaveli|Kottivakkam|Madipakkam|Kovilambakkam|Kandanchavadi|Aminjikarai|Taramani|Ramapuram|Padi)\b"

# Auth
ROLE = '''
==================================
          WELCOME TO CHOWNOW       
==================================
Please select your role:
----------------------------------
1. Customer
2. Restaurant Owner
3. Delivery Partner
0. Exit
----------------------------------
Enter your choice (0-3): '''

# Common Prompts
EXITING = "Exiting...."
PICK_CHOICE = "Enter Your Choice: "
INVALID_CHOICE = "Invalid Choice, Enter the valid input.."

# Variable Constants
INPUT_ID = "Enter Your id:"
INPUT_NAME = "Enter the Name: "
INPUT_EMAIL = "Enter the Email: "
INPUT_CONTACT = "Enter the Mobile Number: "
INPUT_ALTERNATE_CONTACT = "Enter your alternate contact number (optional, Enter 0 to skip): "
INPUT_LOCATION = "Enter the Location: "
INPUT_LICENSE_NUMBER = "Enter your license number: "
INPUT_PASSWORD = '''
Please enter a strong password that meets the following requirements:
- At least 8 characters long.
- Contains at least one uppercase letter (A-Z).
- Contains at least one lowercase letter (a-z).
- Contains at least one number (0-9).
- Contains at least one special character (e.g., @$!%*?&).
Example: P@ssw0rd1
'''
INPUT_OTP = "Enter OTP to verify delivery: "
INPUT_CUSTOMER_ID = "Enter customer ID: "
INPUT_DELIVERY_PARTNER_ID = "Enter Delivery Person ID: "
INPUT_RATING = "Enter rating (1-5): "
INPUT_RESTAURANT_ID = "Enter Your Restaurant Id: "
INPUT_FOOD_NAME = "Enter the Food Item Name: "
INPUT_FOOD_PRICE = "Enter the Food Item Price: "
INPUT_FOOD_NAME_LIST = "Enter food item names (comma separated like 'food1, food2'): "

# Invalid messages
INVALID_INPUT = "Invalid Input"
ENTER_CHOICE_AS_NUMERIC = "Enter Your choice as numeric either 1 or 2"
INVALID_OTP = "Invalid OTP."
INVALID_CONFIRMATION = "Invalid choice enter Either yes or no"
INVALID_PAYMENT_MODE = "Invalid Choice enter Either Upi or Cash"
INVALID_NAME = "Invalid Name, Enter the Valid Name"
INVALID_EMAIL = "Invalid Email, Enter the Valid Email"
INVALID_CONTACT = "Enter the Valid Contact number"
INVALID_LOCATION = "Invalid location, Enter only non numeric values"
INVALID_PASSWORD = "Password does not meet the requirements. Please try again."
INVALID_LICENSE = "Invalid license number, Enter the Valid license number"
INVALID_PRICE = "Invalid Format, Enter the Valid Price without Strings"

# success messages
NAME_UPDATED = "Name updated Successfully"
EMAIL_UPDATED = "Email updated Successfully"
MOBILE_NUMBER_UPDATED = "Mobile Number  updated Successfully"
LOCATION_UPDATED = "Location updated Successfully"
LICENSE_NUMBER_UPDATED = "License number updated Successfully"
PASSWORD_UPDATED = "password updated Successfully"

# common keys
PASSWORD_KEY = "password"
MOBILE_NUMBER_KEY = "mobile_number"
LICENSE_NUMBER_KEY = "license_number"
AVAILABLE_ORDERS = "Available Orders: "
NO_AVAILABLE_ORDERS = "No available orders."
STATUS = "status"
STATUS_PENDING = "pending"
STATUS_PLACED = "Placed"
STATUS_IN_TRANSPORT = "In Transport"
STATUS_ASSIGNED = "Assigned"
ORDER_ID_KEY = "order_id"
CURRENT_ORDER_ID_KEY = "current_order_id"
IS_DELETE = "is_delete"
NAME_KEY = "name"
EMAIL_KEY = "email"
CONTACT_KEY = "contact_numbers"
LOCATION_KEY = "location"
MENU_KEY = "menu"
PRICE_KEY = "price"

# choices
ADD_CHOICE = "add"
REMOVE_CHOICE = "remove"
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
ELEVEN = 11
TWELVE = 12
ZERO = 0

# customer choice
CUSTOMER_CHOICE = '''
==================================
         WELCOME TO CHOWNOW       
==================================
Customer Menu:
----------------------------------
1. Create Customer
2. Show Restaurants
3. Show Restaurant Menu
4. Add to Cart
5. View Cart
6. Edit Cart
7. Place Order
8. Rate delivery partner
9. Show My Orders
10. Update Customer
11. Remove Customer
12. Show My Details
0. Exit
----------------------------------
Enter your choice (0-12): 
'''

CUSTOMER_UPDATE_CHOICE = '''
1. Update Name
2. Update Email
3. Update Mobile Number
4. Update Location
5. Update Password
0. Exit

Enter your choice (0-5)
'''
# customer un success messages
UPDATE_CUSTOMER_NOT_FOUND = "Customer with this id: {unique_id} not found to update"
CUSTOMER_NOT_FOUND = "Customer with ID {customer_id} not found."

# customer success messages
CUSTOMER_ADDED = "Customer successfully added with id: {customer_id}"
CUSTOMER_DELETED = "Customer with this id {customer_id} deleted successfully"

# cart
ALREADY_HAVE_PENDING_CART = "You already have a pending cart. Please place or clear your current cart before adding new items."
ITEMS_ADDED_TO_CART = "Items added to cart: {food_item_names}"
ITEMS_REMOVED_FROM_CART = "Items removed from cart: {removed_items}"
NO_CART_FOUND = "No cart found for Customer ID {customer_id}."
ADD_OR_REMOVE_ITEM_FROM_CART = "Do you want to add or remove items from the cart? (add/remove): "
NO_VALID_FOOD_ITEMS_CART = "No valid food items found in the cart."
INVALID_ADD_OR_REMOVE_ITEM_FROM_CART = "Invalid choice. Please choose 'add' or 'remove'."
NO_PENDING_CART = "No pending cart found for this customer or the cart is already processed."
INPUT_WANT_TO_PLACE_ORDER = "Do you want to place the order? (yes/no): "
INPUT_PAYMENT_MODE = "Which payment mode you choose? (upi/cash): "
VALUE_YES = "yes"
VALUE_NO = "no"
ORDER_PLACED = "Order placed successfully!"
ORDER_DETAILS = "Order details:{order}"
ORDER_NOT_PLACED = "Order not placed. Cart status remains pending."
PAYMENT_MODE_CASH = "cash"
PAYMENT_MODE_UPI = "upi"

# order
INPUT_ORDER_ID = "Enter Order ID : "
ORDER_NOT_FOUND_OR_NOT_AVAILABLE = "Order not found or not available for assignment."
ORDER_NOT_FOUND_OR_NOT_ASSIGNED = "Order not found or is not assigned."
ORDER_NOT_FOUND_OR_NOT_IN_TRANSPORT = "Order not found or is not in transport."
ORDER_DELIVERED = "Order {order_id} has been delivered successfully."
ORDER_ASSIGNED_TO_DELIVERY_PARTNER = "Order {order_id} has been assigned to Delivery Person {unique_id}."
ORDER_PICKED_BY_DELIVERY_PARTNER = "Order {order_id} has been picked up by Delivery Person {unique_id}."

# delivery partner choice
DELIVERY_PARTNER_CHOICE = '''
1. Create Delivery person
2. Update Delivery person
3. Show Available Orders
4. Assign Order 
5. Pick Order
6. Verify and Deliver Order 
7. Show My Details
0. Exit
----------------------------------
Enter your choice (0-7):
'''

DELIVERY_PARTNER_UPDATE_CHOICE = '''
1. Update Name
2. Update Email
3. Update Mobile Number
4. Update Location
5. Update License Number
6. Update Password
0. Exit
----------------------------------
Enter your choice (0-6):
'''

# delivery person un success messages
UPDATE_DELIVERY_PARTNER_NOT_FOUND = "Delivery partner with this id: {unique_id} not found to update"
DELIVERY_PARTNER_NOT_FOUND = "Delivery partner with this id: {unique_id} not found"
DELIVERY_PARTNER_HAS_NO_ORDER_TO_PICK = "Delivery partner has no order to pick up."
DELIVERY_PARTNER_HAS_NO_ORDER_TO_DELIVER = "Delivery partner has no order to deliver."

# delivery person success messages
DELIVERY_PARTNER_ADDED = "Delivery partner details added with this id {unique_id}"
RATING_UPDATED = "Ratings updated Successfully"
INVALID_RATING = "Rating must be between 1 and 5."

# Restaurant choice
RESTAURANT_CHOICE = '''
==================================
         WELCOME TO CHOWNOW       
==================================
Please select an operation:
----------------------------------
1. Add Restaurant
2. Add Food Item to Restaurant
3. Show Restaurant Menu
4. Update Restaurant Food Menu
5. Remove Food Item from Restaurant
6. Show My Restaurant 
7. Remove Restaurant
8. Update My Restaurant Details 
0. Exit
----------------------------------
Enter your choice (0-8): '''
RESTAURANT_UPDATE_CHOICE = '''
1. Update Name
2. Update Email
3. Update Mobile Number
4. Update Location
5. Update Password
0. Exit
----------------------------------
Enter your choice (0-5): 
'''

# restaurant success messages
RESTAURANT_ADDED_SUCCESSFULLY = "Restaurant {name} created successfully with ID {id}."
FOOD_ADDED_SUCCESSFULLY = "Food Item Added Successfully to Restaurant with id:{restaurant_id}"
FOOD_UPDATED_SUCCESSFULLY = "Food item with name: {name} updated Successfully"
FOOD_DELETED_SUCCESSFULLY = "Food item deleted successfully"
RESTAURANT_DELETED = "Restaurant with this id {unique_id} deleted successfully"

# restaurant un success messages
UNABLE_TO_ADD_FOOD = "Unable to Save Food Item Restaurant with this id:{restaurant_id} not found"
FOOD_ALREADY_EXISTS = "Food item with this name {name} Already exists"
RESTAURANT_NOT_FOUND = "Restaurant with ID {restaurant_id} not found."
FOOD_NOT_FOUND = "Food item with this name: {name} not found"
NO_VALID_FOOD_ITEMS_RESTAURANT = "No valid food items found in the restaurant menu."
UPDATE_RESTAURANT_NOT_FOUND = "Restaurant with this id: {unique_id} not found to update"