# Restaurant choice
ADD_RESTAURANT = "Enter 1 to Add Restaurant: "
ADD_FOOD_ITEM = "Enter 2 to Add Food Item to Restaurant: "
SHOW_MENU = "Enter 3 to Show Restaurant Menu: "
UPDATE_FOOD_ITEM = "Enter 4 to Update Restaurant Food Menu: "
REMOVE_FOOD_ITEM = "Enter 5 to Remove Food Item from Restaurant: "

# Variable Constants
INPUT_RESTAURANT_ID = "Enter Your Restaurant Id: "
RESTAURANT_CONTACT_COUNT = ("You can add one or two contact numbers for your Restaurant, "
                            "Enter 1 if you want to add one or Enter 2 if you want to add two: ")
INPUT_FOOD_NAME = "Enter the Food Item Name: "
INPUT_FOOD_PRICE = "Enter the Food Item Price: "

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
#unsuccess warn
UNABLE_TO_ADD_FOOD ="Unable to Save Food Item Restaurant with this id:{restaurant_id} not found"
FOOD_ALREADY_EXISTS ="Food item with this name {name} Already exists"
RESTAURANT_NOT_FOUND ="Restaurant with this id:{restaurant_id} not found"
FOOD_NOT_FOUND = "Food item with this name: {name} not found"

#Invalid messages
INVALID_NAME = "Invalid Name, Enter the Valid Name"
INVALID_EMAIL = "Invalid Email, Enter the Valid Email"
INVALID_CONTACT = "Enter the Valid Contact number"
INVALID_LOCATION = "Invalid location, Enter only non numeric values"