# Lab 03 (Due Week 03, Sunday, 11:59 pm) (10 marks (+2 bonus))

# Aim

1.  Understand the importance of **requirements engineering** and create requirements specifications based on UML **use-cases**.
2.  More Python for bonus!

<br/>

# Lab Instructions

## PART 1 - Requirements Analysis (10 marks)

In this week's lab, you will be working on the same *AffordableCarRentals* case-study from the last week. Your task is to develop requirements specifications for the case study through **use-case modelling.**


This lab must be completed during your lab session and for this lab, you are expected to work in your **project group**. Just like your group assignment, every member of the group is required to contribute *equally* to this lab component.

A copy of the case study has been provided below.


### Case-Study: Affordable Rentals

*AffordableRentals* is a company specialising in car rentals to customers. The company would like to develop a web-based car rental system to enable customers to rent cars online prior to their scheduled pick-up date and time. This software development project has been contracted to a software consultancy firm who has completed the requirements gathering and developed the following high-level problem statement. For the purposes of this lab, the scope of the system is limited to the following functionality.

1.  A car rental is a vehicle that can be used temporarily for a fee during a specified period.
    
2.  The cars that can be rented from _AffordableRentals_ are grouped into small, medium, large and premium cars.
    
3.  A customer should be able to specify search criteria and view available cars that match the search criteria. The search criteria should include age, preferred pick-up and drop-off locations.
    
4.  The search result should include details of the car type and price for each day of car rental.
    
5.  From the displayed search results, the customer can select a car and proceed with booking the car.
    
6.  During the booking process, the customer is required to specify additional details such as:
    
    -   name of the customer and age;
        
    -   licence number;
        
    -   the rental period in number of days;
        
    -   option to purchase an insurance cover; and
        
    -   email-address.
        
7.  Insurance is provided by an external company, QBEI Insurances.
    
8.  Once the booking details have been provided by the customer, a net price is computed and displayed to the customer.
    
9.  The customer proceeds with the booking by providing credit card details for payment. The company uses an external credit card system to handle payments.
    
10.  Once the payment has been confirmed, an email is sent to the customer confirming the booking.
    
11.  The online system must permit staff of _AffordableRentals_ to log in to the system with a username and password.
    
12.  Admins, once logged in, will be able to enter new car information into the system.
    
13.  For each car, the system will hold the following pieces of information: vehicle-type (small, medium, large, premium), make, model, year and registration number.
    
14.  Managers, once logged in, will be able to generate weekly reports that show a log of cars rented during the week.



**Instructions**

1.  Identify the system **actors** and **goals**. **(1 mark)**
    
2.  Draw a **use-case diagram** to model the behaviour of the online rental system. The model should include the **actors**, the **use cases**, the **relations** between the use cases and the actors and the relation between the use cases. _(Refer to the lecture slide "Use Case Diagram: Device Control" to help you with this task.)_ **(5 marks)**
    
3.  Define a detailed **use-case specification** for the main use-case of a customer renting a car. **(4 marks)**
    
    Use the template provided in the lecture to define this specification. It must include:
    
    -   _Use-case name_;
        
    -   _Brief description_;
 
    -   _Initiating Actor_;
        
    -   _Actor's goal_;
        
    -   _Participating actors_;
        
    -   _Flow of events **only** for the Main Success usage scenario_.
        

****For the purposes of this lab, you don't need to define the pre-condition, post-condition and the alternate usage scenarios.****

_(Refer to the lecture slide "Use Case 1: Unlock" to help you with this task.)_

To obtain marks for the above task, you must draw the use-case diagram using an appropriate modelling tool such as [draw.io](http://draw.io/), but it is not necessary. The use-case specification can be typed up. 
 
**All artefacts must be uploaded to GitHub by the due-date.**


<br/>


## Bonus Task - Python Exercises (2 marks)

This part of the lab **must be completed individually** and your solutions must be uploaded to GitHub by the due date.  

Please make sure to use **virtual environment** for this lab as well.

### Instructions
 1. Import the starter code for **lab03** from [here](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs/)
 2. Setup the virtual environment for your lab code:

```bash
cd project-directory-name
virtualenv --python=python3 venv # Create the venv folder in the current directory.
. venv/bin/activate # Activate the virtual environment.
pip3 install -r requirements.txt # Install dependencies in the virtual environment.
```

  <br>

### Extended NumberGuesser (2 Marks) - `numberGuesser.py`

Anna's video on [Syntax and Control Structures](https://www.youtube.com/watch?v=TqA_kg6nhyo&index=3&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW) provides an implementation of a simple number guesser game.

Your task is to write a more sophisticated version of the number guesser that does the following:
1. Generates a random list of numbers (this part has been done for you)
2. The user will guess a number, and if the number *exists* in the list, that number is removed. Otherwise, the program will reveal whether the closest number in the list is higher or lower than their guess
3. The game ends when the user quits early by pressing `q`
4. The message `Thanks for playing! See you soon.`

<br/>
Your program should work like this:

```
Numbers are between 0 and 10 inclusive
There are 3 values left. Guess: 5
You found 5! It was in the list
There are 2 values left. Guess: 4
The closest to 4 is lower
There are 2 values left. Guess: 3
The closest to 3 is lower
There are 2 values left. Guess: 2
You found 2! It was in the list
There are 1 values left. Guess: 6
The closest to 6 is higher
There are 1 values left. Guess: 7
You found 7! It was in the list
Congratulations! You won!
Thanks for playing! See you soon
```

You will need to complete the functions `run_game`, `handle_guess` and `find_closest`.

-   `run_game` should keep asking for guesses from the user until the game is over, and handle guesses appropriately.
-   `handle_guess` should return a **new list** with the guessed number removed if it is in the list.
-   `find_closest` should return the closest number in the list to the guess.

The output of your program should work as shown in the example above.

<br/>

## Testing

Similar to the last lab, you will use the `pytest` package to test your program. You can run the tests by simply running

```bash
python3 -m pytest
```

