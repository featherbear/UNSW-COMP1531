---
title: "Effective Software Design"
date: 2019-04-02T16:17:42+11:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Design Smells

Design smells are a symptom of poor design, often caused by violation of key design principles.

* Rigidity - software is too difficult to change even in simle ways

* Fragility - Tendency of the software to break in many places when a single change is made

* Immobility - hard to reuse

* Viscosity - Changes are easier to implement through 'hacks'

* Opacity - Difficult to understand

* Needless Complexity

* Needless Repetition

# Good Design

* Coupling - Interdependence between components or classes

* Cohesion - How well the components work together

# SOLID
## Single Reponsibility Principle
Class should have ONE reason to change

+ Readability
+ Reusability
+ Testability

## Open-Closed Principle
**Open** - Program is open to modifications  
**Closed** - Extension of the behaviour should need to modify the internals

Applying OCP reduces rigidity, and is achievable by abstracting functionality

Dynamic Binding - At runtime Python is able to determine what type a variable is.

<!-- **Polymorphism** - Different methods depending on type -->

# Model-View-Controller (MVC)

## Model
Holds the data, state, and methods of a data structure
Responds to changes from the controller

## View (Observer)
Presentation layer (Representation of the model)

## Controller
... the controller...?