  
# Lab 02 (Due Week 02, Sunday, 11:59 pm) (14 marks (+2 bonus))

# Aim

1.  Register your team for the group project
2. Understand the importance of **requirements engineering** and create requirements specifications using **user stories**
3. Learn Python  
    \- Python data structures: **lists, dictionaries, tuples**  
    \- **Writing functions**  
    \- **Built-in functions** in Python

# Prelab Tasks

 ###  To assist you with the Python tasks in this lab, watch the following videos

   1.  [Functions](https://www.youtube.com/watch?v=TqA_kg6nhyo)
   2.  [Modules and Virtual Environments](https://www.youtube.com/watch?v=hc1sDvTjUo4)
   3.  [List Data Structure](https://www.youtube.com/watch?v=BXyEcdTtlm8)
   4.  [More Data Structures](https://www.youtube.com/watch?v=DZss6668dQ0)

### Group Project Setup

For your upcoming group project you will be required to work in a **groups of 3**.  You will need to form a team for your group project. 

Once your team has been formed one member from the team will need to register it:

1.  Go to [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login) and sign in
2.  Click on the **Teams** button. This will show you a form that you must fill out
3.  Select your tutorial from the left drop-down menu and think of a team name (do NOT use any emojis or similar special characters)
4.  Click **Create**
5.  Follow the link in the notification to add your other team members. This will create a team within the cs1531 GitHub organisation.

*If you have been unable to form a team prior to your lab 2, you may seek the assistance of your tutor during your lab session,  While they will try to accommodate your preferences for teammates, they may have to make adjustments to ensure teams have **3 members**.*
  

# Part 1 - Requirements Analysis and Writing User Stories (10 marks)

This part of the lab **must be completed during your lab session** and for this lab, you are expected to work with the team that you have created for your group project  Read the following case-study.
  
### Case-Study: Affordable Rentals

*AffordableRentals_* is a company specialising in car rentals to customers. The company would like to develop a web-based car rental system to enable customers to rent cars online prior to their scheduled pick-up date and time. This software development project has been contracted to a software consultancy firm who has completed the requirements gathering and developed the following high-level problem statement. For the purposes of this lab, the scope of the system is limited to the following functionality.

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
     

### Task (10 marks)

Analyse the problem statement above to develop a set of **user stories** that captures the system’s requirements. For this exercise, you are required to do the following:

1.  Write epic stories that capture the requirements in large logical groups **(2 marks)**
2.  Break up your epic stories into atomic user stories with a title for each **(4 marks)**
3.  For each user story, define its acceptance criteria **(3 marks)**
4.  Allocate sensible user story points to each user story and provide your estimate of how many hours of work each user story point represents **(0.5 mark)**
5.  Define a priority scheme (e.g., low, medium, high) and assign priority to each user story **(0.5 mark)**

*Note: both your epic stories and the user stories should be in RGB (role-goal-benefit) format*

***For the above exercise, discuss with your team members to write the user-stories.  **Only one person** in the team is required to document the user-stories and once you have completed the task, your team can be marked off by your tutor.***

  
# Part 2 - Python Exercises (4 marks + 2 bonus)

This part of the lab **must be completed individually** and solution to this lab must be uploaded to GitHub by the due date.  

## Setup

This lab uses the `pytest` package and some plugins to test the programming exercises.

You will need to install these packages in order to run the tests. To do this, you will use a **virtual environment** which is essentially a nice way to manage Python libraries by per-project basis. Read [Virtual Environments in Python](http://cse.unsw.edu.au/~cs1531/19T1/extra/virtualenv.html) for more information.

  
### Instructions

1.  Watch the videos on **Python** and **Virtual Environment** (links provided in the prelab section)
2.  Import the starter code for **lab02** from [here](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs/)
3.  Setup the virtual environment for your lab code:

```bash
cd project-directory-name
virtualenv --python=python3 venv # Create the venv folder in the current directory.
. venv/bin/activate # Activate the virtual environment.
pip3 install -r requirements.txt # Install dependencies in the virtual environment.
```

  

## Exercises (4 marks)

### Exercise 1 - `numbers_list.py` (1 mark)

Perform each of the following tasks with _one line_ of Python code

Given a list of numbers (e.g., `numbers = [2,4,-23,2,95]`), return:

1.  reverse of the list
2.  largest number
3.  minimum number
4.  sum of the numbers
5.  numbers sorted in descending order
6.  average of the numbers

**Test**

```bash
python3 -m pytest test_number_list.py
```

  
  

### Exercise 2 - `count.py` (3 marks)

**Task 2.1 (1 mark)**

Write a function that takes in a string and counts the number of times each character occurs in the text. The function should print each character and its count as in the example below:

```python
>> count_char('HelloOo!')
H 1
e 1
l 2
o 2
O 1
! 1
```

That is, each character should be printed in a separate line, and for each character, it should be printed along with its count separated by a space. Additionally, characters should be printed in the order they appear in the text.

  

**Task 2.2 (1 mark)**  
Now, modify the above function so that it works in a case-insensitive manner. E.g.,

```python
>> count_char_insensitive('HelloOo!')
h 1
e 1
l 2
o 3
! 1
```

_Hint: see if you can complete this task in one line of code_

  

**Task 2.3 (1 mark)**  
Now print the characters in the descending order of count (case-insensitive). E.g.,

```python
>> count_char_ordered('HelloOo!')
o 3
l 2
h 1
e 1
! 1
```

If there are characters with the same count (e.g., `h` , `e` and `!` in the above example), then they should be printed in the order they appear in the text.

**Test**

```bash
python3 -m pytest test_count.py
```

  
  

### Bonus Exercise (2 marks)

**Bonus 1**  
Write a function that takes in a list of numbers and returns the second smallest number in the list **(1 Mark)**

-   E.g. if `numbers = [4,1,1,2,3,2]`, then the output should be `2`
-   You may assume that 2nd smallest number will always exist for the given list

**Bonus 2**  
Write a function that takes in a list of numbers and an integer `k` and returns the k-th smallest number in the list **(1 Mark)**

-   You may assume that k-th smallest number will always exist for the given list and `k`

_Extra requirement: your solution for the 1st task should use a different approach to your solution for the 2nd task!_

**Test**

```bash
python3 -m pytest test_number_list.py
```

  

## Optional Task (worth kudos!)

### Fibonacci Extension

Write a **recursive function** in `fibonacci.py` that returns the `n`-th number in the Fibonacci sequence given the index `n` as the argument of the function.

The Fibonacci sequence for this exercise should start from 1. The first 10 numbers are shown below:

```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
```

**Example I/O**

```python
>> print(fib_sequence(3))
2
>> print(fib_sequence(7))
13

```

**Test**

```bash
python3 -m pytest test_fib.py
```

  

## Testing All Files

```bash
python3 -m pytest
```
