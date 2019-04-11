# Lab 08 (Due Week 8, Sunday, 14th April 11:59 pm) (10 marks)

# Aim
1. Learn Flask and Jinja templating 
2. Develop skills to build a Flask frontend for an existing backend code

# Lab Instructions

In this lab, you will continue your work from lab06 and build the frontend for the app using Jinja and Flask routing. To get started, import the lab code from: [https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/labs).

This lab must be completed **individually** and uploaded to GitHub by Sunday, end of Week 08.

# Important Note
For this lab, the only files you will need to make changes to are `routes.py` and the provided `html` files. In fact, you will only need to make changes to a single function in `routes.py` and only two of the html files, namely `booking_form.html` and `booking_confirm.html`.

As such, large portion of the booking system has already been implemented for you, and your lab can be completed rather easily by analysing the starter code. Please feel free to take away any part of this lab's code for your group project if you think it is beneficial to do so.

However, in order for you to complete the lab succesfully, you will need a **thorough understanding of the backend code** as well as the rest of the starter code. We highly recommend you to **analyse every bit of it before start coding**. Please also note that there has been major changes to the backend code since the last week's lab, especially with regards to the input validation logic.

Furthermore, to fully understand the starter code and start coding in Flask + Jinja, it is also essential that you **watch through all of the** [Flask tutorial videos](https://www.youtube.com/watch?v=-B3_Uo_Qtqw&list=PLbSaCpDlfd6qTRiRQFIkCDU7RbAmk_sIR)  **by Hussein**


## Familiarise yourself with the Flask App

0. First off, setup a virtual environment & install Flask:
	```bash
	cd your_git_repo_name
	virtualenv --python=python3 venv # Create the venv folder in the current directory.
	. venv/bin/activate # Activate the virtual environment.
	pip3 install -r requirements.txt # Install dependencies in the virtual environment.
	export FLASK_APP=run.py # Set the file to execute when starting a Flask app
	```
	(instead of `pip3 install -r requirements.txt`, you can just do `pip3 install flask` to download the latest version of Flask)

 1. In order to launch the app, run the following command in the terminal: `flask run`
 2. Open up your favourite browser and type `localhost:5000` inside its URL bar, then press ENTER
 3. You should now see a search page that looks like this:
![enter image description here](https://lh3.googleusercontent.com/3seK0dFBYmAgIRwE5SEnGUlP5PrcZELr-5UEfYSfUy04onPC3kFUXYmryQ-qHt0s1XlDw6UamHc=s800) 
4. Feel free to play around with the app's search feature (which has already been implemented for you) before proceeding to the next step
5. If you click on one of the cars on the search result, the app will take you to another page consisting of two buttons: "BOOK!" and "See all bookings". Clicking on the second button will display a list of all bookings made for the selected car, but this will be empty since you haven't booked any cars yet.
6. Click on "BOOK!" to bring up a booking form and initiate a booking process
7. Uh-oh, the page is missing the booking form! Yes, that's because it's what you are going to be implementing in this lab :)

## Task: Build Frontend for "Make a Booking"
This lab only consists of a single task, that is, building the frontend and the route for the use-case "Make a Booking".

 - Analyse the starter code and implement the route `@app.route('/cars/book/<rego>', ...)`. Further instructions have been provided inside the function to assist you in completing this task.
 - Modify the files `booking_form.html` and `booking_confirm.html` to display the necessary pages correctly.

Please see the attached snapshots of what your final solution may look like:

1. Initial appearance of `booking_form.html`:
![enter image description here](https://lh3.googleusercontent.com/tzl0NmMRNVWRVr1Z8lUejCChK9ASzZp2d47JjJwfzMNVh8M8t70zueCbebq0f1M4USlrdsLAh5w=s390)

2. "Check Booking" button is clicked when some of the fields are still blank
![enter image description here](https://lh3.googleusercontent.com/K8Wd_atY47Ea-20-OnShN-XQhl2AHRUzV7gwixGTXm1413kNd2keIF5lPKm6C8Au1Tg6hCqA6XI=s460)

3. "Check Booking" button is clicked after providing an invalid rental period
![enter image description here](https://lh3.googleusercontent.com/HQT6FTp5K8VgTaX050DxQ5YT7qusuZXcAsh_FxqC1FfEmH1LUWaGa3mBEWyr8mWvfCZPz8tJZdE=s400)

4. "Check Booking" button is clicked when all inputs are valid![enter image description here](https://lh3.googleusercontent.com/3EPc7bLX0vjIUTVx1tRwjA0h04Xx3BjO1mluPYovQHoDG63UWp4emNW62uxr0mcjSVqlk4lkwUU=s430)

5. `booking_confirm.html` page is displayed after clicking the "Confirm" button
![enter image description here](https://lh3.googleusercontent.com/OABLj-QkaJY1ntcr3Ajsnqaw270aytf9W1UpSvPF1VlSFM_Zz2OYRT7kp18CWTYIfOxbdSsWYTc=s500)
