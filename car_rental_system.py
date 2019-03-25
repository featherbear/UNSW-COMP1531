from booking import Booking
from location import Location
from errors import BookingError, check_booking_error
from datetime import datetime

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []

    '''
    Query Processing Services
    '''
    def car_search(self, name=None, model=None):

        # Return all cars if no keyword given
        if not name and not model:
            return self._cars

        # Convert search keywords into lowercases (if provided)
        name  = name.lower()    if name else None
        model = model.lower()   if model else None

        # Collect all matching cars into a list
        cars = []
        for car in self._cars:
            c_name  = car.name.lower()
            c_model = car.model.lower()

            if name and name in c_name:
                cars.append(car)

            elif model and model in c_model:
                cars.append(car)

        return cars

    def make_booking(self, customer, car, start_date,end_date, start_location,end_location):
        try:
            errors = check_booking_error(start_date, end_date, start_location, end_location)
            if errors:
                raise BookingError(errors)
            period   = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1
            location = Location(start_location, end_location)
            booking = Booking(customer, car, period, location)  
            print("fee:",booking.fee)
        except BookingError as be:
            return None, be.errors
        self._bookings.append(booking)
        booking.apply()
        print('=== Booking Successful! ===')
        print('Booking details:')
        print(booking)
        print('=== Thank you for using Affordable Rentals ===')
        return booking, {}

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    # def check_fee(self, customer, car, date1, date2, location1, location2):
    #     try:
    #         booking = self._create_booking_item(customer, car, date1, date2, location1, location2)
    #     except BookingError as be:
    #         return None, be.errors
    
    #     return booking.booking_fee, {}

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

