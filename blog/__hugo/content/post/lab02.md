---
title: "Lab 2 - User Stories Exercise"
date: 2019-02-25T14:25:58+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Case-Study: Affordable Rentals

<details>
<summary>> See details</summary>
_AffordableRentals_ is a company specialising in car rentals to customers.  
The company would like to develop a web-based car rental system to enable customers to rent cars online prior to their scheduled pick-up date and time. This software development project has been contracted to a software consultancy firm who has completed the requirements gathering and developed the following high-level problem statement.  
For the purposes of this lab, the scope of the system is limited to the following functionality.

* A car rental is a vehicle that can be used temporarily for a fee during a specified period.
* The cars that can be rented from AffordableRentals are grouped into small, medium, large and premium cars.
* A customer should be able to specify search criteria and view available cars that match the search criteria. The search criteria should include age, preferred pick-up and drop-off locations.
* The search result should include details of the car type and price for each day of car rental.
* From the displayed search results, the customer can select a car and proceed with booking the car.
* During the booking process, the customer is required to specify additional details such as:
  * name of the customer and age;
  * licence number;
  * the rental period in number of days;
  * option to purchase an insurance cover; and
  * email-address.
* Insurance is provided by an external company, QBEI Insurances.
* Once the booking details have been provided by the customer, a net price is computed and displayed to the customer.
* The customer proceeds with the booking by providing credit card details for payment. The company uses an external credit card system to handle payments.
* Once the payment has been confirmed, an email is sent to the customer confirming the booking.
* The online system must permit staff of AffordableRentals to log in to the system with a username and password.
* Admins, once logged in, will be able to enter new car information into the system.
* For each car, the system will hold the following pieces of information: vehicle-type (small, medium, large, premium), make, model, year and registration number.
* Managers, once logged in, will be able to generate weekly reports that show a log of cars rented during the week.
</details>


--- 

# Epic Stories
1) As a customer, I am able to select a car to their preference and pay through the system so that I can efficiently order a car

2) As a manager, I am able to create reports so I can oversee the performance of the car rentals.

3) As an admin, I am able to manage the available cars in the rental system to ensure that cars can be rented.

# User Stories
1.1) As a customer, I should be able to search the cars to a criteria (age, size) so that I can find the cars that I prefer (7 hours, HIGH)

  * When a customer searches for a car, they should be given details of the car (vehicle type, make, model, year, registration number), available insurance options, and the daily rental price
  * If no car matches the search criteria, the customer should receive an error message (No cars found)
  * When search results are returned to the customer, the customer should be given an option to see more details about the car (photos, reviews, etc) as well as an option to add the car to a compare/watch-list.
  * If there are few cars matching the criteria, the system should be additional return similar listings that may be of interest
  * As a customer, I should be able to select which pickup and dropoff location I want to so I can collect and return the car conventiently (4 hours, MEDIUM)
  * If the car is far away from the requested pickup location, a the user should be given a delay time as a notification.>

1.2) As a customer, I should be able to enter my payment / personal / insurance details so that the system can process my order (2 hours, MEDIUM)  

  * When a customer enters their personal details, their phone number and email address should be validated
  * If details are invalid, the customer should be prompted to fix their details
  * When a customer rents a car, the payment provider should be notified.
  * If the payment is unsuccessful, the user should receive an error message
  * If the payment is succcessful, the manager should be notified, to be able to verify the order.
  * When customers make an order, they should provide their name, age, credit card details, insurance option, email address, rental period, and license number
  * When a customer successfully rents a car, they should be sent a booking confirmation email to their provided email address.


2.1) As a manager, I should be able to create reports of car rentals of the week, so that I can better manage their company's performance and see a general overview (2 hours, LOW)

  * Managers should be given staff access to the system through credentials
  * If the wrong username or password is entered, an error message is displayed to the user.
  * A password reset / forgot option will be present on the logon screen.
  * If a car has already been entered, an error message should be displayed.

3.1) As an admin, I should be able to add new car information into the system so that the customers can search for and rent cars. (4 hours, HIGH)

  * Admins should be given staff access to the system through credentials
  * If the wrong username or password is entered, an error message is displayed to the user.
  * A password reset / forgot option will be present on the logon screen.
  * If a car has already been entered, an error message should be displayed.
  * When an Admin enters a new car into the system, the vehicle details should be added.
  * If details are left out in the New Car form, the staff should be notified to fill in all the fields

&nbsp;

&nbsp;


_This part goes somewhere..._
---

* When a customer successfully rents a car, the insurance company should be notified of the insurance option applied.
* ~As the insurance and payment provider, we should provide our services when requested so that the order is fulfilled.~
* Insurance providers should be able to see rentals associated with their respective insurance options so they know which insurance options to process. (1 hour, MEDIUM)
