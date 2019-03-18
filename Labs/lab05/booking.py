class Booking: # Car Rental
  def __init__(self, customer, car, period, location):
    # Ignore insurance
    self._customer = customer
    self._car = car
    self._period = period
    
    self._location = location
    
    self._price = car.calculatePrice(period)
    
  @property
  def customer(self):
    return self._customer
  
  @property
  def car(self):
    return self._car
  
  @property
  def period(self):
    return self._period

  @property
  def price(self):
    return self._price
  
  @property
  def location(self):
    return self._location

  def __str__(self):
    return f"Made by {self._customer}\nReserve {self._car} for {self._period} days\nLocations: {self._location}\nTotal fee: ${self._price:.2f}"