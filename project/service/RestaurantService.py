from model.Restaurant import Restaurant


class RestaurantService:
    def __init__(self):
        self.restaurants = []

    def add_new_restaurant(self, name: str, email: str,
                           contact_number: str, location: str):
        restaurant = Restaurant(name, email, contact_number, location)
        self.restaurants.append(restaurant)
        return restaurant
