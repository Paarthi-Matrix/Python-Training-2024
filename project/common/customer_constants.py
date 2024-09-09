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
8. Rate delivery person
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
# un success messages
UPDATE_CUSTOMER_NOT_FOUND = "Customer with this id: {unique_id} not found to update"
CUSTOMER_NOT_FOUND = "Customer with ID {customer_id} not found."

# success messages
CUSTOMER_ADDED = "Customer successfully added with id: {customer_id}"
CUSTOMER_DELETED = "Customer with this id {customer_id} deleted successfully"

# input
INPUT_CUSTOMER_ID = "Enter customer ID: "

# cart
ALREADY_HAVE_PENDING_CART = "You already have a pending cart. Please place or clear your current cart before adding new items."
ITEMS_ADDED_TO_CART = "Items added to cart: {food_item_names}"
ITEMS_REMOVED_FROM_CART ="Items removed from cart: {removed_items}"
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
ORDER_ASSIGNED_TO_DELIVERY_PERSON = "Order {order_id} has been assigned to Delivery Person {unique_id}."
ORDER_PICKED_BY_DELIVERY_PERSON = "Order {order_id} has been picked up by Delivery Person {unique_id}."
