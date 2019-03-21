---
title: "[UML] Class Diagram"
date: 2019-03-09T21:58:24+11:00

categories: ["UML", "Structural Diagrams"]

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Class

| CLASS NAME |
|:-----------|
|-Attribute_1: type<br>-Attribute_2: type<br>-Attribute_3: type|
|+Method_1(): type<br>+Method_2(): type<br>+Method_3_(): type|

That is, three cells:  
Cell One - Class name  
Cell Two - Attributes (possibly with type)  
Cell Three - Methods (possibly with function input types and output type)

# Child Class
Syntax: Connect the child to the parent with a hollow triangle  
A **'is a kind of'** relationship.  

![](Snipaste_2019-03-09_22-13-36.png)

# Associations
Syntax: Connect the two classes with a solid line  
A **'has-a"** relationship.  

## Aggregation (◊)
Syntax: Connect the element to the container (diamond on the container)  
The contained item is an element, but can also exist on its own.  
Aka the container will function with or without the element.  
_(ie A room contains computers - each computer does not rely on its existence in the room)_

## Composition (♦)
Syntax: Connect the element to the container (diamond on the container)  
The element is an integral part of the container.  
Aka the container will not function without the element.  
_(ie the leg of a desk)_

# Cardinality
* One to One
* One to Many
* Many to Many 

---

![](20190306_144140.jpg)
![](sketch.png)
![](sketch_2.png)
