from abc import ABC, abstractmethod

class Car(ABC):
  @abstractmethod
  def __init__(self, type, make, model, year, rego):
    self._type = type
    self._make = make
    self._model = model
    self._year = year
    self._rego = rego
    self._rate = 0

  @property
  def type(self):
    return self._type

  @property
  def make(self):
     return self._make

  @property
  def model(self):
    return self._model
   
  @property
  def year(self):
    return self._year
   
  @property
  def rego(self):
    return self._rego

  @property
  def rate(self):
    return self._rate
  
  def calculatePrice(self, period):
    return self._rate * period

  def __str__(self):
    return f"{self._type} Car <{self._make}, {self._model}, rego: {self._rego}>"

class SmallCar(Car):
  def __init__(self, *args):    
    super().__init__("Small", *args)
    self._rate = 50
    
class MediumCar(Car):
  def __init__(self, *args):    
    super().__init__("Medium", *args)
    self._rate = 75

class LargeCar(Car):
  def __init__(self, *args):    
    super().__init__("Large", *args)
    self._rate = 100

  def calculatePrice(self, period):
    return super().calculatePrice(period) * (0.95 if period > 7 else 1)

class PremiumCar(Car):
  def __init__(self, *args):    
    super().__init__("Premium", *args)
    self._rate = 157.8947368421053

  def calculatePrice(self, period):
    tariff = 0.15 # decimal
    price = super().calculatePrice(period) * (1 + tariff)
    return price * (0.95 if period > 7 else 1)
