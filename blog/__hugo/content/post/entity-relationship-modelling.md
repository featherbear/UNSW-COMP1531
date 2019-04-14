---
title: "Entity Relationship Modelling"
date: 2019-04-13T15:14:07+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

Aside: Big Data
---
Big Data refers to (a lot of) data of different types that can be analysed to provide insights.

The three V's of Big Data are:

* **V**olume - The amount
* **V**elocity - The rate
* **V**ariety - The types

Originally - to store data, the common SQL approach was adopted. However when requiring to store datatypes of different and complex types, other standards such as NoSQL (Not-Only SQL) came to arise

Aside: Databases
---

**DBMS** - **D**ata**b**ase **M**anagement **S**ystem  
**DDL** - **D**ata **D**efinition **L**anguage _[schemas]_  
**DML** - **D**ata **M**anipulation **L**anguage _[transactions]_

Types of Databases:  
* OO Model - OODBMS
* Relational Model - RDBMS - ie Oracle, MySQL, SQLite
* DOM Model - ie JSON, XML - ie MongoDB


# Entity Relationship Modelling
ER Modelling is another way to describe the relationship between data objects

## Entity Sets
Entity Sets describe the type of an entity.

&#9633; Square - **Entity name**  
&#9675; Circle - **Simple attribute**  
&#9022; Double Circle - **Multi-valued attribute** _[ie array]_  
&#9676; Dotted circle - **Derived attribute** _[uses other attributes]_  
**Composite attributes** are drawn like a subtree  
**Primary Keys** are underlined
Straight lines connect these different items together

**Diamond** for relationship

_**Candidate Keys** are the possible attributes that are can uniquely identify one entity from another.  
**Super Keys** are composite candidate keys where a removal of one of the attributes will still uniquely identify it  
An entity's **Primary Key** is the chosen candidate key_

![](Snipaste_2019-04-13_15-18-20.png)

**Cardinality**  
1:1, 1:M, M:M  
They can also be represented with lines and arrows (single arrow from the relator to the 'one' relationship)

**Level of Participation**  
Partial Participation - 0 or more  
Total Participation - 1 or more (Draw with two lines, or a thick line)

## Entity Instances
Most similar to object instances, entity instances are actualisations of a entity set.

No two entity instances can share the exact same attribute values. (Whereas object instances can)
