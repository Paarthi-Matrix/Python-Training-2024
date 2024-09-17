import uuid

from constant.constant import (
    PASSWORD_KEY, NAME_KEY, EMAIL_KEY, CONTACT_KEY,
    LOCATION_KEY, MENU_KEY, PRICE_KEY, IS_DELETE
)

restaurants = {}


def add(name: str, password: str, email: str,
                       contact_numbers: list[str], location: str):
    """
    Adds a new restaurant to the restaurants dictionary with a unique ID.

    Parameters:
    - name (str): The name of the restaurant.
    - password (str): The password for the restaurant's account.
    - email (str): The email address of the restaurant.
    - contact_numbers (list[str]): A list of contact numbers for the restaurant.
    - location (str): The physical location of the restaurant.

    Returns:
    - str: The unique ID of the newly added restaurant.
    """
    unique_id = str(uuid.uuid4())
    restaurants[unique_id] = {
        NAME_KEY: name,
        PASSWORD_KEY: password,
        EMAIL_KEY: email,
        CONTACT_KEY: contact_numbers,
        LOCATION_KEY: location,
        MENU_KEY: [],
        IS_DELETE: False
    }
    return unique_id


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
    restaurant = get(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                return False
        restaurant[MENU_KEY].append({
            NAME_KEY: name,
            PRICE_KEY: price,
            IS_DELETE: False
        })
        return True
    return None


def get(restaurant_id: str):
    """
    Finds a restaurant by its unique ID.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - dict: The restaurant's details if found and not deleted, None otherwise.
    """
    restaurant = restaurants.get(restaurant_id)
    if restaurant:
        if not restaurant[IS_DELETE]:
            return restaurant
    return None


def filter_restaurant_info(restaurant):
    """
    Filters out sensitive and unnecessary information from a restaurant's details.

    Parameters:
    - restaurant (dict): The full details of the restaurant.

    Returns:
    - dict: The filtered restaurant details without sensitive information.
    """
    return {key: value for key, value in restaurant.items() if key not in [PASSWORD_KEY, MENU_KEY, IS_DELETE]}


def get_all():
    """
    Retrieves all restaurants that are not marked as deleted.

    Returns:
    - dict: A dictionary of all active restaurants with filtered information.
    """
    filtered_restaurants = {
        restaurant_id: filter_restaurant_info(restaurant)
        for restaurant_id, restaurant in restaurants.items()
        if not restaurant.get(IS_DELETE, False)
    }
    return filtered_restaurants


def get_menu(restaurant_id: str):
    """
    Retrieves the menu of a specified restaurant.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - list: The menu of the restaurant with non-deleted items, None if the restaurant is not found.
    """
    restaurant = restaurants.get(restaurant_id)
    if restaurant:
        return [{key: value for key, value in food_item.items() if key != IS_DELETE} for food_item in
                restaurant.get(MENU_KEY, []) if not food_item.get(IS_DELETE, False)]
    return None


def update(restaurant, to_update: str, detail_to_update: str):
    """
    Updates a specific detail of a restaurant.

    Parameters:
    - restaurant (dict): The restaurant's details.
    - to_update (str): The key of the detail to update.
    - detail_to_update (str): The new value for the specified detail.

    Returns:
    - bool: True if the update was successful.
    """
    restaurant[to_update] = detail_to_update
    return True


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
    restaurant = get(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                item[PRICE_KEY] = price
                return True
        return False
    return None


def delete_food_item_details(restaurant_id: str, name: str):
    """
    Marks a specific food item as deleted in a restaurant's menu.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.
    - name (str): The name of the food item to delete.

    Returns:
    - bool: True if the food item was marked as deleted successfully, False if the item was not found.
    - None: If the restaurant was not found.
    """
    restaurant = get(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                item[IS_DELETE] = True
                return True
        return False
    return None


def remove(restaurant_id: str):
    """
    Marks a restaurant as deleted.

    Parameters:
    - restaurant_id (str): The unique ID of the restaurant.

    Returns:
    - None
    """
    restaurant = get(restaurant_id)
    if restaurant:
        restaurant[IS_DELETE] = True
    return None
