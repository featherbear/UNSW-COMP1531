from flask import render_template, request, redirect, url_for, abort
from server import app, system
from datetime import datetime
from src.location import Location
# from src.error import BookingError, LoginError
from src.customer import Customer


'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404



'''
Search for Cars
'''
@app.route('/', methods=["GET", "POST"])
def cars():

    if request.method == 'POST':
        make  = request.form.get('make')
        model = request.form.get('model')

        if make == '':
            make = None

        if model == '':
            model = None

        cars = system.search_car(make, model)
        return render_template('cars.html', cars = cars)
    
    return render_template('cars.html', cars = system.cars)




'''
Display car details for the car with given rego
'''
@app.route('/cars/<rego>')
def car(rego):
    car = system.get_car(rego)

    if not car:
        abort(404)

    return render_template('car_details.html', car=car)


'''
Make a booking for a car with given rego
'''
from src.forms import BookingForm
@app.route('/cars/book/<rego>', methods=["GET", "POST"])
def book(rego):
    car = system.get_car(rego)

    if not car:
        abort(404)

    if request.method == 'POST':
        if "make" not in request.form and "check" not in request.form:
          abort(404)
        
        form = BookingForm(request.form)
        print(request.form)

        # 1. If form is not valid, then display appropriate error messages
        if not form.is_valid:
          return render_template('booking_form.html', errors = form.errors, form = request.form)

        # 2. If the user has pressed the 'check' button, then display the fee
        if "check" in request.form:
          checkData = dict(fee = system.check_fee(car, form.start_date, form.end_date))
          
          return render_template('booking_form.html', car=car, data=checkData, errors=False, form = request.form)
        
        # 3. Otherwise, if the user has pressed the 'confirm' button, then 
        #   make the booking and display the confirmation page
        
        customer = Customer(form.customer_name, form.customer_licence)
        booking = system.make_booking(customer, car, form.start_date, form.end_date, form.start_location, form.end_location)
        bookingData = dict(booking = booking)
        return render_template('booking_confirm.html', car=car, data = bookingData)

    return render_template('booking_form.html', car=car, form={})

'''
Display list of all bookings for the car with given 'rego'
'''
@app.route('/cars/bookings/<rego>')
def car_bookings(rego):
    return render_template('bookings.html', bookings=system.get_bookings_by_car_rego(rego))