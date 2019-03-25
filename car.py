from abc import ABC

class Car(ABC):

    def __init__(self, name, model, rego, rate):
        self._name  = name
        self._model = model
        self._rego  = rego
        self._daily_rate = rate
        self._bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def calc_fee(self, period):
        return period * self._daily_rate

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def rego(self):
        return self._rego

    @property
    def bookings(self):
        return self._bookings

    def __str__(self):
        return f'Car <{self.name}, {self.model}, rego: {self.rego}>'


class SmallCar(Car):

    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 50)

    def __str__(self):
        return 'Small ' + super().__str__()



class MediumCar(Car):
    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 75)

    def __str__(self):
        return 'Medium ' + super().__str__()



class LargeCar(Car):
    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 100)

    def calc_fee(self, period):

        fee = super().calc_fee(period)
        if period >= 7:
            fee = fee * 0.95
        return fee

    def __str__(self):
        return 'Large ' + super().__str__()


class PremiumCar(Car):

    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 150)
        self._premium_tariff = 0.15

    def calc_fee(self, period):
        return super().calc_fee(period) * (1 + self._premium_tariff)

    def __str__(self):
        return 'Premium ' + super().__str__()
