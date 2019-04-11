from abc import ABC


class Car(ABC):

    def __init__(self, name, model, rego, rate):
        self._name       = name
        self._model      = model
        self._rego       = rego
        self._daily_rate = rate

    def get_fee(self, period):
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

    def __str__(self):
        return f'Car <{self.name}, {self.model}>'



class SmallCar(Car):

    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 50)

    def __str__(self):
        return f'Small Car <{self.name}, {self.model}>'



class MediumCar(Car):
    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 75)

    def __str__(self):
        return f'Medium Car <{self.name}, {self.model}>'



class LargeCar(Car):
    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 100)

    def get_fee(self, period):

        fee = super().get_fee(period)
        if period >= 7:
            fee = fee * 0.95
        return fee

    def __str__(self):
        return f'Large Car <{self.name}, {self.model}>'



class PremiumCar(Car):

    def __init__(self, name, model, rego):
        super().__init__(name, model, rego, 150)
        self._premium_tariff = 0.15

    def get_fee(self, period):
        return super().get_fee(period) * (1 + self._premium_tariff)

    def __str__(self):
        return f'Premium Car <{self.name}, {self.model}>'
