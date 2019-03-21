---
title: "Python - Testing With `pytest`"
date: 2019-03-18T13:23:51+11:00

categories: ["Python"]

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

`pytest` is a Python testing framework to check that your code is doing what they should!


```python3
# Imports here
import pytest

class TestUS1():
  def test_normal_use(self):
    pass
    
  def test_no_items(self):
    pass
    
  def test_one_item(self):
    pass
```

* Any python files that start with `test_` or end with `_test` are included by pytest
* Any class that starts with `Test` are included by pytest
* Any method that starts with `test_` are executed by `pytest`

# Testing for Exceptions
```python3
with pytest.raises(ExceptionName):
  doSomethingThatRaisesAnException
```

# Setup and Teardown
 