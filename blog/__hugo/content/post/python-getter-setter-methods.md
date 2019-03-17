---
title: "Python Getter/Setter Methods"
date: 2019-03-13T14:54:22+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

Setters and getters are implentations of [Object Oriented designs](../object-oriented-design) where encapsulated data are exposed from the object.  

A setter executes an object's method to update properties of that object.  
A getter executes and returns a value from an object's method.  

# Method One - `property(getter, setter)`
```python3
class Animal:
  def __init__(self):
    self._age = 30
  
  def getAge(self):
    return self._age
  
  def setAge(self, age):
    self._age = age
  
  age = property(getAge, setAge)  
```

# Method Two - Function decorator
```python3
class Animal:
  def __init__(self):
    self._age = 30
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, age):
    self._age = age
  ```