---
title: "[UML] Use Case Diagram"
date: 2019-03-09T21:27:22+11:00

categories: ["UML", "Behaviour Diagrams"]
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

Each solid line represents an interaction between an actor and the system  
Each dotted line represents an interaction between a use case and another use case

# Actors
Actors are the objects that interact with the use cases.  
They can be either **initiators** or **participants**

--- 

## Interactions
# \<\<initiates>>
Usage: For actors that call a use case
Syntax: Solid line between actor and the use case

# \<\<participates>>
Usage: For actors that are involved in a use case
Syntax: Solid line between actor and the use case

# \<\<includes>>
Usage: For required use cases  
Syntax: Dotted line FROM the use case, TO the use case that is included

# \<\<extends>>
Usage: For optional use cases  
Syntax: Dotted line FROM the extension, TO the main functionality

Dotted line (with arrow) from primary to secondary case 

