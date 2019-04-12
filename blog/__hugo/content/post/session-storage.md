---
title: "Storing website data"
date: 2019-04-09T16:22:17+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

> The HTTP protocol is **stateless**, meaning that requests are independent from each other, and hence there is no sort of data persistance. There is a need to store and transmit data, and it can be achieved in several ways

# Client Side Storage
## Cookies
Cookies are data elements that are stored on the client.  
Each time a request is made, all the cookies are sent to the server.  

Cookies have a 'lifetime' - that is, they expire after a certain time.

### Flask
```python3
@app.route("/doSomething")
def something():
  return request.cookies["name"]
```

#### Secure Cookies in Flask
Because cookies are insecure (they can be easily tampered), Flask provides a mechanism to securely stored data - using Flask's `session` feature

_Note_: The session is just an encrypted cookie with the name `session`

**Setup**  
1) Import session  
`from Flask import session`  
2) Set up the secret key (the encryption key)  
`(app:Flask).secret_key = YOUR_SECRET_KEY`

In your request context, you can then treat `session` as a dictionary.
```python3
@app.route("/blah")
def someRouteFunction():
  return session["name"]
```

## JavaScript - localStorage
The drawback to cookies, is that all the cookies are sent to the server.  
_i.e When writing a web app, there may be security and privacy concerns about transmitting confidential user data._

`localStorage` is bound to the domain name of the website, and exists for an infinite lifetime.

`localStorage.get(key)`  
`localStorage.set(key)`  
`localStorage.clear()`

## JavaScript - sessionStorage
For non-persistent storage (ie data that gets destroyed when the page is closed), there exists `sessionStorage`

`sessionStorage.get(key)`  
`sessionStorage.set(key)`  
`sessionStorage.clear()`


# Server Side Storage
We can also store session information on the server, which involves each client being mapped to a key in the server