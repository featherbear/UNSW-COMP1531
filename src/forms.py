from abc import ABC, abstractmethod
from datetime import datetime

'''
ERRORS
'''
class ParseError(Exception):
    '''
    Raised when a form cannot be parsed correctly or fails validation
    '''
    pass



'''
FORMS
'''
class BookingForm():

    def __init__(self, form):
        # Fields of the form
        self._name    = Field('customer_name',      [InputRequired('Name cannot be empty')])
        self._licence = Field('customer_licence',   [InputRequired('Licence cannot be empty')])
        self._date1   = DateField('start_date',     [InputRequired('Start date must be provided')])
        self._date2   = DateField('end_date',       [InputRequired('End date must be provided')])
        self._loc1    = Field('start_location',     [InputRequired('Start location cannot be empty')])
        self._loc2    = Field('end_location',       [InputRequired('End location cannot be empty')])

        # Collect all of the above fields above
        self._fields = [attr for attr in self.__dict__.values() if isinstance(attr, Field)]

        # Errors not specific to a single field
        self._other_errors = {}
        self._parse(form)

    def _parse(self, form):
        '''
        Interprets form input from user and records any errors in the input
            - This may also perform operations such as converting a string into a date object
        '''

        for field in self._fields:
            field.parse(form.get(field.name, None))
        
        # Extra validation rules
        if self._date1.is_valid and self._date2.is_valid:
            if self._date1.data > self._date2.data:
                self._other_errors['period'] = 'End date cannot be before start date'


    def get_raw_data(self, field_name):
        '''
        returns the user's input for the specified field,
        but returns an empty string if the field does not exist
        '''
        field = self._field(field_name)
        if not field:
            return ''

        return field.raw_data or ''
 
    def get_error(self, field_name):
        '''
        returns the error for the specified field, returns an empty string
        if the field does not exist or if the field does not have any errors
        '''
        field = self._field(field_name)
        
        if not field:
            return self._other_errors.get(field_name) or ''
        return field.error or ''

    def has_error(self, field_name):
        return self.get_error(field_name) is not ''

    def _field(self, field_name):
        '''
        find and return the field object matching with the specified field name,
        if no matching field was found, then return None
        '''
        return next((field for field in self._fields if field.name == field_name), None)

    @property
    def is_valid(self):
        '''
        returns true if the form input has no errors, false otherwise
        '''
        if len(self._other_errors) > 0:
            return False

        return all(field.is_valid for field in self._fields)


    '''
    Form properties
        These properties should be accessed only when form.is_valid == True
    '''
    @property
    def customer_name(self):
        return self._name.data

    @property
    def customer_licence(self):
        return self._licence.data

    @property
    def start_date(self):
        return self._date1.data

    @property
    def end_date(self):
        return self._date2.data

    @property
    def start_location(self):
        return self._loc1.data

    @property
    def end_location(self):
        return self._loc2.data
    


'''
FIELDS
'''
class Field():
    def __init__(self, name, validators = None):
        self._name = name
        self._validators = validators or []
        self._error     = None
        self._raw_data  = None
        self._data      = None

    def parse(self, raw_data):
        '''
        raw_data: user input for the field
        '''
        self._raw_data = raw_data
        try:
            # validate form 
            for v in self._validators:  
                v.validate(raw_data)
            
            # transform raw_data (of type string) into the desired data type or format
            self._transform(raw_data)   

        except ParseError as pe:
            self._error = str(pe)


    def _transform(self, raw_data):
        self._data = raw_data # apply no transform for basic fields

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self._error

    @property
    def raw_data(self):
        return self._raw_data
    
    @property
    def is_valid(self):
        return self._error is None


class DateField(Field):
    def _transform(self, raw_data):
        try:
            # Parse string into a date object
            self._data = datetime.strptime(raw_data, '%Y-%m-%d')
        except:
            raise ParseError('Required date format: YYYY-mm-dd')



'''
FORM VALIDATORS
'''
class Validator(ABC):

    def __init__(self, error_msg=''):
        self._error_msg = error_msg

    @abstractmethod
    def validate(self, raw_data):
        pass


class InputRequired(Validator):

    def __init__(self, error_msg='This field cannot be empty'):
        super().__init__(error_msg)

    def validate(self, raw_data):
        if raw_data is None or raw_data == '':
            raise ParseError(self._error_msg)
