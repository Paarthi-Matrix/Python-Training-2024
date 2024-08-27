from service.RestaurantService import RestaurantService


class RestaurantController:
    def __init__(self):
        self.service = RestaurantService()

    def add_new_restaurant(self, name: str, email: str,
                           contact_number: str, location: str):
        return self.service.add_new_restaurant(
            name, email, contact_number, location
        )

    def add_food_item_to_restaurant(self, restaurant_id: str,
                                    name: str, price: float):
        return self.service.add_food_item_to_restaurant(
            restaurant_id, name, price
        )
