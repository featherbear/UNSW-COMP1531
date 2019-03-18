import pytest

from car import SmallCar, MediumCar, LargeCar, PremiumCar

class TestSmallCar():
  def _createCar(self):
    self.car = SmallCar(1, 2, 3, 4)
  
  def test_create(self):
    self._createCar()
    assert(self.car.type == "Small")
    assert(self.car.make == 1)
    assert(self.car.model == 2)
    assert(self.car.year == 3)
    assert(self.car.rego == 4)
  
  def test_rate(self):
    self._createCar()
    rate = self.car.rate 
    assert(self.car.calculatePrice(1) == 1 * rate)
    assert(self.car.calculatePrice(2) == 2 * rate)
    assert(self.car.calculatePrice(3) == 3 * rate)
    assert(self.car.calculatePrice(4) == 4 * rate)
    assert(self.car.calculatePrice(5) == 5 * rate)
    assert(self.car.calculatePrice(6) == 6 * rate)
    assert(self.car.calculatePrice(7) == 7 * rate)
    
    # No discount for small cars rented past a week
    assert(self.car.calculatePrice(8) == 8 * rate)

class TestMediumCar():  
  def _createCar(self):
    self.car = MediumCar(1, 2, 3, 4)
  
  def test_create(self):
    self._createCar()
    assert(self.car.type == "Medium")
    assert(self.car.make == 1)
    assert(self.car.model == 2)
    assert(self.car.year == 3)
    assert(self.car.rego == 4)
  
  def test_rate(self):
    self._createCar()
    rate = self.car.rate 
    assert(self.car.calculatePrice(1) == 1 * rate)
    assert(self.car.calculatePrice(2) == 2 * rate)
    assert(self.car.calculatePrice(3) == 3 * rate)
    assert(self.car.calculatePrice(4) == 4 * rate)
    assert(self.car.calculatePrice(5) == 5 * rate)
    assert(self.car.calculatePrice(6) == 6 * rate)
    assert(self.car.calculatePrice(7) == 7 * rate)
    
    # No discount for small cars rented past a week
    assert(self.car.calculatePrice(8) == 8 * rate)

class TestLargeCar():  
  def _createCar(self):
    self.car = LargeCar(1, 2, 3, 4)
  
  def test_create(self):
    self._createCar()
    assert(self.car.type == "Large")
    assert(self.car.make == 1)
    assert(self.car.model == 2)
    assert(self.car.year == 3)
    assert(self.car.rego == 4)
  
  def test_rate(self):
    self._createCar()
    rate = self.car.rate 
    assert(self.car.calculatePrice(1) == 1 * rate)
    assert(self.car.calculatePrice(2) == 2 * rate)
    assert(self.car.calculatePrice(3) == 3 * rate)
    assert(self.car.calculatePrice(4) == 4 * rate)
    assert(self.car.calculatePrice(5) == 5 * rate)
    assert(self.car.calculatePrice(6) == 6 * rate)
    assert(self.car.calculatePrice(7) == 7 * rate)
    
    # 5% discount for large cars rented past a week
    assert(self.car.calculatePrice(8) == 8 * rate * 0.95)

class TestPremiumCar():  
  def _createCar(self):
    self.car = PremiumCar(1, 2, 3, 4)
  
  def test_create(self):
    self._createCar()
    assert(self.car.type == "Premium")
    assert(self.car.make == 1)
    assert(self.car.model == 2)
    assert(self.car.year == 3)
    assert(self.car.rego == 4)
  
  def test_rate(self):
    self._createCar()
    rate = self.car.rate 
    assert(self.car.calculatePrice(1) == 1 * rate * 1.15)
    assert(self.car.calculatePrice(2) == 2 * rate * 1.15)
    assert(self.car.calculatePrice(3) == 3 * rate * 1.15)
    assert(self.car.calculatePrice(4) == 4 * rate * 1.15)
    assert(self.car.calculatePrice(5) == 5 * rate * 1.15)
    assert(self.car.calculatePrice(6) == 6 * rate * 1.15)
    assert(self.car.calculatePrice(7) == 7 * rate * 1.15)
    
    # 15% tariff charged on premium cars
    # 5% discount for large cars rented past a week
    assert(self.car.calculatePrice(8) == 8 * rate * 1.15 * 0.95)