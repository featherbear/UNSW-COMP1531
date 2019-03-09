---
title: "Introduction to Python"
date: 2019-02-20T14:54:44+11:00

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

Python is a

* **dynamically typed** language - variable types are assigned at runtime
* **Interpreted language** - code is compiled and executed line by line 
* **Strongly typed** - No type coercion


&nbsp;  

Python gives us high level functions and operations to do things that might take 10-15 lines in C.

_In the interpreter..._  
Unless defined, the `_` character keeps the result of the last value

_Fun fact: Python was written in C_

---

# String Indexing
`your_string = "hello"`

We can extract part of a string FROM an index to the end  
> `your_string[2:] == "llo"`

We can also extract part of a string FROM an index TO a limit (not including the limit index)  
> `your_string[1:4] == "ell"`

We can step every `n` elements of a string  
> `your_string[::2] == "hlo"`

We can extract part of a string, and also step  
> `your_string[0:4:2] == "hl"`

We can reverse a string with a negative step  
> `your_string[::-1] == "elloh"`

# (Im)mutability
Strings are immutable (cannot change a letter by its index)
```python
string_variable = "Hello, World!"
string_variable[1] = "Z"
# TypeError: 'str' object does not support item assignment
```

Lists are mutable though!
```python
string_variable   = "Hello, World!"
list_of_string    = list(string_variable)
list_of_string[1] = "Z"
"".join(list_of_string)
# HZllo, World!
```
