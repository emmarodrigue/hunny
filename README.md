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
        - Created a pages for the user's match preferences.
        - Created a universal navbar that displays different routes based on if the user is logged in or not.
        - Developed and implemented the backend for the preferences page and edit profile page.
	- ### **Links to contributions:**
        - Work was done on emma branch then implemented into the demo branch since the file structure changed mid-project.
        - [Configured hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) to edit and save user information, and to verify that the user 
          is logged in before attempting to edit a profile to ensure that only their profile is being updated.
        - [Configured hunny_app/forms.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/forms.py) to create a form where the user can enter their personal information.
        - [Configured hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/models.py) to set restrictions for the type of data a user can enter.
        - [Configured hunny_app/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/urls.py) to set routes for the profile and edit profile pages.
        - [Created hunny_app/templates/base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/base.html) as a base template for the profile page.
        - [Created hunny_app/templates/edit_profile.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/edit_profile) to display the form to edit a user's profile.
        - [Created hunny_app/templates/profile.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/profile.html) to display the user's profile card with all the information they previously entered the account information.
        - [Linked templates related to the user's profile](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/) to ensure that everything flows together and there is a seemless transition when moving from the edit profile page to the view profile page.
        - [Implemented the backend functionality for hunny_app/templates/profile_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/profile_edit.html) so that the user's current settings are displayed when editing and changes can be saved.
        - [Configured hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/views.py) to contain the functionality for logging out a user, displayed the preferences page, and saving user preferences.
        - [Modified hunny_app/forms.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/forms.py) to include the user's birthday and a variety of user preferences for matching.
        - [Configured hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/models.py) to calculate a user's age based on their birthday, and added multiple fields for the user's preferences.
        - [Modified hunny_app/templates/base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/base.html) to contain a dynamic universal navbar that was implemented on all pages.
        - [Created hunny_app/templates/preferences.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences.html) to display a user's current match preferences.
        - [Created hunny_app/templates/preferences_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences_edit.html) to allow the user to change/update their match preferences.
        - [Modified hunny_app/templates/user.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/user.html) to include the correct routes and a login button with correct functionality.
        - [Added login_required decorators to user-only pages on hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/views.py) to ensure that some pages are only available when the user is logged in.
	- ### **Next steps:**
        - Allow the user to upload multiple pictures.
        - Ensure that all profile pictures render correctly.
- ## **Saron:**
	- ### **Features:** 
		- Created a user page to navigate the user through the website and an account page.
	- ### **Links to contributions:**
		- Work was done in s_a383 branch that was later implemented into the master branch.
		- [Configured hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) included user page to be displayed.
		- [Configured hunny_project/hunny_app/templates/user.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/user.html) navigates the user to other features once logged in.
	- ### **Next steps:**
		- Link the buttons to our other urls, complete account settings page.
- ## **Lily:**
	- ### **Features:**
		- Developed Front-End for the web application
	- ### **Links to contributions:**
		- [Created Static Folder](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/static/messages/): Static folder to manage all static files(images, CSS, JS ...)for front-end
		- [Configured hunny_project/hunny_app/static/messages/main.css](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/static/messages/main.css): CSS file to style the content of homepage/login/singup pages 
		- [Configure hunny_project/hunny_app/templates/login.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/templates/login.html) html Template- User Interface for login feature
		- [Configured hunny_project/hunny_app/templates/messages.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/templates/messages.html) html Template- User Interface for message feature
		- [Configured hunny_project/hunny_app/templates/home.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/templates/home.html) html Template- User Interface for sign-up feature
	- ### **Next steps:**
		- Create User-interface (html templates + CSS) for other features
		- Develop the back-end for Match-Room features
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
