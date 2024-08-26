from service.RestaurantService import RestaurantService


class RestaurantController:
    def __init__(self):
        self.service = RestaurantService()

    def add_new_restaurant(self, name: str, email: str,
                           contact_number: str, location: str):
        return self.service.add_new_restaurant(name, email,
                                               contact_number, location)
