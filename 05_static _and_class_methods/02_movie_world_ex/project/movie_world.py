from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{str(customer)}\n"
        for dvd in self.dvds:
            result += f"{str(dvd)}"
        return result.strip()


