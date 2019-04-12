---
title: "Submitting data to Flask with HTML Forms"
date: 2019-04-10T18:05:21+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams:
  enable: false
  options: ""
---

_**Disclaimer**: This page is entirely static and does not interact with any server, all client-server interactions are purely simulated_

---

<script type="text/javascript">
location.query = {};
(function() {
  let queryIndex = location.href.indexOf("?");
  if (queryIndex > -1) {
    for (let keyPair of location.href.replace(location.hash,"").substr(queryIndex+1).split("&")) {
      keyPair = keyPair.split("=");
      location.query[keyPair[0]] = keyPair[1];
    }
  }
})();

function applyQuery() {
  if (location.query.name && location.query.age) {
    for (let elem of document.getElementsByClassName("name")) elem.innerText = location.query.name;
    for (let elem of document.getElementsByClassName("age")) elem.innerText = location.query.age;
  }
};

let checkPoint = 0;
function applyCheckpoint() {
  if (checkPoint) document.getElementById("anchor" + checkPoint).scrollIntoView();
}
</script>

<style>
form {
  background-color: rgba(127,127,127,0.05);
  padding: 20px 0;
}
form:hover {
    background-color: rgba(127,127,127,0.1);
}

input, button {
  display: block;
  height: 50px;
  width: 90%;
  margin: 0 auto;
  border: none;
}
input::placeholder {
  -webkit-transform: translateY(0px);
  transform: translateY(0px);
  -webkit-transition: .5s;
  transition: .5s;
}
button {
  -webkit-transition: .3s;
  transition: .3s;
  width: 93%;
  background-color: rgba(127,127,127,0.2)
}
button:hover {
    color: #ff5722;
}
input:hover, input:focus, input:active:focus {
  color: #ff5722;
  outline: none;
  border-bottom: 1px solid #ff5722;
}
input:hover::placeholder, input:focus::placeholder, input:active:focus::placeholder {
  color: #ff5722;
  position: relative;
  -webkit-transform: translateY(-20px);
  transform: translateY(-20px);
}

input[name=name],
input[name=age] {
  position: relative;
  z-index: 1;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  padding-left: 20px;
  font-family: 'Open Sans', sans-serif;
  color: #858585;
  font-weight: lighter;
  -webkit-transition: .5s;
  transition: .5s;
}
</style>

# HTML Forms
<form id="form1">
  <input type="text" name="name" placeholder="What's your name?" required>
  <br/>
  <input type="number" name="age" placeholder="How old are you?" required>
  <br/>
  <button type="submit">Submit</button>
</form>

The source code of this HTML form looks like:

```html
<form>
  <input type="text" name="name" placeholder="What's your name?" />
  <input type="number" name="age" placeholder="How old are you?" />
  <button type="submit">Submit</button>
</form>
```

<script type="text/javascript">
function submitForm(formID, forceBool) {
  var elem = document.getElementById(formID);
  if (forceBool || elem.reportValidity()) elem.submit();
}
</script>

{{% admonition note "Try It!" %}}
Write your name and age into the above form.  
When you press the [**Submit**](<javascript:submitForm(\'form1\')>) button, have a look at the URL!
{{% /admonition %}}

<style>
.name, .age {
  font-weight: bold;
}
</style>

<div id="checkPoint1" style="display:none">
</br></br><hr><div id="anchor1"></div></br></br></br>
Hey there, <span class="name"></span>!</br>
You're apparently <span class="age"></span> years old!!!
</br></br></br><hr></br></br></br>
</div>

<script type="text/javascript">
if (location.query.name && location.query.age) {
  document.getElementById("checkPoint1").style.display="initial";
  checkPoint = 1;
}
</script>

<br><br>
## Forms using GET

Have a look at the address bar - We can see the data that we just submitted.  
This type of form submission uses a `GET` request

Great, **_or is it..._**

{{% admonition note "Try It!" %}}
Modify the <code>?name=<span class="name"></span>&age=<span class="age"></span></code> portion of the URL and change the name!
{{% /admonition %}}

Submitting form data via a GET request is somewhat insecure, as it allows the client to easily tamper with the data. _(It also makes the URL look yucky!)_

&nbsp;  

Instead, what we can do is change our form to use the `POST` request method!!!

<br><br>

## Forms using POST

<form method="POST" id="form2">
  <input type="text" name="name" placeholder="What's your name?" required>
  <br/>
  <input type="number" name="age" placeholder="How old are you?" required>
  <br/>
  <button type="submit">Submit via POST</button>
</form>

<script type="text/javascript">
  document.getElementById('form2').addEventListener('submit', function(evt) {
    if (evt) evt.preventDefault();
    history.replaceState(null,null,".");
    if (this.reportValidity()) {
      location.query.name = this.name.value;
      location.query.age = this.age.value;
      this.name.value = "";
      this.age.value = "";
      document.getElementById("checkPoint2").style.display="initial";
      applyQuery();
      checkPoint = 2;
      applyCheckpoint();
    }
  })
</script>


The HTML code follows the standard form convention, but with a `method="POST"` attribute in the `<form>` tag:

```html
<form method="POST">
  <input type="text" name="name" placeholder="What's your name?" />
  <input type="number" name="age" placeholder="How old are you?" />
  <button type="submit">Submit via POST</button>
</form>
```

{{% admonition note "Try It!" %}}
Write your name and age into the above form.  
Then press the [**Submit**](<javascript:submitForm(\'form2\')>) button!
{{% /admonition %}}

<div id="checkPoint2" style="display:none">
</br></br></hr></br><hr></br></br></br>
<div id="anchor2"></div>
Hey there, <span class="name"></span>!</br>
You're apparently <span class="age"></span> years old!!!
</br></br></br></br><hr></br></br></br>
</div>

This time, there's no data in the URL - rather the data was sent to the server via a `POST` request!

<script type="text/javascript">
applyQuery();
applyCheckpoint();
</script>

<br><br>
# Forms and Flask
## Handling GET
To retrieve the query arguments in Flask  

1) Import the request proxy  
`from flask import request`

2) Access the data  
`request.args`

***Example***
```python3
@app.route("/hello/", methods=["GET"])
def greetingGET():
  # validate(request.args) # Check that the arguments are valid
  return f"""Hey there, {request.args['name']}!<br>
             You are supposedly {request.args['age']} years old!"""
```
## Handling POST
To retrieve the post data in Flask  

1) Import the request proxy  
`from flask import request`

2) Access the data  
`request.data`  
_(Make sure your route decorator has `POST` in its method scope!)_

