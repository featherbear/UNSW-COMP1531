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

# Fixtures
If you have code which produces an object that runs for several tests, you can group them into a fixture
```python3
@pytest.fixture
def mySystem():
  # do stuff
  sys = SomeSystemThing()
  sys.setValue(7)
  return sys

def test_checking(mySystem):
  # Fixture name here ^^^^
  assert mySystem.check() == True
```

# Setup and Teardown
Another way to rerun the same piece of code multiple times is through a setup and teardown procedure.  

Consider this excerpt from [StackOverflow](https://stackoverflow.com/a/40558283)
```python3
lh = <got log handler from logger module>

class TestClass:
    @classmethod
    def setup_class(cls):
        lh.info("starting class: {} execution".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        lh.info("starting class: {} execution".format(cls.__name__))

    def setup_method(self, method):
        lh.info("starting execution of tc: {}".format(method.__name__))

    def teardown_method(self, method):
        lh.info("starting execution of tc: {}".format(method.__name__))

    def test_tc1(self):
        <tc_content>
        assert 

    def test_tc2(self):
        <tc_content>
        assert
```

> Now when I run my tests, when the TestClass execution is starting, it logs the details for when it is beginning execution, when it is ending execution and same for the methods..
