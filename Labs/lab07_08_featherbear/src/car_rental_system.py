from src.booking import Booking
from src.location import Location
from src.customer import Customer

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []

    '''
    Query Processing
    '''
    def search_car(self, name=None, model=None):

        # Return all cars if no keyword given
        if not name and not model:
            return self.cars

        # Convert search keywords into lowercases (if provided)
        name  = name.lower()    if name else None
        model = model.lower()   if model else None

        # Collect all matching cars into a list
        cars = []
        for car in self.cars:
            if name and (name in car.name.lower()):
                cars.append(car)

            elif model and (model in car.model.lower()):
                cars.append(car)

        return cars


    def get_car(self, rego):
        for c in self.cars:
            if c.rego == rego:
                return c
        return None


    def get_bookings_by_car_rego(self, rego):
        bookings = []

        for booking in self.bookings:
            if booking.car_rego == rego:
                bookings.append(booking)

        return bookings
    

    '''
    Booking
    '''
    def make_booking(self, customer, car, date1, date2, location1, location2):
        self._customers.append(customer)

        period   = (date2 - date1).days + 1
        location = Location(location1, location2)
        
        booking  = Booking(customer, period, car, location)
        self._bookings.append(booking)
        return booking

    def check_fee(self, car, date1, date2):
        period = (date2 - date1).days + 1 
        return car.get_fee(period)


    '''
    Registration
    '''
    def add_car(self, car):
        self._cars.append(car)
        
    
    '''
    Properties
    '''
    @property
    def cars(self):
        return self._cars


    @property
    def bookings(self):
        return self._bookings