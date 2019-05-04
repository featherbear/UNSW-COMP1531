---
title: "Course Summary"
date: 2019-05-04T14:32:21+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

> Note: Heading links and TOC links will bring you to the related post

# Theory

## [Introduction to Software Engineering](../intro-to-software-engineering)

**Software engineering** is the discipline of the systematic planning, development, operation and maintenance of software.

Q. What's the difference between a programmer and a software engineer?  
A _programmer_ wites code.  
A _software engineer_ orchestrates the tasks of the programmer.  


## [Software Development Life Cycle](../software-development-lifecycle)

* Analysis - Finding the needs and wants of the customer and then system
* Design - Planning how the system will be implemented
* Implementation - Programming
* Testing - Testing of code, user acceptance testing
* Release and Evaluation - Release and feedback

## [Software Development Approaches](../software-development-approaches)

* Waterfall
  * Very formal and structured
  * Good for systems that have been thoroughly planned out
  * Bad for systems that have changing requirements - becomes costly to change
* Agile
  * Iterative and feedback-based
  * Good for systems whose requirements are not initially fully known
  * _is it really bad?_ - May lead to alot of changes from the client (angery devs)
  * [Rational Unified Process](../rational-unified-process)
    * Inception, Elaboration, Construction, Transition
    * All iterations involve all four phases, but the later iterations give more attention to the later phases
  * [Extreme Programming (XP)](../extreme-programming)
    * Pair programming
    * Continuous integration
    * Continuous refactoring
    * Test-driven Development
    * Daily meetings


## [User Stories](../user-stories)

* **User stories** are development artifacts which provide feature requirements that the software has to conform to.  
* **Epic stories** are a summary of all of the user stories of a specific role.  
* Each user story has several **acceptance criteria** which are specific requirements for that user story

* RGB (Role-Gole-Benefit) Framework for writing user stories  
  "*As a _______ I want to ______ so that _________*
* Story points - an estimation of how long a user story will take, one point is given an arbitrary duration

* The three C's
  * **C**ard - The physical representation (post-it note!) summarising who, what and why  
  * **C**onversation - The dialogue between parties, specifying concrete feature requests and requirements  
  * **C**onfirmation - The acknowledgement of the procured requirements and tasks

* The INVEST Framework
  * **I**ndependent
  * **N**egotiable
  * **V**aluable 
  * **E**timatable
  * **S**mall
  * **T**estable

## [Requirements Specification](../requirements-specification)

A **requirement** is a condition or capability needed by a user to fulfill an objective.  
They describe the external behaviour (as opposed to a Domain Model, which describes the internal behaviour)

* Functional requirements refer to the behaviour of a system (ie the response of a system on user input)
* Non-functional requirements refer to the meta-behaviour of a system (ie performance, reliability, usability).  

## [UML Diagrams](../unified-modelling-language)
Unified Modelling Language is a widely adopted language to model software solutions, data structures, system behaviours and other processes.

They are split into two categories, _structure diagrams (Static structure)_ and _behaviour diagrams (Dynamic changes over time)_.

## [Use Case Diagrams (UML)](../uml-use-case-diagram)
Each solid line represents an interaction between an actor and the system  
Each dotted line represents an interaction between a use case and another use case

* **Actors** are the objects that interact with the use cases; they can be either **initiators** or **participants** 
* Connections
  * \<\<initiates>>  
Usage: For actors that call a use case  
Syntax: Solid line between actor and the use case  
  * \<\<participates>>  
Usage: For actors that are involved in a use case  
Syntax: Solid line between actor and the use case
  * \<\<includes>>Usage: For required use cases  
Syntax: Dotted line **FROM** the use case, **TO** the use case that is included
  * \<\<extends>>  
Usage: For optional use cases  
Syntax: Dotted line **FROM** the extension, **TO** the main functionality
  * Dotted line (with arrow) from primary to secondary case 

## [Object Oriented Design](../object-oriented-design)
OO Design is a design approach where data is grouped and bound together in what is known as an object.

A _class_ is the blueprint - a sort of recipe - to what makes up an object.  
(ie: A cake recipe is the class, and an actual cake is an object)

**Components**

* _Attributes_ - the properties of the object
* _Behaviour_ - the methods of an object

The **state** of an object describes the value of an object.  
_Note: The words 'function' and 'method' are interchangeable, however methods are commonly used to describe a function that belongs to an object_  

**Properties of OO Design**

* Abstraction
  * Abstraction serves to generalise the attributes and behaviours of similar objects
  * Classes can inherit other classes, and gain the attributes and behaviours of the class they inherit
  * **Overriding** - Child classes can override the functionality of the parent class they inherit
* Encapsulation
  * Privatisation of an object's attributes, which is only accessible by the object itself
  * Attributes must be retreived through a public method

_Aside (not in course)_

