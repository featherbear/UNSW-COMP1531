from booking import Booking

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []

    def make_booking(self, customer, car, period, location):
        booking = Booking(customer, car, period, location)
        self._bookings.append(booking)
        
        print("=== Booking Successful! ===")
        print(booking)
        print("=== Thank you for using Affordable Rentals ===")

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, rego):
        for car in self._cars:
            if car.rego is rego:
                return car
        return None

    def add_car(self, car):
        self._cars.append(car)

    def add_customer(self, customer):
        self._customers.append(customer)


    '''
    Properties
    '''
    @property
    def cars(self):
        return self._cars

    @property
    def customers(self):
        return self._customers

    @property
    def bookings(self):
        return self._bookings