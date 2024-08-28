import uuid


class Customer:
    def __init__(self, name:str, email:str,
                 mobile_number:str, location:str):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.location = location
        self.orders = []

    def __str__(self):
        return (f"Id: {self.id}, Name: {self.name}, Email: {self.email}, "
                f"Mobile_Number: {self.mobile_number}, "
                f"Location: {self.location}")


