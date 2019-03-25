# Lab 06 (Due Week 6, Sunday, 31st March 11:59 pm) (20 marks)

# Aim

1.  Develop skills to build exception handling and perform unit-testing with Pytest

# Python Videos

Watch the tutorial videos by Hussein and Isaac:
1.  [Pytest Intro](https://www.youtube.com/watch?v=oPsuzDvwHgg&index=12&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW)
2.  [Test Driven Development](https://www.youtube.com/watch?v=TfJHsEVw58c&index=14&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW) 
4.  [Exception Handling](https://www.youtube.com/watch?v=OJqP-xR5HwA&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW&index=13)

# Lab Instructions

In this lab, you will implement exception handling and build some test-cases to test your application. To get started, import the lab code from:  [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs).

This lab must be completed  **individually**  and uploaded to GitHub by Sunday, end of Week 06.


### 1.  Implement a new use-case - "Search for a car by "make" and model" ( 4 marks )

The owners of Affordable Car Rentals would like to make changes to the search functionality.  They would like customers to search for cars by a specified "make" or "model".  For example, if you specify “Falcon” as the model and click on search, this should display all the cars in the rental system that match that model. If no criteria has been specified, then display all cars.  Your task is to implement this new use-case  “Search for a car by make and model”.  To implement the logic for this filter search, you will need to:

1.  Implement the function  `search_car(self, name, model)`  in the file  `car_rental_system.py`


###  2.  Implement the use-case “Get all car bookings” (2 marks)

Choosing a particular car from the search result above, should show a list of all current bookings for the car.   For this task, you will need to:

2.  Implement the function  `get_car(self, rego)`  in the file  `car_rental_system.py` which will return the selected car, that contains all the details about the car and the current bookings for the car.   

###  3.  Exception Handling (8 marks)

For this task, you will implement exception handling for the user story “Book a car” (read the user stories provided to you). Complete the following tasks:

1.  Create a user-defined exception  `BookingError`  in  `error.py`  which defines a constructor that takes the name of the invalid field provided and an error message *( 1 marks )*
2.  Modify the function  `make_booking()`  to carry out the following tasks *( 6 marks )* :
    -   Validate the input fields: dates and locations as specified in the acceptance criteria
    -   Raise a  `BookingError`  exception if an invalid value is specified for the dates or the locations. Appropriate error messages must be assigned for each type of invalid input
    -   Define a  `try/except`  block to handle the exception and return the error message if a validation error occurs *( In the next lab, you will display this error message to the user, when you build the front-end using Flask )* else, if booking is successful, return the booking
3.    Write a method  `check_fee()`  in  `car_rental_system.py`  which validates user input in the same way as  `make_booking()`  and returns the expected fee for valid inputs.  *( 1 marks )*

### 5. Build Test Cases Using Pytest (6 marks)

1.  In your virtual environment, install Pytest by typing:  
    `pip3 install pytest`
2.  Read user-stories `Book a car`, `Search a car by make and model`  provided to you and build test-cases in  `test_make_booking.py`, `test_search.py` to define test-cases corresponding to the acceptance criteria defined for this user-story. Feel free to add any test cases that you think are important.  A sample test-case has been provided in `test_make_booking.py` to help you.

Make sure to test your  **thoroughly**  in order to receive  **full marks**  for this section