* Polymorphism - ability for an object to act as a different data type depending on how it is used
* Overloading - ability for a method to take in different parameters  
(doesn't occur in Python as it is a dynamically typed language)

## [CRC Cards](../uml-domain-modelling/##crc-cards)
CRC cards are a physical tool in [OO design](../object-oriented-design) (usually written on sticky notes!) which help to identify the features of a class.

* **Class** - The name of the class
* **Responsbility** - What the class knows and can do
* **Collaboration** - Relationship to other classes

## [Class Diagram](../uml-class-diagram)
Class diagrams are a way to represent the attributes and behaviour of an object, and can also be used to model the relationship between objects.

|Name|Meaning|Symbol|
|:--:|:--|:--:|
|Inheritance|'Is a kind of'|&##x21E7;|
|Association|'Has a'|Solid line|
|Aggregation|'Contains' (optional)|&##9674;|
|Composition|'Composes' (integral)|&##9830;|

* Cardinality
  * One to One - 1:1
  * One to Many - 1:*
  * Many to Many - \*:*

## [Project Management](../project-management)

* Project Velocity - Rate of completed story points per iteration/sprint

## [Effective Software Design](../effective-software-design)

**Design Smells** are symptoms of poor design, which often occur when key design principles are violated

* Rigidity
* Fragility
* Immobility
* Viscosity
* Opacity
* Complexity
* Reptition

Good design will implement **low coupling** (interdependence of components), and **high cohesion** (how well components work together)

**The SOLID principles**

* Single Responsibility Principle - One reason for change
* Open Closed Principle - Code is open for extension, but should not need to be modified when extending behaviour

## [Databases](../databases)

* A **table** is a store of records
* A **record** is a group of data
* A **field** is an attribute of a record
* A **Primary Key** is a field which uniquely identifies a record
* A **Foreign Key** is a field which refers to the primary key of another record (usually in another table)

* Constraints
  * Databases implement constraints, which prevent invalid or incorrect data from being inserted into a table
  * Referential Integrity Constraint - The PK which a FK refers to must exist
  * Key Constraint - No duplicate attribute value (unless NULL)
  * Primary Key Constraint - No duplicate attribute value, and NULL not permitted

## [Entity Relationship (ER) Modelling](../entity-relationship-modelling)
ER Models help to model how data would be stored in a database.

|Meaning|Symbol|
|:--|:--:|
|Entity|&#9633;|
|Simple Attribute|&#9675;|
|Composite Attribute|Draw attributes like a tree|
|Multi-valued Attribute|&#9022;|
|Derived Attribute|&#9676;|
|Relationship|&#9826;|
|Weak Entity*|Double Box|
|Identifying Relationship*|Double Diamond|

* PK attributes are <u>underlined</u>
* Cardinality - "one" relationships are arrowed

**Participation** in a relationship refers to the "0/1 or more" existence of a relation.  
A **partial** participation means 0 or more.  
A **total** participation means 1 or more (at leat one relation has to exist) - drawn with a double or thick line)

**Weak** entities only exist due to an association with strong entities.
They have no key, and must be a total commitment to the relation

* Attributes can also exist in a relation

* Overlapping inheritance (A child entity can be both A and B)
* Disjoint inheritance (A child entity can be A or B, but not both)

<!-- ## Box Line Digrams -->

## [Software Architecture](../software-architecture)

* Client-Server Architecture

|Architecture|Description|Pros|Cons|Example|
|:--|:--|:--|:--|:--|
|Client Server|A client sends a request, and the server returns a response|Straightforward, scalable, easy to maintain|Single point of failure and congestion|Client computer browsing a website on a webserver|
|_n-tiered client server_|Components of a system is separated into both logical and physical parts, so they can be deployed on different systems|||Client browser, web server, database server|
|Peer to Peer|Each peer is both a client and a server. They contact other peers 'directly' and therefore do not need a central server<br><br>_But, who owns the data?_|Efficiency, scalability, robustness|Complexity, processing demand, resource availability|Torrenting clients|
|Pipe and Filter|Data is processed along a pipe and sent to subsequent 'filters' (processes)|Easy to understand, concurrency|Order-dependent, error handling|The Unix command shell|
|Repository|A centralised location for data to be accessed by many accessors|Easy to share large amounts of data, centralised management, integrity|?|The memory on your computer, SQL database|
|Publish Subscribe|Event-based subscription|-|-|Push notifications to your phone, web event handlers (ie `onClick`)|
|Service Oriented|Agnostic services that provide functionality|-|-|Third party services via an API|



---

# Python


* [Intro to Python](../intro-to-python)
* [Exceptions](../python-exceptions-and-exception-handling)
* [Testing with `pytest`](../python-testing-with-pytest)
* [Getter and Setters](../python-getter-setter-methods)

* [Flask Toolkit](../flask-toolkit)
* [Submitting Data to Flask](../submitting-data-to-flask)

* [Session Storage](../session-storage)

* [Useful Git commands](../git-cheatsheet)
