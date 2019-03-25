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
    
def test_successful_customer_search(rental_fixture):
    print("test_successful_customer_search")

    assert rental_fixture.get_customer(1) == rental_fixture.customers[0]
    assert rental_fixture.get_customer(2) == rental_fixture.customers[1]
    assert rental_fixture.get_customer(3) == rental_fixture.customers[2]

def test_unsuccessful_customer_search(rental_fixture):
    print("test_unsuccessful_customer_search")

    assert rental_fixture.get_customer(999) is None
    
def test_successful_car_search_name(rental_fixture):
    print("test_successful_car_search_name")

    results = rental_fixture.car_search(name="Mazda")
    assert len(results) == 6
    assert results[0] == rental_fixture.cars[0]
    assert results[1] == rental_fixture.cars[1]
    assert results[2] == rental_fixture.cars[2]
    assert results[3] == rental_fixture.cars[3]
    assert results[4] == rental_fixture.cars[4]
    assert results[5] == rental_fixture.cars[5]

def test_unsuccessful_car_search_name(rental_fixture):
    print("test_unsuccessful_car_search_name")
    
    result = rental_fixture.car_search(name="AAAAAAAAH!")
    assert result == [] and len(result) is 0


    
def test_successful_car_search_model(rental_fixture):
    print("test_successful_car_search_model")

    results = rental_fixture.car_search(model="Falcon")
    assert len(results) == 9

def test_unsuccessful_car_search_model(rental_fixture):
    print("test_unsuccessful_car_search_model")

    result = rental_fixture.car_search(model="AAAAAAAAH!")
    assert result == [] and len(result) is 0

def test_successful_car_search_rego(rental_fixture):
    print("test_successful_car_search_rego")

    result = rental_fixture.get_car(2)
    assert result == rental_fixture.cars[1]

def test_unsuccessful_car_search_rego(rental_fixture):
    print("test_unsuccessful_car_search_rego")

    result = rental_fixture.get_car(999)
    assert result is None


def test_successful_car_search_dual(rental_fixture):
    print("test_successful_car_search_dual")
    results = rental_fixture.car_search(name="Holden", model="Commodore")

    assert len(results) == 3
    assert results[0] == rental_fixture.cars[9]
    assert results[1] == rental_fixture.cars[10]
    assert results[2] == rental_fixture.cars[11]

def test_car_search_all(rental_fixture):
    print("test_car_search_all")

    results = rental_fixture.car_search()
    assert len(results) == len(rental_fixture.cars)
