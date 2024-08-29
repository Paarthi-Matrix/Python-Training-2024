import uuid

from common.restaurant_constants import (
    NAME_KEY, EMAIL_KEY, CONTACT_KEY,
    LOCATION_KEY, MENU_KEY, PRICE_KEY
)
from resources.logging_config import logger

restaurants = {}


def add_new_restaurant(name: str, email: str,
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
    id = str(uuid.uuid4())
    restaurants[id] = {
        NAME_KEY: name,
        EMAIL_KEY: email,
        CONTACT_KEY: contact_numbers,
        LOCATION_KEY: location,
        MENU_KEY: []
    }
    logger.debug(find_by_id(id))
    return id


def add_new_food_item(restaurant_id: str,
                      name: str, price: float):
    """
    Adds a new food item to the menu of a specified restaurant.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.
    - name (str): The name of the food item.
    - price (float): The price of the food item.

    Returns:
    - bool: True if the food item was added successfully, False otherwise.
    """
    restaurant = find_by_id(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] != name:
                restaurant[MENU_KEY].append({
                    NAME_KEY: name,
                    PRICE_KEY: price
                })
                return True
        return False
    return None


def find_by_id(restaurant_id: str):
    """
    Finds a restaurant by its unique ID.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - dict: The restaurant details if found, None otherwise.
    """
    return restaurants.get(restaurant_id)


def get_restaurant_menu(restaurant_id: str):
    """
    Retrieves the menu of a specified restaurant.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - list: The menu of the restaurant if found, None otherwise.
    """
    restaurant = restaurants.get(restaurant_id).get(MENU_KEY)
    print(restaurant)
    if restaurant:
        return restaurant.get(MENU_KEY)
    return None


def update_food_item_details(restaurant_id: str, name: str, price: float):
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
    restaurant = find_by_id(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                item[PRICE_KEY] = price
                return True
        return False
    return None


def delete_food_item_details(restaurant_id: str, name: str):
    """
    Deletes a specific food item from a restaurant's menu.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.
    - name (str): The name of the food item to delete.

    Returns:
    - None: If the restaurant or food item was not found.
    """
    restaurant = find_by_id(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                restaurant[MENU_KEY].remove(item)
                return True
        return False
    return None


