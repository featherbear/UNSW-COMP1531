from datetime import datetime

class BookingError(Exception):

    '''
    To be completed
    '''
    def __init__(self, errors, message = None):
      self._errors = errors
      if message is None:
        msg = "Booking validation error occurred with fields: %s"%(', '.join(errors.keys()))
      super().__init__(message)
    
    @property
    def errors(self):
      return self._errors
    
    @property
    def message(self):
      return self._message

def check_booking_error(start_date: datetime, end_date: datetime, start_location, end_location):
    errors = {}

    '''
    to be completed
    '''
    
    if end_date < start_date:
      errors['date'] = "End date is before the start date"
    
    if not start_date:
      errors['start_date'] = "No start date provided"
    
    if not end_date:
      errors['end_date'] = "No end date provided"
    
    if not start_location:
      errors['start_location'] = "No start location provided"
    
    if not end_location:
      errors['end_location'] = "No end location provided"
    
    return errors


