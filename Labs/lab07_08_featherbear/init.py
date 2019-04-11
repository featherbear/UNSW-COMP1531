from src.car import SmallCar, LargeCar, MediumCar, PremiumCar
from src.car_rental_system import CarRentalSystem
from src.customer import Customer


def bootstrap_system():

    system = CarRentalSystem()

    rego = 0
    for name in ["Mazda", "Holden", "Ford"]:
        for model in ["Falcon", "Commodore", "Buggy"]:
            system.add_car(SmallCar(name, model, str(rego)))
            rego += 1
            system.add_car(MediumCar(name, model, str(rego)))
            rego += 1
            system.add_car(LargeCar(name, model, str(rego)))
            rego += 1

    for name in ["Tesla", "Audi", "Mercedes"]:
        for model in ["model x", "A4", "S class"]:
            system.add_car(PremiumCar(name, model, str(rego)))
            rego += 1

    return system
