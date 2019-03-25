from car import SmallCar, MediumCar, LargeCar, PremiumCar
from car_rental_system import CarRentalSystem
from customer import Customer
from location import Location

system = CarRentalSystem()

class IdGenerator():

    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

rego_generator = IdGenerator()
licence_generator = IdGenerator()

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


print('~~~ Print all customers ~~~')
print('\n'.join(str(c) for c in system.customers))

print('\n~~~ Print all cars ~~~')
print('\n'.join(str(c) for c in system.cars))


print('\n\n~~~ Make first booking ~~~')
user = system.get_customer(3)
car  = system.get_car(5)

year1 = 2018
month1 = 12
day1 = 1

year2 = 2018
month2 = 12
day2 = 5

start_date      = f'{year1}-{month1}-{day1}'
end_date        = f'{year2}-{month2}-{day2}'

booking = system.make_booking(user, car, start_date, end_date,'Sydney', 'Canberra')
print("fee: ", booking[0].fee)

print('\n\n~~~ Make second booking ~~~')
user = system.get_customer(2)
car  = system.get_car(21)

system.make_booking(user, car, start_date, end_date, 'Earth', 'Moon')

print('\n\n~~~ Print all bookings ~~~\n')
print('\n\n'.join(str(b) for b in system.bookings))