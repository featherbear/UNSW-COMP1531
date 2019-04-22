---
title: "Assignment - GourmetBurgers"
date: 2019-03-04T09:07:16+11:00

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

> Demo Site | [featherbear.github.io](https://featherbear.github.io/UNSW-COMP1531-Assignment/)  
> GitHub | [featherbear/UNSW-COMP1531-Assignment](https://github.com/featherbear/UNSW-COMP1531-Assignment)   

Over the course of this semester, I had a group assignment to implement an online ordering system for a ficticious company, 'GourmetBurgers'.  
The backend had to be written with Python, and Flask.


![System diagram](20190401_144906.png)


We used Trello to manage our TODO list
![Trello task backlog](Snipaste_2019-03-30_15-08-47.png)

---

# Screenshots

![Homepage](view_home.png)
<video style="max-width: 760px" src="view_menu.mp4" autoplay loop muted></video>
![Customise Modal](view_customise.png)
![Order Review / Checkout](view_checkout.png)
![Order Status](view_order.png)
![Staff Order Dashboard](view_order_some.png)
![Staff Inventory Dashboard](view_inventory.png)


---

# Diagrams

## CRC Card
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/crc%20cards.v2.png)

## Class Diagram
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/class%20diagram.v2-extended.png)

## Use Case Diagram
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/use%20case%20diagram.png)

## Velocity Chart
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/velocity%20chart.png)

## Database Schema
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/database%20schema.png)

## Entity Relationship Diagram
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/entity%20relationship%20diagram.png)

## Website Design Mockups
![](https://github.com/featherbear/UNSW-COMP1531-Assignment/raw/master/docs/site%20design%20storyboard.png)

---

# Progress Log
|`27/02/19`|
|:--|
|Facebook group chat created to allow for online communication|

|`4/03/19` - Standup Meeting One|
|:--|
|Each member was requested to write their own user stories<br>They would then be merged with the other members' stories|
|**Outcomes**<br>- `06/03/19` Submit invididual user stories<br>- `07/03/19` Merge user stories<br>- `09/03/19` Deadline to submit user stories|

|`6/03/19`|
|:--|
|_Deadline for team members to submit their individual user stories_|

|`7/03/19`|
|:--|
|Each individual's user stories were merged together|
|Team decided not to implement a payment feature in the system.<br>Changed in favour of a '*Click and Collect*' model where customers will physically pay on collection of their order.|

|`8/03/19`|
|:--|
|User stories were reviewed by all team members.|
|Created [Website design storyboard](site design storyboard.png)|

|`9/03/19` - Milestone One|
|:--|
|_User stories submitted_|
 
|`12/03/19`|
|:--|
|Created SQL database schema (v1)|

|`16/03/19`|
|:--|
|Created Trello board for task assignment to team members|

|`18/03/19` - Standup Meeting Two|
|:--|
|Tasks on Trello were delegated to each team member|
|Rewrote [database schema (v2)](docs/database schema.png)|
|**Outcomes**<br>Andrew: Refactor code to conform to OO principles|

|`21/03/19`|
|:--|
|Created [CRC Cards (v1)](docs/crc cards.v1.png) and [Class Diagram (v1)](docs/class diagram.v1.png)|
|Implemented inventory provider server functionality|

|`21/03/19`|
|:--|
|Created [Use Case Diagram](docs/use case diagram.png)|

|`24/03/19`|
|:--|
|Created website homepage|

|`25/03/19` - Standup Meeting Three|
|:--|
|Group reviewed and decided to rewrite the CRC Cards and the Class Diagram|
|**Outcomes**<br>Andrew: Website homepage, Website browse page<br>Tong: Create inventory, Staff Order Dashboard<br>Catherine: Create inventory, Customer Order Status|


|`28/03/19`|
|:--|
|Created website browse menu page|
|Created class models|
|Updated user stories|
|Create raw inventory data|
|Tong: Started on Staff Order Dashboard webpage|

|`30/03/19`|
|:--|
|Create [CRC Cards (v2)](docs/crc cards.v2.png) and [Class Diagram (v2)](docs/class diagram.v2-extended.png)|

|`1/04/19` - Standup Meeting Four|
|:--|
|**Outcomes**<br>Tong: Write `pytest` for MenuItem<br>Catherine: Write the `pytest` for Ingredient, implement GBSystem functionality for ingredient updating<br>Andrew: Work on front-end|

|`4/04/19` - Standup Meeting Five & Collaborating Coding Session|
|:--|
|Updated user stories|
|User Story One completed|
|User Story Three completed|
|Tong & Catherine: Write `pytest` for Ingredient, MenuItem and Order|

|`5/04/19`|
|:--|
|Tidy up `pytest` files|
|Create `pytest` for GBSystem, and for user stories|

|`11/04/19` - Standup Meeting Five|
|:--|
|Team reviewed the additional requirements and concluded that there were no changes needed in the user stories, as the Customise / Add to Cart feature was already part of the initial implementation|
|**Outcomes**<br>Andrew: Update the database to include Sundaes|

|`13/04/19`|
|:--|
|Andrew: Updated database to include new client specification|
|Tong: Finished staff order dashboard|
|Tong: Finished order complete page|

|`14/04/19`|
|:--|
|User Story Seven completed|


|`15/04/19`|
|:--|
|User Story Six completed|

|`20/04/19`|
|:--|
|Tong: Finished staff inventory dashboard|
|Catherine: Finished item customise page|

|`21/04/19`|
|:--|
|User Story Two completed|
|User Story Four completed|
|User Story Five completed|
|User Story Eight completed|
|**All tasks completed! :)**|