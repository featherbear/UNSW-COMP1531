class Customer():

    def __init__(self, name, licence):
        self._name    = name
        self._licence = licence

    @property
    def name(self):
        return self._name

    @property
    def licence(self):
        return self._licence

    def __str__(self):
        return f'Customer <name: {self._name}, licence: {self._licence}>'
