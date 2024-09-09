DELIVERY_PERSON_CHOICE = '''
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

DELIVERY_PERSON_UPDATE_CHOICE = '''
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
# un success messages
UPDATE_DELIVERY_PERSON_NOT_FOUND = "Delivery person with this id: {unique_id} not found to update"
DELIVERY_PERSON_NOT_FOUND = "Delivery person with this id: {unique_id} not found"
DELIVERY_PERSON_HAS_NO_ORDER_TO_PICK = "Delivery person has no order to pick up."
DELIVERY_PERSON_HAS_NO_ORDER_TO_DELIVER = "Delivery person has no order to deliver."
# success messages
DELIVERY_PERSON_ADDED = "Delivery person details added with this id {unique_id}"
RATING_UPDATED = "Ratings updated Successfully"
INVALID_RATING = "Rating must be between 1 and 5."
# input
INPUT_DELIVERY_PERSON_ID = "Enter Delivery Person ID: "
INPUT_RATING = "Enter rating (1-5): "

# keys
CURRENT_ORDER_ID_KEY = "current_order_id"

