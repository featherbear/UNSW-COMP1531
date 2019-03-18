class User:
  def __init__(self, name):
    self._name = name
    self._username = None
    self._password = None
    
  @property
  def username(self):
    return self._username

  @property
  def password(self):
    return self._password
    