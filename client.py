from customer import Customer
from car import SmallCar, MediumCar, LargeCar, PremiumCar
from car_rental_system import CarRentalSystem
from location import Location

# Populate the system
CRS = CarRentalSystem()

# Add customers
CRS.add_customer(Customer("Matt",   18, 1, "matt@email.com"))
CRS.add_customer(Customer("Isaac",  31, 2, "eyezac@fmail.com"))
CRS.add_customer(Customer("Taylor", 27, 3, "taelore@gmail.com"))

# Add cars
CRS.add_car(SmallCar("Mazda", "Falcon", 2019, 1))
CRS.add_car(MediumCar("Mazda", "Falcon", 2019, 2))
CRS.add_car(LargeCar("Mazda", "Falcon", 2019, 3))
CRS.add_car(SmallCar("Mazda", "Commodore", 2019, 4))
CRS.add_car(MediumCar("Mazda", "Commodore", 2019, 5))
CRS.add_car(LargeCar("Mazda", "Commodore", 2019, 6))
CRS.add_car(SmallCar("Holden", "Falcon", 2019, 7))
CRS.add_car(MediumCar("Holden", "Falcon", 2019, 8))
CRS.add_car(LargeCar("Holden", "Falcon", 2019, 9))
CRS.add_car(SmallCar("Holden", "Commodore", 2019, 10))
CRS.add_car(MediumCar("Holden", "Commodore", 2019, 11))
CRS.add_car(LargeCar("Holden", "Commodore", 2019, 12))
CRS.add_car(SmallCar("Ford", "Falcon", 2019, 13))
CRS.add_car(MediumCar("Ford", "Falcon", 2019, 14))
CRS.add_car(LargeCar("Ford", "Falcon", 2019, 15))
CRS.add_car(SmallCar("Ford", "Commodore", 2019, 16))
CRS.add_car(MediumCar("Ford", "Commodore", 2019, 17))
CRS.add_car(LargeCar("Ford", "Commodore", 2019, 18))
CRS.add_car(PremiumCar("Tesla", "model x", 2019, 19))
CRS.add_car(PremiumCar("Tesla", "A4", 2019, 20))
CRS.add_car(PremiumCar("Tesla", "S class", 2019, 21))
CRS.add_car(PremiumCar("Audi", "model x", 2019, 22))
CRS.add_car(PremiumCar("Audi", "A4", 2019, 23))
CRS.add_car(PremiumCar("Audi", "S class", 2019, 24))

#
print("\n\n~~~ Print all customers ~~~")
for customer in CRS.customers:
  print(customer)

print("\n\n~~~ Print all cars ~~~")
for car in CRS.cars:
  print(car)

print("\n\n~~~ Make first booking ~~~")
customer = CRS.get_customer(3)
car = CRS.get_car(5)
CRS.make_booking(customer, car, 7, Location("Sydney", "Canberra"))

print("\n\n~~~ Make second booking ~~~")
customer = CRS.get_customer(2)
car = CRS.get_car(21)
CRS.make_booking(customer, car, 12, Location("Earth", "Moon"))

print("\n\n~~~ Print all bookings ~~~")
for booking in CRS.bookings:
  print(booking)

######################################################
# Do our own tests
######################################################

print("\n\n> Try to find non-existent customer with unknown licence")
lic = 3333
print(f"Looking for customer with licence {lic}")
customer = CRS.get_customer(lic)
print(f"Returned: {customer} (Expected: {None})")
print(f"Test: {customer is None}")

print("\n\n> Try to find non-existent car with unknown rego")
reg = 4444
print(f"Looking for car with registration number {reg}")
car = CRS.get_car(reg)
print(f"Returned: {car} (Expected: {None})")
print(f"Test: {car is None}")

# Verify that the prices are caculated correctly

# Small Car
# No discount for small cars rented past a week
print("\n\n> Calculate price for a small car rental")
car = SmallCar("/make/", "/model/", "/year/", "/rego/")
rate = car.rate
assert(car.calculatePrice(1) == 1 * rate)
assert(car.calculatePrice(2) == 2 * rate)
assert(car.calculatePrice(3) == 3 * rate)
assert(car.calculatePrice(4) == 4 * rate)
assert(car.calculatePrice(5) == 5 * rate)
assert(car.calculatePrice(6) == 6 * rate)
assert(car.calculatePrice(7) == 7 * rate)
assert(car.calculatePrice(8) == 8 * rate)

# Medium Car
# No discount for medium cars rented past a week
print("\n\n> Calculate price for a medium car rental")
car = MediumCar("/make/", "/model/", "/year/", "/rego/")
rate = car.rate
assert(car.calculatePrice(1) == 1 * rate)
assert(car.calculatePrice(2) == 2 * rate)
assert(car.calculatePrice(3) == 3 * rate)
assert(car.calculatePrice(4) == 4 * rate)
assert(car.calculatePrice(5) == 5 * rate)
assert(car.calculatePrice(6) == 6 * rate)
assert(car.calculatePrice(7) == 7 * rate)
assert(car.calculatePrice(8) == 8 * rate)

# Large Car
# 5% discount for large cars rented past a week
print("\n\n> Calculate price for a large car rental")
car = LargeCar("/make/", "/model/", "/year/", "/rego/")
rate = car.rate
assert(car.calculatePrice(1) == 1 * rate)
assert(car.calculatePrice(2) == 2 * rate)
assert(car.calculatePrice(3) == 3 * rate)
assert(car.calculatePrice(4) == 4 * rate)
assert(car.calculatePrice(5) == 5 * rate)
assert(car.calculatePrice(6) == 6 * rate)
assert(car.calculatePrice(7) == 7 * rate)
print("    Test for 5% discount for rentals past a week")
assert(car.calculatePrice(8) == 8 * rate * 0.95)

# Premium Car
# 15% tariff charged on premium cars
# 5% discount for premium cars rented past a week
print("\n\n> Calculate price for a premium car rental")
car = PremiumCar("/make/", "/model/", "/year/", "/rego/")
rate = car.rate
print("    Test for 15% tariff all premium car rentals")
assert(car.calculatePrice(1) == 1 * rate * 1.15)
assert(car.calculatePrice(2) == 2 * rate * 1.15)
assert(car.calculatePrice(3) == 3 * rate * 1.15)
assert(car.calculatePrice(4) == 4 * rate * 1.15)
assert(car.calculatePrice(5) == 5 * rate * 1.15)
assert(car.calculatePrice(6) == 6 * rate * 1.15)
assert(car.calculatePrice(7) == 7 * rate * 1.15)
print("    Test for 5% discount for rentals past a week")
assert(car.calculatePrice(8) == 8 * rate * 1.15 * 0.95)