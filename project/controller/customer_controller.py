from service.customer_service import CustomerService


class CustomerController:
    def __init__(self):
        self.service = CustomerService()

    def add_new_customer(self, name: str, email: str,
                         mobile_number: str, location: str):
        return self.service.add_new_customer(name, email,
                                             mobile_number, location)