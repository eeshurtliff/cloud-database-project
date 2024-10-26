## Overview

**Project Title**:Tennis Clinics Database

**Project Description**: This is a database that keeps track of the students and details of a coach's tennis clinics through a Firebase Database and python code. 

**Project Goals**:
* Create the Firestore Database and learn how to add to it. 
* Connect python to the Firestore Database
* Query from the Database
* Update parts of the database.
* Add documents to the database
* Delete documents from the database. 

## Instructions for Build and Use

Steps to build and/or run the software:

1. Have python version 3.10 installed; 3.12 does not work with Firebase
2. acquire a key from the database to be able to connect the python file to the database
3. Run the python code. 

Instructions for using the software:

1. Run the code
2. Choose an option from the main menu in the terminal.
3. Follow the prompts from there to look at and edit things from the database. 

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* I am using python version 3.10.11 for this project. The more recent versions do not work with the firebase library. 
* Install the library firebase_admin with the terminal command 'py -m pip install firebase_admin'. 
*

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Initialize Cloud Firestore: ](https://firebase.google.com/docs/firestore/manage-data/add-data#python) - Gives code for how to connect your database to a code file and code examples of what can be done with that database

* [Get started with Cloud Firestore: ](https://firebase.google.com/docs/firestore/quickstart#python) - Shows how to set up your development and databse enviornments

* [Introduction to Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite?hl=en&authuser=0)

* [O'Reilly- Databse Options in the Cloud: ](https://www.oreilly.com/library/view/an-introduction-to/9781492044857/ch01.html)

* [Firebase Realtime Database Creation](https://www.google.com/search?q=how+to+make+a+firebase+database&rlz=1C1CHBF_enUS989US989&oq=how+to+start+a+firebase+&gs_lcrp=EgZjaHJvbWUqCAgBEAAYFhgeMgYIABBFGDkyCAgBEAAYFhgeMggIAhAAGBYYHjIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIKCAYQABgKGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCTEwMzUzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:39388994,vid:qKxisFLQRpQ,st:0)

* [Stack Abuse: ](https://stackabuse.com/python-check-if-variable-is-a-list/#checkifvariableisalistwithtype) Shows how to check to see if a variable is a list.

* [CSE 310 - Cloud Database Workshop](https://video.byui.edu/media/t/1_gvd1voh8)
* [Tracking your Firebase hosting bandwidth, & Firestore reference fields](https://youtu.be/Elg2zDVIcLo?si=McWIRwVk9qGLhyrl)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Create real Authenification for the Coach
* [ ] Create and implement authenification for other users like students and parents
* [ ] Create a new collection to track the parent's information.
* [ ] Allow the user to update references in the database
* [ ] Create an option for making new Clinics
