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
        '''
        Task 1
        '''
        cars = self._cars

        if not (name or model):
          return cars

        if name:
          cars = filter(lambda car: car.name == name, cars)
        
        if model:
          cars = filter(lambda car: car.model == model, cars)

        return list(cars)
        
    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, rego):
        '''
        Task 2
        '''
        try:
          return next(filter(lambda car: car.rego == rego, self._cars))
        except StopIteration:
          return None
          
    '''
    Booking Services
    '''

    def make_booking(self, customer, car, start_date, end_date, start_location, end_location):
        '''
        Task 3
        '''
        try:
          start_date = datetime.strptime(start_date, "%Y-%m-%d")
        except:
          raise BookingError({'start_date': 'Invalid start date'})
        
        try:
          end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except:
          raise BookingError({'end_date': 'Invalid end date'})
          
        errors = check_booking_error(start_date, end_date, start_location, end_location)
        if errors:
          raise BookingError(errors)

        period = (end_date - start_date).days + 1
        booking = Booking(customer, car, period, Location(start_location, end_location))
        car.add_booking(booking)
        self._bookings.append(booking)
        return [booking]

    def check_fee(self, customer, car, date1, date2, location1, location2):
        '''
        Task 4
        '''
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
       
        try:
          check_booking_error(start_date, end_date, start_location, end_location)
        except BookingError as err:
          print(err)
          return

        period = end_date - start_date
        booking = Booking(customer, car, period.days, Location(start_location, end_location))
        
        return booking.fee

    ''' 
        Registration Services
    '''
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

