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

rego_generator = IdGenerator()
licence_generator = IdGenerator()

@pytest.fixture
def rental_fixture():
    system = CarRentalSystem()
    for name in ["Mazda", "Holden", "Ford"]:
        for model in ["Falcon", "Commodore"]:
            system.add_car(SmallCar(name, model, rego_generator.next()))
            system.add_car(MediumCar(name, model, rego_generator.next()))
            system.add_car(LargeCar(name, model, rego_generator.next()))

    for name in ["Tesla", "Audi"]:
        for model in ["model x", "A4", "S class"]:
            system.add_car(PremiumCar(name, model, rego_generator.next()))

    for name in ["Matt", "Isaac", "Taylor"]:
        system.add_customer(Customer(name, licence_generator.next()))
    
    return system
    
def test_successful_make_small_car_booking(rental_fixture):
    print("test_successful_make_small_car_booking")
    start_location  = 'Sydney'
    end_location    = 'Melbourne'

    user = rental_fixture.get_customer(3)
    car  = rental_fixture.get_car(5) 
    
    start_date      = f'2018-12-1'
    end_date        = f'2018-12-5'

    booking = rental_fixture.make_booking(user, car, start_date, end_date,start_location, end_location)
    assert len(rental_fixture ._bookings) == 1
    assert rental_fixture._bookings[0].location.pickup == start_location
    assert rental_fixture._bookings[0].location.dropoff == end_location
    assert booking[0].fee == 375
