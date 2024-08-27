from model.FoodItem import FoodItem
from model.Restaurant import Restaurant


class RestaurantService:
    def __init__(self):
        self.restaurants = []

    def add_new_restaurant(self, name: str, email: str,
                           contact_number: str, location: str):
        restaurant = Restaurant(name, email, contact_number, location)
        self.restaurants.append(restaurant)
        return restaurant

    def add_food_item_to_restaurant(self, restaurant_id: str,
                                    name: str, price: float):
        food_item = FoodItem(name, price)
        restaurant = self.find_restaurant_by_id(restaurant_id)
        if restaurant:
            restaurant.menu.append(food_item)
        return restaurant

    def find_restaurant_by_id(self, restaurant_id):
        for restaurant in self.restaurants:
            if restaurant.id == restaurant_id:
                return restaurant
        return None
