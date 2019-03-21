---
title: "Python - Exceptions and Exception Handling"
date: 2019-03-19T14:00:00+11:00

categories: ["Python"]

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Exceptions
A Python exception is a runtime error signal that indicates a event.  

Compared to the `assert` functionality, exceptions can be _caught_ and dealt with in a programmatic way.  
This allows for a piece of code to be robust, and not completely self-destruct should something forseeably bad happen.

```python3
file = open("secrets.txt", r")
# FileNotFoundError: [Errno 2] No such file or directory: 'secrets.txt'
```

You can throw an exception by `raise`-ing it
```python3

raise FileNotFoundError
```

# Try .. Except .. Finally
Most languages have a try..catch block - In Python this is called a `try..except` block

```python3
try:
  # do these stuff here
  # they will execute as usual
  # if something bad happens
  # like this:
  print(1/0)
except ZeroDivisionError:
  # instead of the programming crashing
  # we can programmatically respond to the error
  print("Cannot divide by zero")
else:
  # if no exceptions occur
  # we could do some stuff here
  # though you might as well just put it after the usual statements in the original try block
  pass
finally:
  # At the end of either case (general case, or exception)
  # we can run the same final bit of code
  print("Finishing loop")
```

# Custom Exceptions
A custom exception can be created by extending the `Exception` base class.  
This exception can then be caught in the `except` clause of a try..except block

```python3
class NoSuchPerson(Exception):
  pass


def getPerson(id):
  people = {}
  if id not in people:
    raise NoSuchPerson(id)
  return people[id]


try:
  getPerson("andrew1532")
except NoSuchPerson as e:
  print(f"No user with ID `{e}` exists")
```