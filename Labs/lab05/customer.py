from _user import User

class Customer(User):
  def __init__(self, name, age, licence, email):
    super().__init__(name)
    self._name = name
    self._age = age
    self._licence = licence
    self._email = email
  
  @property
  def name(self):
    return self._name
     
  @property
  def age(self):
    return self._age
 
  @property
  def licence(self):
    return self._licence
  
  @property
  def email(self):
    return self._email
  
  def __str__(self):
    return f"Customer <name: {self._name}, licence: {self._licence}>"