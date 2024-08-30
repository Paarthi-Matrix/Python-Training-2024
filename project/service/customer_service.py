from model.customer import Customer


class CustomerService:
    def __init__(self):
        self.customers = []

    def add_new_customer(self, name: str, email: str,
                         mobile_number: str, location: str):
        customer = Customer(name, email, mobile_number, location)
        self.customers.append(customer)
        print([str(customer) for customer in self.customers])
        return customer