***Example***
```python3
@app.route("/hello/", methods=["POST"])
def greetingPOST():
  # validate(request.data) # Check that the data is valid
  return f"""Hey there, {request.data['name']}!<br>
             You are supposedly {request.data['age']} years old!"""
```

<br><br>
# Use Cases
## Keeping submitted data
If you noticed in the above forms...  
When you pressed the [Submit](javascript:) button, after the page loaded with the response - **your form was empty**!

This is because HTTP is a stateless protocol, each request doesn't know about any other request.  
As a result, the response webpage will not be able to know the submitted data... **_unless_** we make it so

This can easily be done with Flask's `render_template` function, where we can pass the submitted form data back into the webpage!

Refer to this [file from the week 7 / 8 lab](https://github.com/featherbear/UNSW-COMP1531/blob/6843ca5d5123b0cdf917110aeedb2ac972b465c4/Labs/lab07_08_featherbear/templates/booking_form.html#L56)...

<u>**Example**</u>
```python3
from flask import request, render_template # ...
###

@app.route("/hello", methods=["GET", "POST"])
def helloMULTI():
  if (request.method == "GET"):
    data = request.args
  else: # request.method == "POST"
    data = request.data

  name = data["name]
  age = int(data["age"])
  ageIsEven = age % 2 == 0

  return render_template("hello.html", name = name, age = age, isEven = ageIsEven, formData = data)
```
```html
<form>
  <input name="name" {% if formData["name"] %}value={{formData["name"]}}{% endif %}>
  <input age="age" {% if formData["age"] %}value={{formData["age"]}}{% endif %}>
</form>
Hey there, {{name}}!!
You are {{age}} years old, which is an {{"even" if isEven else "odd"}} age!
```

<br>
<u>**Demo**</u>
<form id="form3" method="POST">
 <input type="text" name="name" placeholder="What's your name?" required>
 <input type="number" name="age" placeholder="What's your age?" required>
 <button type="submit">Submit</button>
</form>

<div id="form3_output" style="display:none">
  <br><u><b>Output</b></u><br>
  <div class="content">
    Hey there, <span class="name"></span>!!<br>
    You are <span class="age"></span> years old, which is an <span name="isEven"></span> age!
  </div>
</div>

<script type="text/javascript">
  document.getElementById('form3').addEventListener('submit', function(evt) {
    if (evt) evt.preventDefault();
    history.replaceState(null,null,".");
    if (this.reportValidity()) {
      location.query.name = this.name.value;
      location.query.age = this.age.value;
      document.querySelector("[name=isEven]").innerText = Number(location.query.age) % 2 == 0 ? "even" : "odd";
      document.getElementById("form3_output").style.display="initial";
      applyQuery();
    }
  });
</script>

<br><br>
## Client-side validation
It is good practice to also validate form data on the client-side **as well as on the server-side**!  

_(Note: Server-side validation is a **MUST**, regardless if you have client-side validation or not)_

To do such, you can add the `required` attribute to your `<input>` tags.  
For example: `<input type="number" name="age" required>`  

This prevents the browser from submitting the form unless the input is filled, _and_ has valid content corresponding to the input `type`

(In fact, all the forms on this page already have this attribute added!)