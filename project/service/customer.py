import uuid

from project.constant.constant import (
    STATUS, STATUS_PLACED, SIX, PASSWORD_KEY,
    IS_DELETE, LOCATION_KEY)
from project.service.restaurant import get as get_restaurant

customers = {}

carts = {}

orders = {}


def add(name: str, password, email: str,
        mobile_number: str, location: str):
    """
    Registers a new customer and assigns them a unique ID.

    Parameters:
    - name (str): The customer's name.
    - password: The customer's password.
    - email (str): The customer's email address.
    - mobile_number (str): The customer's mobile number.
    - location (str): The customer's location.

    Returns:
    - str: The unique ID assigned to the customer.
    """
    unique_id = str(uuid.uuid4())
    customers[unique_id] = {
        "name": name,
        "password": password,
        "email": email,
        "mobile_number": mobile_number,
        "location": location,
        "orders": [],
        IS_DELETE: False
    }
    return unique_id


def get(customer_id: str):
    """
    Retrieves a customer's details by their unique ID if they are not marked as deleted.

    Parameters:
    - customer_id (str): The unique ID of the customer.

    Returns:
    - dict: The customer's details, or None if the customer is not found or is deleted.
    """
    customer = customers.get(customer_id)
    if customer:
        if not customer[IS_DELETE]:
            return customer
    return None


def filter_customer_info(customer):
    """
       Filters out sensitive information (e.g., password) from a customer's details.

       Parameters:
       - customer (dict): The customer's full details.

       Returns:
       - dict: The customer's details with sensitive information removed.
    """
    return {key: value for key, value in customer.items() if key not in [PASSWORD_KEY, IS_DELETE]}


def get_all():
    """
    Retrieves all customers who are not marked as deleted.

    Returns:
    - dict: A dictionary of all customers with their sensitive information removed.
    """
    filtered_customers = {
        customer_id: filter_customer_info(customer)
        for customer_id, customer in customers.items()
        if not customer.get(IS_DELETE, False)
    }
    return filtered_customers


def update(customer, to_update: str, detail_to_update: str):
    """
    Updates a specific detail of a customer.

    Parameters:
    - customer (dict): The customer's details.
    - to_update (str): The key of the detail to update.
    - detail_to_update (str): The new value for the specified detail.

    Returns:
    - bool: True if the update was successful.
    """
    customer[to_update] = detail_to_update
    return True


def remove(unique_id: str):
    """
    Marks a customer as deleted.

    Parameters:
    - unique_id (str): The unique ID of the customer to delete.

    Returns:
    - bool: True if the customer was successfully marked as deleted, None if the customer was not found.
    """
    customer = get(unique_id)
    if customer:
        customer[IS_DELETE] = True
        return True
    return None


def add_to_cart(customer_id: str, restaurant, restaurant_id, food_item_names: list[str]):
    """
        Adds selected food items to the customer's cart.

        Parameters:
        - customer_id (str): The unique ID of the customer.
        - restaurant (dict): The restaurant's details.
        - restaurant_id (str): The unique ID of the restaurant.
        - food_item_names (list[str]): The names of the food items to add to the cart.

        Returns:
        - bool: True if the items were successfully added to the cart, False otherwise.
    """
    food_items = [{key: value for key, value in item.items() if key not in [IS_DELETE]} for item in restaurant["menu"]
                  if item["name"] in food_item_names]

    if food_items:
        cart_id = str(uuid.uuid4())
        carts[customer_id] = {
            "id": cart_id,
            "customer_id": customer_id,
            "restaurant_id": restaurant_id,
            "food_items": food_items,
            "total_price": price_calculator(food_items),
            "status": "pending"
        }
        return True
    return False


def price_calculator(food_items):
    """
    Calculates the total price of the items in the cart.

    Parameters:
    - food_items (list[dict]): A list of food items with their details (including price).

    Returns:
    - float: The total price of all the items in the cart.
    """
    total = 0
    for food_item in food_items:
        total += food_item["price"]
    return total


def update_items_to_cart(food_item_names: list, cart: dict):
    """
    Adds additional items to an existing cart.

    Parameters:
    - food_item_names (list[str]): A list of food item names to add to the cart.
    - cart (dict): The current cart details.

    Returns:
    - list: A list of food items that were successfully added to the cart.
    """
    restaurant = get_restaurant(cart["restaurant_id"])

    if restaurant:
        food_items_to_add = [item for item in restaurant["menu"] if item["name"] in food_item_names]
        cart["food_items"].extend(food_items_to_add)
        cart["total_price"] = price_calculator(cart["food_items"])
        return food_items_to_add

    return []


def remove_items_from_cart(food_item_names: list, cart: dict):
    """
    Removes specified items from the cart.

    Parameters:
    - food_item_names (list[str]): A list of food item names to remove from the cart.
    - cart (dict): The current cart details.

    Returns:
    - list: A list of food item names that were successfully removed from the cart, or an empty list if none were removed.
    """
    original_length = len(cart["food_items"])
    cart["food_items"] = [item for item in cart["food_items"] if item["name"] not in food_item_names]

    if len(cart["food_items"]) < original_length:
        cart["total_price"] = price_calculator(cart["food_items"])
        return food_item_names

    return []


def get_cart_by_customer(customer_id):
    """
    Retrieves the cart for a specific customer.

    Parameters:
    - customer_id (str): The unique ID of the customer.

    Returns:
    - dict: The cart associated with the customer, or None if no cart exists.
    """
    return carts.get(customer_id)


def get_order(order_id: str):
    """
    Retrieves an order by its unique ID.

    Parameters:
    - order_id (str): The unique ID of the order.

    Returns:
    - dict: The order details, or None if the order is not found.
    """
    return orders.get(order_id)


def get_all_orders():
    """
    Retrieves all orders.

    Returns:
    - dict: A dictionary of all orders.
    """
    return orders


def get_customer_orders(customer):
    customer_orders = get_all_orders()
    return [customer_orders[order_id] for order_id in customer['orders']]


def place_order(cart: dict, customer_id: str, payment_mode: str):
    """
    Places an order using the current cart and assigns an OTP.

    Parameters:
    - cart (dict): The current cart details.
    - customer_id (str): The unique ID of the customer placing the order.
    - payment_mode (str): The chosen payment method for the order.

    Returns:
    - dict: The order details with an assigned OTP.
    """
    order_id = str(uuid.uuid4())
    otp = str(uuid.uuid4().int)[:SIX]
    order = {
        "order_id": order_id,
        "customer_id": customer_id,
        "restaurant_id": cart["restaurant_id"],
        "food_items": cart["food_items"],
        "status": "Placed",
        "delivery_partner_id": None,
        "payment_mode": payment_mode,
        "otp": otp
    }
    orders[order_id] = order
    customers[customer_id]["orders"].append(order_id)
    del carts[customer_id]
    return order


def list_available_orders(delivery_partner_location: str):
    """
    Lists all available orders for delivery based on the delivery person's location.

    Parameters:
    - delivery_partner_location (str): The location of the delivery person.

    Returns:
    - list: A list of orders available for delivery from the specified location.
    """
    available_orders = [
        order for order in orders.values()
        if order[STATUS] == STATUS_PLACED and get_restaurant(order['restaurant_id'])[
            LOCATION_KEY].lower() == delivery_partner_location.lower()]
    return available_orders
