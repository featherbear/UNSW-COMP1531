---
title: "Flask Toolkit"
date: 2019-02-19T16:36:00+11:00

categories: ["Info"]

description: ""
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Basic application code
```python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

# Routing
```python3
@app.route(...)
```
Browsers automatically append a trailingslash (canonical URL).  
If the route does not end with a trailing slash, a client accessing a canonical URL will receive a 404

POST requests
```python3
@app.route(..., methods=["POST"])
def func():
  ...
```


#Variable Rules
```python3
@app.route('/path/<VARIABLE_NAME>')
def someFunc(<VARIABLE_NAME>):
    return <VARIABLE_NAME>
```

@app.route('/path/<CONVERTER_TYPE:VARIABLE_NAME>')
def someFunc(<VARIABLE_NAME>):
    return <VARIABLE_NAME>
```

|Converter Type|Description|
|:--|:--|
string|(default) accepts any text without a slash
int|accepts positive integers
float|accepts positive floating point values
path|like string but also accepts slashes
uuid|accepts UUID strings

# Static Files
```python3
url_for('static', filename=<FILENAME>)
```
Store files in the `static` directory


# Template Rendering

Templating uses Jinja2 as the processor
Store templates in the `templates` directory

## Accessing `request` data
```python3
from flask import request

POST -> request.form[<KEY>]  
REQ  -> requests.args.get(<KEY>, <DEFAULT>)
FILE -> request.files[<KEY>]
```

## Cookies
Set cookies -> `<response>.set_cookie(<KEY>, <VALUE>)`  
Get cookies -> `request.cookies.get(<KEY>)`


# Redirect
`flask.redirect(<PATH>)`

# Errors
`flask.abort(<STATUS_CODE>)`

# Error Handlers
```python3
@app.errorhandler(<STATUS_CODE>)
def func(error):
  return ..., <STATUS_CODE>)
```

# Session Management
```flask.session`
Session is stored INSIDE the client's cookies (encrypted with the secret key)

$ python -c 'import os; print(os.urandom(16))'
b'_5#y2L"F4Q8z\n\xec]/'

# Message flashing
Putting data created from one response into another request (ie to write 'successful login')
# Deferred Request Callbacks
We can write functions that will execute before (and) after a was reached

Apply the `@<app>.before_request` decorator onto the function

Apply the `flask.after_this_request` decorator onto a function that is defined inside