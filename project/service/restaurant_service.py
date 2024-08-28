import uuid

from common.restaurant_constants import (
    NAME_KEY, EMAIL_KEY, CONTACT_KEY,
    LOCATION_KEY, MENU_KEY, PRICE_KEY
)

restaurants = {}


def add_new_restaurant(name: str, email: str,
                       contact_numbers: list[str], location: str):
    id = str(uuid.uuid4())
    restaurants[id] = {
        NAME_KEY: name,
        EMAIL_KEY: email,
        CONTACT_KEY: contact_numbers,
        LOCATION_KEY: location,
        MENU_KEY: []
    }
    restaurant = find_by_id(id)
    print(restaurant)
    return id


def add_new_food_item(restaurant_id: str,
                      name: str, price: float):
    restaurant = find_by_id(restaurant_id)
    if restaurant:
        restaurant[MENU_KEY].append({
            NAME_KEY: name,
            PRICE_KEY: price
        })
        return True
    return False


def find_by_id(restaurant_id: str):
    return restaurants.get(restaurant_id)


def get_restaurant_menu(restaurant_id: str):
    restaurant = restaurants.get(restaurant_id)
    return restaurant.get(MENU_KEY)


def update_food_item_details(restaurant_id: str, name: str, price: float):
    restaurant = find_by_id(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                item[PRICE_KEY] = price
                return True
        return False
    return None


def delete_food_item_details(restaurant_id: str, name: str):
    restaurant = find_by_id(restaurant_id)
    if restaurant:
        for item in restaurant[MENU_KEY]:
            if item[NAME_KEY] == name:
                restaurant[MENU_KEY].remove(item)
                return restaurant[MENU_KEY]
    return None