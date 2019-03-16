# Lab 05 (Due Week 05, Sunday, 24th March 11:59 pm) (10 marks)


# Aim
1. Translate the conceptual class diagram to Python classes
2. Start writing tests yourself!

# Python Videos

Familiarise yourself with Object Oriented concepts and Test Driven Development with Python videos by Anna:

Video #7. [OOP and Encapsulation](https://www.youtube.com/watch?v=f3PA7LveBOA&index=7&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW)  
Video #8. [Abstraction, inheritance, Abstract classes](https://www.youtube.com/watch?v=7vuO3zEq3J4&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW&index=8)  
Video #9. [Aggregation and Composition](https://www.youtube.com/watch?v=bPwGhF0n7q0&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW&index=9)  

Or if you want to learn more, watch the whole [playlist](https://www.youtube.com/playlist?list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW)!


# Implementing the Python classes
In this lab, you will be implementing one of the use-cases for the car rental system; map the *conceptual class diagram* from last lab to *Python classes* with their corresponding attributes.

This lab must be completed **individually** and uploaded to GitHub by Sunday, end of Week 05.

## 0. Setup Instructions

There is a starter code available for this lab, which you can import from [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs).

Here's a detailed instruction for importing the starter code:
1.  Go to [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs). 
2. Select lab05 and click **Import**
3.  Follow the link that is shown in the green banner flashed at the top of the screen to go to the place where the repo has been imported
4.  Click on the **Clone or download** button.  
![enter image description here](https://lh3.googleusercontent.com/fRKmSGm0qTZZnPtE70T9AR0CmhgQL-Jj5U7N1etS407LDClwFeaWWo8Xa6b8HEMSanANCvR0lDE=s900)
    
5.  If the title for the dropdown box is _Clone with HTTPS_ click on the **Use SSH** link on the right. The box should look like the below  
	![enter image description here](https://lh3.googleusercontent.com/8RM5PDX21n-QxcLDT0xWwLLNSfayAdpPrdU8K1JHIM6XQQX6brM3hXbUgcraUklT5G_AowslXOc=s900)

6.  Copy the link in the text box
7.  Open a Terminal and navigate to the folder you want the lab to be in
8.  `git clone [link]` (Replace \[link\] with the copied link from above step)
9.  Type `ls` to ensure the folder has been copied correctly
10.  `cd [repo_name]` to navigate into the cloned repo


## 1. Create Python classes (2 marks)

1. For each class, implement a **constructor** to ensure that the objects of the class are instantiated appropriately.
2. The base class `Car` should **NOT be instantiable**
3. Each class must adhere to OO **encapsulation** and implement appropriate getter methods using Python **properties** 
	- If you are not sure what they are, refer back to the lecture demo on Python properties and the optional section in this week's tutorial
4. Override the `__str__` method in the class `Car` (and its derived classes) to provide an appropriate string representation of each class.

Check the example output in *Task 3* for more clarification on the expected behaviour .

## 2. Implement the use-case to Book a car (4 marks)

For this task, you only need to implement the use-case to “book a car”. All other use-cases (search for a car, payment etc.) are not required to be implemented. For this use-case, you can ignore the purchase of insurance.  

To book a car, the following sequence of steps needs to be taken:

1.  Accept booking details from the user
    -   Customer details (name, licence number)
    -   Rental period (number of days)
    -   Pickup and drop-off location

2. Create a car booking for the customer and return an email confirmation to the customer advising of the customer’s name, details of car booked, rental period and total rental fee
	- For this exercise, email notification can simply be implemented as printing to the console the customer name, details of car booked, period booked and total rental fee. *Hint: use the `__str__()` method*

3.  The total rental fee should be computed based on the type of car rented and the number of days. The following business rules are to be applied in the computation.
    -   Each car carries a daily rental rate.
    -   For all cars, the rental fee is the product of the daily rate and the number of days the car is rented.
    -   Additionally, for large cars and premium cars, if the number of days rented exceeds a week, then an overall discount of 5% is applied.
    -   Premium cars are charged an additional 15% tariff on the daily rate.

Check the example output in *Task 3* for more clarification on the expected behaviour.

## Task 3: Testing the Implementation for Booking and Fee Calculation (4 marks)

Create some test data to demonstrate your implementation using **print statements**. Write your tests in a separate file called `client.py`.

Your test must include booking each type of car (small, medium, large, premium) under various booking conditions, especially the rental period.

Provided below is an example of what your test outputs may look like. Note that you do not have to follow the exact format as below, but you are required to test your implementation more rigorously. **Marks will be deducted for inadequate testing.**

```
~~~ Print all customers ~~~
Customer <name: Matt, licence: 1>
Customer <name: Isaac, licence: 2>
Customer <name: Taylor, licence: 3>

~~~ Print all cars ~~~
Small Car <Mazda, Falcon, rego: 1>
Medium Car <Mazda, Falcon, rego: 2>
Large Car <Mazda, Falcon, rego: 3>
Small Car <Mazda, Commodore, rego: 4>
Medium Car <Mazda, Commodore, rego: 5>
Large Car <Mazda, Commodore, rego: 6>
Small Car <Holden, Falcon, rego: 7>
Medium Car <Holden, Falcon, rego: 8>
Large Car <Holden, Falcon, rego: 9>
Small Car <Holden, Commodore, rego: 10>
Medium Car <Holden, Commodore, rego: 11>
Large Car <Holden, Commodore, rego: 12>
Small Car <Ford, Falcon, rego: 13>
Medium Car <Ford, Falcon, rego: 14>
Large Car <Ford, Falcon, rego: 15>
Small Car <Ford, Commodore, rego: 16>
Medium Car <Ford, Commodore, rego: 17>
Large Car <Ford, Commodore, rego: 18>
Premium Car <Tesla, model x, rego: 19>
Premium Car <Tesla, A4, rego: 20>
Premium Car <Tesla, S class, rego: 21>
Premium Car <Audi, model x, rego: 22>
Premium Car <Audi, A4, rego: 23>
Premium Car <Audi, S class, rego: 24>


~~~ Make first booking ~~~
=== Booking Successful! ===
Booking details:
Made by Customer <name: Taylor, licence: 3>
Reserve Medium Car <Mazda, Commodore, rego: 5> for 7 days
Locations: <pickup: Sydney, dropoff: Canberra>
Total fee: $525.00
=== Thank you for using Affordable Rentals ===


~~~ Make second booking ~~~
=== Booking Successful! ===
Booking details:
Made by Customer <name: Isaac, licence: 2>
Reserve Premium Car <Tesla, S class, rego: 21> for 12 days
Locations: <pickup: Earth, dropoff: Moon>
Total fee: $2070.00
=== Thank you for using Affordable Rentals ===


~~~ Print all bookings ~~~

Made by Customer <name: Taylor, licence: 3>
Reserve Medium Car <Mazda, Commodore, rego: 5> for 7 days
Locations: <pickup: Sydney, dropoff: Canberra>
Total fee: $525.00

Made by Customer <name: Isaac, licence: 2>
Reserve Premium Car <Tesla, S class, rego: 21> for 12 days
Locations: <pickup: Earth, dropoff: Moon>
Total fee: $2070.00
```


