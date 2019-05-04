---
title: "Databases; Box-Line Diagrams"
date: 2019-04-17T14:37:42+10:00

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


# Relational Databases 


# Terms
Each group of data is called a **record**  
Each attribute in the record is known as a **field**  

A Primary Key is a unique identifier  
A Foreign Key is a field that references a primary key of another table

# Constraints
Constraints protect the data being inserted into a table, to prevent invalid data from being stored

## Domain Constraint
Values must match their type, must be present, etc

## Referential Integrity Constraint
"A restraint on the integrity of the reference"  

When a record is created, if a foreign key field is present, the value of that field must exist as a primary key of the referenced table.  
(X must exist as a primary key in a table if another table)

## Key Constraint
No two records can have the same value for a specific field unless they are NULL

## Primary Key Constraint
No two records can have the same value for a specific field, and NULL is not permissible


# Effective Database Design Principles
## Multi-valued Attributes
In SQL databases, there exists no such _multi-value_ attribute type, which makes holding arrays of data slightly more difficult.  
_(Other databases like MongoDB and NoSQL have multi-value attributes, so crisis averted!)_

We might originally have a table like

|ID|Name|Hobby 1|Hobby 2|Hobby 3|Hobby 4|...|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|1|Andrew|Sports|Photography|Programming|Music|...|

But this is bad as it will use alot of data for each record.  Consider if someone else only had one hobby, their Hobby 2, 3, 4, ... would be empty - but space will still be reserved for those fields!

Or something like 

|ID|Name|Hobby|
|:--:|:--:|:--|
|1|Andrew|Sports,Photography,Programming,Music|

This is slightly better, but still not the best, as data of the field `Hobby` needs to be parsed outside of the database.  
Consequently, we are unable to search for people who like "Sports" by using just the database

A better approach would be to create a second table (many-to-many), which links each person with their hobbies

|<u>**ID**</u>|Name|
|:--:|:--|
|1|Andrew|

|_ID_|Hobby|
|:--:|:--|
|1|Sports|
|1|Photography|
|1|Programming|
|1|Music|
