from service.restaurant_service import (
    add_new_restaurant, add_new_food_item,
    get_restaurant_menu, update_food_item_details, delete_food_item_details
)


def add_restaurant(name: str, email: str,
                   contact_numbers: list[str], location: str):
    return add_new_restaurant(
        name.lower(), email.lower(), contact_numbers, location.lower()
    )


def add_food_item(restaurant_id: str,
                  name: str, price: float):
    return add_new_food_item(
        restaurant_id, name.lower(), price
    )


def get_menu(restaurant_id: str):
    return get_restaurant_menu(restaurant_id)


def update_food_item(restaurant_id: str, name: str, price: float):
    return update_food_item_details(restaurant_id, name.lower(), price)


def delete_food_item(restaurant_id: str, name: str):
    return delete_food_item_details(restaurant_id, name.lower())

