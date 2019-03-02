lab03.html

# Lab 03_04 (20 marks + 2 bonus)

## Due Dates

-   Due end of **Week 04**, Sunday, 11:59 pm: bonus Python component (individual submission)
-   Due end of **Week 04**, Sunday, 11:59 pm: (group submission)

**All artefacts must be uploaded to GitHub by the respective due-dates.**

# Aim

1.  Understand the importance of requirements engineering and create requirements specifications based on UML **use-cases**.
2.  Understand how to create a **domain model** based on **object oriented design** principles
3.  Develop skills to design a **conceptual class diagram**
4.  Get familiar with **[draw.io](http://draw.io) on the CSE machines** (_mid-term exam preparation!_)
5.  More Python for bonus!

# Python Videos

Familiarise yourself with Object Oriented concepts and programming with more Python videos by Anna:

Video #8. [OOP and Encapsulation](https://youtu.be/f3PA7LveBOA)  
Video #9. [Abstraction, inheritance, Abstract classes](https://youtu.be/7vuO3zEq3J4)  
Video #10. [Aggregation and Composition](https://youtu.be/bPwGhF0n7q0)  
Video #12. [Pytest Intro](https://youtu.be/oPsuzDvwHgg)

Or if you want to learn more, watch the whole [playlist](https://www.youtube.com/playlist?list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW)!

# Lab Instructions

In this week’s lab, you will continue working on the same _AffordableCarRentals_ case-study from the last week. Your task is to develop requirements specifications for the case study through **use-case modelling**; and based on those specifications, you will then be creating a **domain model**

This lab must be completed in your **project group**. Similar to your group assignment, every member of the group is required to contribute _equally_ to this lab component. Only **one copy** of the various design artifacts will need to be pushed to the master branch on GitHub.

# PART I - Requirements Analysis (10 marks)

## Case-Study: Affordable Rentals

_AffordableRentals_ is a company specialising in car rentals to customers. The company would like to develop a web-based car rental system to enable customers to rent cars online prior to their scheduled pick-up date and time. This software development project has been contracted to a software consultancy firm who has completed the requirements gathering and developed the following high-level problem statement. For the purposes of this lab, the scope of the system is limited to the following functionality.

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
    

## Tasks

1.  Identify the system **actors** and **goals**. **(1 mark)**
    
2.  Draw a **use-case diagram** to model the behaviour of the online rental system. The model should include the actors, the use cases, the relations between the use cases and the actors and the relation between the use cases. _(Refer to the lecture slide “Use Case Diagram: Device Control” to help you with this task.)_ **(5 marks)**
    
3.  Define a detailed specification for the **main usage scenario** for the use-case of renting a car. **(4 marks)**
    
    Use the template provided in the lecture to define this specification. It must include:
    
    -   _Use-case name_;
    -   _Brief description_;
    -   _Initiating Actor_;
    -   _Actor’s goal_;
    -   _Participating actors_;
    -   _Flow of events **only** for the Main Success usage scenario_.
    
    **For the purposes of this lab, you don’t need to define the pre-condition, post-condition and the alternate usage scenarios.**  
    _(Refer to the lecture slide “Use Case 1: Unlock” to help you with this task.)_
    

## Using [draw.io](http://draw.io)

To obtain marks for the above task, you **must** draw the use-case diagram using [draw.io](http://draw.io) **that is already installed on the CSE machines.** In the upcoming _mid-term exam_, you will be required to develop your solutions using this tool.

If you wish to use [draw.io](http://draw.io) for your group assignment, you are free to use the online version of the tool at [https://www.draw.io/](https://www.draw.io/) or download an offline copy on your own machine.

### Instructions

1.  Login into a CSE machine
2.  Right-click on the desktop the open up the context menu
3.  Go to _Applications > Graphics > [draw.io](http://draw.io)_ to open [draw.io](http://draw.io)
4.  Click “Create New Diagram”
5.  Name your diagram, and “Create a blank diagram”
6.  On the left of the screen is a list of built-in components; under **UML**, you should be able to find elements you need for your use-case diagram
7.  To save a work-in-progress version of your diagram, go _File > Save as_. If you save the xml file in your local repo, then you can add it to GitHub like any other file.
8.  To export a complete diagram, go _File > Export As > \[file type\]_. This will download the current diagram as a \[file type\]. For your assignment, you should choose _PDF_ as the file type.

# PART II: Domain Modelling (10 marks)

1.  Using the use-cases developed in Part 1, identify key classes using **CRC cards**. **(4 marks)**  
    A CRC card is written using the following template:
    
    ```
      < Class Name >  
      Responsibilities Collaborators
    
    
    ```
    
    CRC cards can be _hand-written_. No case tools needed
    
2.  Using the CRC cards, develop a UML **conceptual class diagram** using [draw.io](http://draw.io) **(6 marks)**
    
    The conceptual class diagram needs to show **only** the _class-names, relationships_ and _attributes_. For this lab, the class diagram does **not** need to show the _methods_.
    
    In [draw.io](http://draw.io), use the following elements (under UML) for your class diagram:  
    \- _Object_ box for your classes (first element in the list)  
    \- Last 3 elements in the list for aggregation, composition and association respectively  
    \- _Generalisation_ arrow for inheritance.
    

## Submission & Demo

Tasks in Parts I and II are to be completed with your group project team. To obtain marks for this section, make sure that your team has pushed a PDF copy of each of the design artifacts created to the master branch by the due date.  
_These design artifacts will be marked by your tutor in week 5 lab session after the mid-term exam._

# Bonus Task - Python Exercises (2 marks)

This part of the lab **must be completed individually** and your solutions must be uploaded to GitHub by the due date.

Please make sure to use **virtual environment** for this lab as well.

### Instructions

1.  Import the starter code for **lab03** from [here](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs/)
2.  Setup the virtual environment for your lab code:

```bash
cd project-directory-name
virtualenv --python=python3 venv # Create the venv folder in the current directory.
. venv/bin/activate # Activate the virtual environment.
pip3 install -r requirements.txt # Install dependencies in the virtual environment.


```

### Extended NumberGuesser (2 Marks) - `numberGuesser.py`

Anna’s video on [Syntax and Control Structures](https://www.youtube.com/watch?v=TqA_kg6nhyo&index=3&list=PLbSaCpDlfd6p1h87LKUWDa7TBGQhLYQXW) provides an implementation of a simple number guesser game.

Your task is to write a more sophisticated version of the number guesser that does the following:

1.  Generates a random list of numbers (this part has been done for you)
2.  The user will guess a number, and if the number _exists_ in the list, that number is removed. Otherwise, the program will reveal whether the closest number in the list is higher or lower than their guess
3.  The game ends when the user quits early by pressing `q`
4.  The message `Thanks for playing! See you soon.`

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

## Testing

Similar to the last lab, you will use the `pytest` package to test your program. You can run the tests by simply running

```bash
python3 -m pytest


```
