from service.restaurant_service import (
    add_new_restaurant, add_new_food_item,
    get_restaurant_menu, update_food_item_details, delete_food_item_details
)


def add_restaurant(name: str, email: str,
                   contact_numbers: list[str], location: str):
    """
    Adds a new restaurant to the restaurants dictionary with a unique ID.

    Parameters:
    - name (str): The name of the restaurant.
    - email (str): The email address of the restaurant.
    - contact_number (str): The contact number of the restaurant.
    - location (str): The physical location of the restaurant.

    Returns:
    - str: A unique ID of the new restaurant.
    """
    return add_new_restaurant(
        name.lower(), email.lower(), contact_numbers, location.lower()
    )


def add_food_item(restaurant_id: str,
                  name: str, price: float):
    """
    Adds a new food item to the menu of a specified restaurant.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.
    - name (str): The name of the food item.
    - price (float): The price of the food item.

    Returns:
    - bool: True if the food item was added successfully, False if the item already exists.
    - None: If the restaurant was not found.
    """
    return add_new_food_item(
        restaurant_id, name.lower(), price
    )


def get_menu(restaurant_id: str):
    """
    Finds a restaurant by its unique ID.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - dict: The restaurant details if found, None otherwise.
    """
    return get_restaurant_menu(restaurant_id)


def update_food_item(restaurant_id: str, name: str, price: float):
    """
    Retrieves the menu of a specified restaurant.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - list: The menu of the restaurant if found, None otherwise.
    """
    return update_food_item_details(restaurant_id, name.lower(), price)


def delete_food_item(restaurant_id: str, name: str):
    """
    Updates the details of a specific food item in a restaurant's menu.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.
    - name (str): The name of the food item to update.
    - price (float): The new price for the food item.

    Returns:
    - bool: True if the food item was updated successfully, False if the item was not found.
    - None: If the restaurant was not found.
    """
    return delete_food_item_details(restaurant_id, name.lower())
