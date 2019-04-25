---
title: "Quiz 03"
date: 2019-04-24T14:00:00+10:00
categories: ["Assessments"]
hiddenFromHomePage: false
postMetaInFooter: false
flowchartDiagrams:
  enable: false
  options: ""
sequenceDiagrams: 
  enable: false
  options: ""
---

> Disclaimer: These are my answers, not official answers. Also multiple choice questions suck.

# Question One
In relational model terminology, a table is considered as:

a) range  
**b) relation**  
c) domain  
d) tuple  

# Question Two
Which of the statements below best describes the scenario depicted in the ER model below? 
![](Picture1.png)

a) Every graphic designer must create a poster, and a poster must be judged by a judge  
**b) Every poster must be associated with one or more graphic designers and a poster must be judged by one or more judges**  
c) A graphic designer may or may not design a poster. Every judge must judge at least one poster  
d) Every poster must be associated with one or more graphic designers but a poster may or may not be judged by a judge  

# Question Three
If you were designing an email system like Gmail where all incoming mails are scanned for different security checks at different levels one after another. Each security level implements its own security check and is dependent on input from the previous levels

a) n-tiered client server  
**b) pipe and filter**  
c) shared repository style architecture  
d) event driven architecture  

# Question Four
Choose the in-correct statement of the following.

a) The basic building block of SOA is the service  
b) Web services are a preferred and popular realisation of SOA  
**c) SOA emphasises implementing software modules with the same technology**  
d) SOA is typically used in B2B applications  
e) SOA is ideal to wrap legacy software as reusable services

# Question Five
A company releases a new software, and allows the customer to register for a “free-trial” period. The company wishes to build an automated application, that tracks customer’s free trial registrations and at the end of the free trial period, if the customer has not notified through email to cancel the “free trial”, the application should automatically renew the customer’s license for a period of 12 months and accordingly charge the customer’s credit card. Which style of architecture would best suit to implement the above application? The credit-card payment service is provided by a third-party service provider.

a) P2P  
b) Publish Subscribe  
**c) Service Oriented Architecture**  
d) Pipe and Filter  
e) A web-based client-server architecture based on a HTTP request/response

# Question Six
Which of the following statements is incorrect?

a) A traditional Pipe and Filter architecture has poor fault tolerance, as the entire pipe-line crashes if one filter crashes  
b) P2P networks are the cheapest method of distributing content because they use the bandwidth of peers, not the bandwidth of the content’s creator.  
c) An email server is an example of client-server architecture  
**d) MVC architecture and 3-tier client-server architecture imply the same architectural style**  

# Question Seven
The relational schema for two tables are given as:

Customer : { client_id: integer, client_name: varchar, age: integer}  
Investment: { property_id:integer, property_address: varchar, market_value: float , client:integer }  

The relation Investment has an attribute client which must refer to a valid client_id in the relation Customer  

This is an example of:

**a) Referential Integrity constraint**  
b) Domain constraint  
c) Key constraint  
d) Primary Key constraint  

# Question Eight
Which of the following statements is incorrect about a relation in the relational data model?

a) A relation can be used to model an entity-set in the ER model  
**b) Every relation has a primary key**  
c) A relation can also be used to model relationship sets  
d) Attributes in a relation can be atomic or composite  
e) An instance of a relation is a set of tuples of attribute values

# Question Nine
![](Picture2.png)
![](Picture3.png)

The relational model above represents:

**a) ER-style mapping for a class hierarchy**  
b) OO-style mapping for a class hierarchy  
c) Single-table style for a class hierarchy  
d) None of the above

# Question Ten
Which of the following statements is incorrect about an ER model?

a) A hobbies attribute for a Student entity-set has values = {diving, tennis}. This is an example of a multi-valued attribute  
b) A weak entity-set does not have a primary key  
c) An entity-instance in an ER model is similar to an object instance and an entity-set is similar to a class  
**d) In an ER model, two entity-instances can have the same set of attribute values**
