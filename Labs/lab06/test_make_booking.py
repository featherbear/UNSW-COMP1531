"""
Everything wrong

- the ID Generator is static, and keeps incrementing 0-23, 24-47, 48-71
- Small Car wouldn't have an ID of 5

datetime or string!?!?!

"""

from location import Location
from datetime import datetime
from errors import BookingError
from car import SmallCar, MediumCar, LargeCar, PremiumCar
from customer import Customer
from car_rental_system import CarRentalSystem

import pytest

class IdGenerator():
    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id



@pytest.fixture
def rental_fixture():

    rego_generator = IdGenerator()
    licence_generator = IdGenerator()

    system = CarRentalSystem()
    for name in ["Mazda", "Holden", "Ford"]:
        for model in ["Falcon", "Commodore"]:
            system.add_car(SmallCar(name, model, rego_generator.next()))
            system.add_car(MediumCar(name, model, rego_generator.next()))
            system.add_car(LargeCar(name, model, rego_generator.next()))

    for name in ["Tesla", "Audi"]:
        for model in ["model x", "A4", "S class"]:
            system.add_car(PremiumCar(name, model, rego_generator.next()))

    print(system.cars)
    for name in ["Matt", "Isaac", "Taylor"]:
        system.add_customer(Customer(name, licence_generator.next()))
    
    return system
    
def test_successful_make_small_car_booking(rental_fixture):
    print("test_successful_make_small_car_booking")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(1)  
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 250

def test_successful_make_small_car_booking_no_discount(rental_fixture):
    print("test_successful_make_small_car_booking_no_discount")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(1)  
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-8'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 400


def test_successful_make_medium_car_booking(rental_fixture):
    print("test_successful_make_medium_car_booking")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(2)  
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 375

def test_successful_make_medium_car_booking_no_discount(rental_fixture):
    print("test_successful_make_medium_car_booking_no_discount")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(2)  
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-8'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 600

    
def test_successful_make_large_car_booking(rental_fixture):
    print("test_successful_make_large_car_booking")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(3)  
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 500

    
def test_successful_make_large_car_booking_discount(rental_fixture):
    print("test_successful_make_large_car_booking_discount")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(3)  
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-8'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 760

def test_successful_make_premium_car_booking(rental_fixture):
    print("test_successful_make_large_car_booking")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(24)
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert int(booking[0].fee) == 862

def test_successful_make_premium_car_booking_discount(rental_fixture):
    print("test_successful_make_large_car_booking_discount")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(24)
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-8'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert int(booking[0].fee) == 1380


def test_unsuccessful_end_date_before_start_date(rental_fixture):
    print("test_unsuccessful_end_date_before_start_date")
    
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = f'2018-12-6'
    end_date        = f'2018-12-5'

    with pytest.raises(BookingError):
      booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)

def test_unsuccessful_empty_start_date(rental_fixture):
    print("test_unsuccessful_empty_start_date")
    
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = None
    end_date        = f'2018-12-5'

    with pytest.raises(BookingError):
      booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)

def test_unsuccessful_empty_end_date(rental_fixture):
    print("test_unsuccessful_empty_end_date")
    
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = f'2018-12-5'
    end_date        = None

    with pytest.raises(BookingError):
      booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)

def test_unsuccessful_empty_start_location(rental_fixture):
    print("test_unsuccessful_empty_start_location")
    
    start_location  = None
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = f'2018-12-5'
    end_date        = f'2018-12-10'

    with pytest.raises(BookingError):
      booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)

def test_unsuccessful_empty_end_location(rental_fixture):
    print("test_unsuccessful_empty_end_location")
    
    start_location  = 'Melbourne'
    end_location    = None

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = f'2018-12-5'
    end_date        = f'2018-12-10'

    with pytest.raises(BookingError):
      booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
