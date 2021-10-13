# Hunny
- 	Who you’re working with (you and your team members)?
Saron Abebe, Kody Gentry, Isaac Jaramillo, Thanh Pham, and Emma Rodrigue.
-	What you’re creating?
Hunny is a blind dating web application that allows users to find their match based on personality before looks.
-	Who you’re doing it for, your audience (may be same as the previous question)?
Hunny is for those who are looking to meet new people that want a genuine connection past appearance. 
-	Why you’re doing this, the impact or change you hope to make?
We hope to break a user's cycle of falling for the wrong type by avoiding the overwhelming expectations of appearance.
	
# **Project Status:**
- ## We have:
	- the basic structure of our project complete using the Django framework along with most of the pages that we are planning on implementing in the future.
	- the ability to sign up for our app and also sign in using the appropriate credentials.
	- the base of our UI complete, but we need to diverge on an overall style and format.
	- few functionalities in our pages, this is the main focus in our next sprint.
- ## **Next steps:**
	- creating a uniform and aesthetic look to our UI with styling and structure
	- giving our pages more functionality including: 
		- home page UI displaying other users profiles 
		- uniform nav bar to switch between all pages
		- like/dislike another user
		- send and recieve messages with matches
		- location tracking and radius
		- animations (like/dislike, home page scrolling, loading, misc.)
		
# **Contributors:**
- ## **Emma:**
	- ### **Features:** 
		- Created a profile route with the ability to save specific profile information in our database so that users who have created an account can view and edit their profile.
	- ### **Links to contributions:**
		- Work was done on emma branch then implemented into the demo branch since the file structure changed mid-project.
		- [Configured hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) to edit and save user information, and to verify that the user 
		  is logged in before attempting to edit a profile to ensure that only their profile is being updated.
		- [Configured hunny_app/forms.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/forms.py) to create a form where the user can enter their personal information.
		- [Configured hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/models.py) to set restrictions for the type of data a user can enter.
		- [Configured hunny_app/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/urls.py) to set routes for the profile and edit profile pages.
		- [Created hunny_app/templates/base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/base.html) as a base template for the profile page.
		- [Created hunny_app/templates/edit_profile.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/edit_profile) to display the form to edit a user's profile.
		- [Created hunny_app/templates/profile.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/profile.html) to display the user's profile card with all of the information they previously entered in the account information.
		- [Linked templates related to the user's profile](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/) to ensure that everything flows together and there is a seemless transition when moving from the edit profile page to the view profile page.
	- ### **Next steps:**
		- Modify the steps taken to edit the user's original profile information to ensure that everything is done through our web application and not the django admin site.
- ## **Saron:**
	- ### **Features:** 
	- ### **Links to contributions:**
	- ### **Next steps:**
- ## **Lily:**
	- ### **Features:** 
	- ### **Links to contributions:**
	- ### **Next steps:**
- ## **Isaac:**
	- ### **Features:**
		- Configured the backend to allow users to register and implemented the code needed for the frontend so it can pass the information along
		- Configured the backend to allow users to sign in, although the user page isn't done yet so it just refreshes the current page. 
	- ### **Links to contributions:**
		- [Configured hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) Edited the method register which will take in a request on the page and render the necessary information. *Currently in progress to add more features but works*
		- [Configured hunny_app/forms.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/forms.py) created a class that will allow users to input the data which Django can understand and take in the information. *Completed*
		- [Configured hunny_app/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/urls.py) Slightly edited the urls so they could load the proper information. *Completed*
		- [Configured hunny_app/templates/initial.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/initial.html) to display the form to allow a person to register. *Completed, but may be able to add additional features*
		- [Configured hunny_app/templates/login.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/login.html) to allow a user to login (currently just refreshes page). *Mostly completed, some things needed to be changed*
		- [Configured requirements.txt](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/requirements.txt) to update Django dependencies. *Completed for now*
	- ### **Next steps:**
		- Clean up UI, add more features to login/signup such as displaying a message that a user successfully created an account.
		- link it so when the user logs in, it'll redirect them to Emma's user profile page.
- ## **Kody:**
    - ### **Features:** 
		- created project structure using Django framework, linking and editing templates, and creating a file to format other templates to promote a uniform UI 
	- ### **Links to contributions:**
		- work done mostly within **kody** branch but also **demo** and **master**
		- [created Django project directory with required files](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/) to hold our app and dependencies
		- [configured hunny_project/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/urls.py) to ensure the server has a path to our hunny_app
		- [configured settings.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/settings.py) based on the Django framework
		- [created Django app directory with required files](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/) to hold our actual code
		- [configured hunny_app/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/urls.py) to hold the urls to path to our templates
		- [configured views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/views.py) to define the means of calling the urls and also contain some functionality of our pages
		- [linked and pathed html templates using Django framework](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/) to make sure each page is accessible 
		- [created base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/base.html) for formatting templates to ensure reusable and flexible code
	- ### **Next steps:**
		- home page UI displaying other users profiles 





## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Create an image/picture/icon representing your project.
- Provide general information about your project here.
- What problem does it (intend to) solve?
- What is the purpose of your project?
- Why did you undertake it?


## Technologies Used
- Django
- HTML
- CSS
- Javascript

## Features
List the ready features here:
- Messaging platform so that users can talk to each other and get to know each other.
- Like and dislike buttons so that users can curate their matches.
- Preferences and settings for the individual user to customize their experience.
- Profile: allows user to introduce themselves before the search begins.
- Survey: word bank of questions that'll be used to connect them with those of similar interest.

## Screenshots
[hunny logo](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/static/hunny-logo.PNG)

## Setup
<!What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?
Proceed to describe how to install / setup one's local environment / get started with the project.>


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_

## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
