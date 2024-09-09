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
# Variable Constants
INPUT_RESTAURANT_ID = "Enter Your Restaurant Id: "
INPUT_FOOD_NAME = "Enter the Food Item Name: "
INPUT_FOOD_PRICE = "Enter the Food Item Price: "
INPUT_FOOD_NAME_LIST = "Enter food item names (comma separated like 'food1, food2'): "

#Dict Keys
NAME_KEY = "name"
EMAIL_KEY = "email"
CONTACT_KEY = "contact_numbers"
LOCATION_KEY = "location"
MENU_KEY = "menu"
PRICE_KEY = "price"

#success info
RESTAURANT_ADDED_SUCCESSFULLY = "Restaurant {name} created successfully with ID {id}."
FOOD_ADDED_SUCCESSFULLY ="Food Item Added Successfully to Restaurant with id:{restaurant_id}"
FOOD_UPDATED_SUCCESSFULLY ="Food item with name: {name} updated Successfully"
FOOD_DELETED_SUCCESSFULLY ="Food item deleted successfully"
RESTAURANT_DELETED = "Restaurant with this id {unique_id} deleted successfully"
#unsuccess warn
UNABLE_TO_ADD_FOOD ="Unable to Save Food Item Restaurant with this id:{restaurant_id} not found"
FOOD_ALREADY_EXISTS ="Food item with this name {name} Already exists"
RESTAURANT_NOT_FOUND ="Restaurant with ID {restaurant_id} not found."
FOOD_NOT_FOUND = "Food item with this name: {name} not found"
NO_VALID_FOOD_ITEMS_RESTAURANT = "No valid food items found in the restaurant menu."
UPDATE_RESTAURANT_NOT_FOUND = "Restaurant with this id: {unique_id} not found to update"

#Invalid messages
INVALID_NAME = "Invalid Name, Enter the Valid Name"
INVALID_EMAIL = "Invalid Email, Enter the Valid Email"
INVALID_CONTACT = "Enter the Valid Contact number"
INVALID_LOCATION = "Invalid location, Enter only non numeric values"
INVALID_PASSWORD = "Password does not meet the requirements. Please try again."
INVALID_LICENSE = "Invalid license number, Enter the Valid license number"
INVALID_PRICE = "Invalid Format, Enter the Valid Price without Strings"

IS_DELETE = "is_delete"