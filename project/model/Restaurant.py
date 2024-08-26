import uuid


class Restaurant:
    def __init__(self, name: str, email: str,
                 contact_number: str, location: str):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.contact_number = contact_number
        self.location = location
        self.food_items = []


    def __str__(self):
        return (f"Id: {self.id}, Name: {self.name}, Email: {self.email},"
                f" Contact Number: {self.contact_number},"
                f" Location: {self.location}")
