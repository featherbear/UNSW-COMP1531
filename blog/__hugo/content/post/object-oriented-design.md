---
title: "Object Oriented Design"
date: 2019-03-09T21:43:28+11:00

categories: ["Info"]

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

Object Oriented Programing is a design paradigm (approach) where data is assigned to a discrete object.

# Overview

Each object has:

* **Attributes** - Properties of the object
* **Behaviours** - The actions of the object (aka method)

The **state** of an object are the values of its attributes

# Classes vs Objects
A class is a definition of the structure of an object.  
An object is an instance of a class.

Keywords: An object is said to be **instantiated** from a class. 

# Abstraction
_Think of class inheritance..._  

An abstraction of a `Dog` and a `Cat`, would be for example, that they are both `Animals`.

Abstraction serves to generalise the properties and behaviour of objects - discarding the specific nuances of each object

# Encapsulation
Encapsulation refers to the private scope of an object's attributes.  

The attributes in an object <u title="It can in Python">'cannot'</u> be accessed by external entities.  
Rather, the object must invoke one of its methods to retreive the attribute

#Aside (not in course)#

## Polymorphism
Ability for an object to act as a different data type depending on how it is used

## Overloading
Ability for a method to take in different parameters - but doesn't occur in Python as it is a dynamically typed langauge