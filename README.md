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
		- **Sprint 1**
        - Work was done on emma branch during the first sprint then on the develop branch for the remaining sprints.
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
		- **Sprint 2**
        - [Modified hunny_app/forms.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/forms.py) to include the user's birthday and a variety of user preferences for matching.
        - [Configured hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/models.py) to calculate a user's age based on their birthday, and added multiple fields for the user's preferences.
        - [Modified hunny_app/templates/base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/base.html) to contain a dynamic universal navbar that was implemented on all pages.
        - [Created hunny_app/templates/preferences.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences.html) to display a user's current match preferences.
        - [Created hunny_app/templates/preferences_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences_edit.html) to allow the user to change/update their match preferences.
        - [Modified hunny_app/templates/user.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/user.html) to include the correct routes and a logout button with correct functionality.
        - [Added login_required decorators to user-only pages on hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/views.py) to ensure that some pages are only available when the user is logged in.
		- **Sprint 3**
		- [Modified hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/models.py) to allow the user to upload up to three pictures to their account.
		- [Configured hunny_app/templates/preferences.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences.html) and [hunny_app/templates/preferences_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences_edit.html) to have a UI that matched the rest of the web application.
		- [Configured hunny_project/settings.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_project/settings.py) to render the user's profile picture.
		- [Modified hunny_app/forms.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/forms.py) and [hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/models.py) to remove the children preferences for the ease of filtering in the match room.
	- ### **Next steps:**
        - Implement a geolocation feature so that the user doesn't have to manually enter the information.
		- Add range scrollers to some of the preferences to make them more intuitive.
- ## **Saron:**
	- ### **Features:** 
		- Created a user page to navigate the user through the website and an account page.
		- Front-end for account settings completed and set style format for profile, preferences, and their edit pages.
		- Created a contact page for user feedback.
		- Created an about page for quick 1,2,3 instructions of our website.
		- Adjusted pages for mobile friendly feature.
	- ### **Links to contributions:**
		- **Sprint 1**
		- Work was done in s_a383 branch that was later implemented into the master branch.
		- [Configured hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) included user page to be displayed.
		- [Configured hunny_project/hunny_app/templates/user.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/user.html) navigates the user to other features once logged in.
		- **Sprint 2**
		- Work was done in develop branch and focused on settings, profile, and preferences front end.
		- [Modified hunny_project/hunny_app/templates/settings.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/settings.html) to create a consistent front-end that allows the user to adjust their account settings.
		- [Modified hunny_project/hunny_app/templates/profile.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/profile.html) updated rough draft of profile from backend implementation.
		- [Modified hunny_project/hunny_app/templates/profile_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/profile_edit.html) to clean up input display for user to edit their profile.
		- [Modified hunny_project/hunny_app/templates/preferences.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences.html) front-end for consistent match with settings that displays their preferences.
		- [Modified hunny_project/hunny_app/templates/preferences_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences_edit.html) connected format to others to clean up website which will allow them to input their preferences.
		- **Sprint 3**
		- [Modified hunny_project/hunny_app/templates/base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/base.html) final updates for front-end to match changes especially with the navigation bar adjustments and drop down menu options.
		- [Modified hunny_project/hunny_app/templates/preferences.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences.html) reformatted to fit mobile friendly format and fit sizing of other pages.
		- [Modified hunny_project/hunny_app/templates/preferences_edit.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/preferences_edit.html) reformatted to fit mobile friendly format and fit sizing of other pages.
		- [Modified hunny_project/hunny_app/templates/profile.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/profile.html) reformatted away from bootstrap to fit navbar layout.
		- [Modified hunny_project/hunny_app/templates/about.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/about.html) added an about page with interactive panels to provide instructions of our site.
		- [Modified hunny_project/hunny_app/templates/contact.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/develop/hunny_project/hunny_app/templates/contact.html) added a contact page for users to send their opinions and update requests for our dating app.

	- ### **Next steps:**
		- Connect contact page to store and reference user feedback.
		- Update preference with more details and allow for specificity of their profile page for users to quickly find their accurate match.

-  ## **Lilly:**
	- ### **Features:**
		- Developed Front-End for the web application
		- Enable users to login/ display error messeges when they enter wrong information
		- Built Front-End for Matching system
		- Enable users to see profiles of other accounts one by one
		- Enable users to like/dislike profiles
		- Enable the matching system to instantiate matches among users and save all likes/matches information in the database
		- Automate Userprofile-creation upon Register-time
	- ### **Links to contributions:**
		- [Created Static Folder](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/static/messages/): Static folder to manage all static files(images, CSS, JS ...)for front-end
		- [Configured hunny_project/hunny_app/static/messages/main.css](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/static/messages/main.css): CSS file to style the content of homepage/login/singup pages 
		- [Configure hunny_project/hunny_app/templates/login.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/templates/login.html) html Template- User Interface for login feature
		- [Configured hunny_project/hunny_app/templates/messages.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/master/hunny_project/hunny_app/templates/messages.html) html Template- User Interface for message feature
		- [Configured hunny_project/hunny_app/templates/home.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/signup.html) html Template- User Interface for sign-up feature
		- [Configured hunny_project/hunny_app/templates/matchingroom.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/matchingroom.html) html Template- User Interface for Matching feature
		- [Configured hunny_project/hunny_app/templates/likenext.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/likenext.html) html Template- User Interface,which users will be brought to after clicking like-button
		- [Configured hunny_project/hunny_app/templates/dislikenext.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/dislikenext.html)  html Template- User Interface,which users will be brought to after clicking like-button
		- [Configured hunny_project/hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/models.py) Added attributes of Profile model to store matches,like, current profile to check out
		- [Configured hunny_project/hunny_app/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/urls.py) enable urls link for like/dislike/matchingroom pages
		- [Configured hunny_project/hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) implemented back-end for matching-room to see the current profile when users doen't make decision on likes/dislikes
		- [Configured https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_project/settings.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_project/settings.py) Adding details for userprofile-creation automation
		- [Configured hunny_project/hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) implemented back-end for like-button
		- [Configured hunny_project/hunny_app/views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/views.py) implemented back-end for dislike-button
		- [Configured hunny_project/hunny_app/models.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/models.py) Added attributes of Profile model to store matches,like, current profile to check out
	- ### **Next steps:**
		- refactor views.py and other hmtl files
		- use preference data to implement filter function for matching-system
		- edit the matching-system user-interface 
- ## **Isaac:**
	- ### **Features:**
        - Configured the backend database for the project.
        - Edited some of the CSS 
	- ### **Links to contributions:**
		- [Configured hunny_project/settings.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_project/settings.py) Added the backend connection to MySQL on Google *Completed*
		- [Configured hunny_app/templates/initial.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/initial.html) Fixed some of the CSS for the initial *Completed* 
		- [Configured hunny_app/templates/login.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/demo/hunny_project/hunny_app/templates/login.html) Fixed some of the CSS for login *Mostly completed*
	- ### **Next steps:**
        - Deploy the project online using AWS, Heroku, or something.
        - Add dummy data
        - Whatever else needs to be done too
- ## **Kody:**
    - ### **Features:** 
		- (Sprint 1) created project structure using Django framework, linking and editing templates, and creating a file to format other templates to promote a uniform UI 
		- (Sprint 2) created chat and chat room interface, created a landing page, handled matches for using websockets to enable chat functionality between users
		- (Sprint 3) implemented chat interface to display user matches, chat room ui expands for more info and displays messages intuitively with scrollable chat history, chat saves to database model, more user friendly landing page, contact and more
	- ### **Links to contributions:**
		- **Sprint 1**
		- work done mostly within **kody** branch but also **develop** and **demo**
		- [created Django project directory with required files](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/) to hold our app and dependencies
		- [configured hunny_project/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/urls.py) to ensure the server has a path to our hunny_app
		- [configured settings.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/settings.py) based on the Django framework
		- [created Django app directory with required files](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/) to hold our actual code
		- [configured hunny_app/urls.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/urls.py) to hold the urls to path to our templates
		- [configured views.py](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/views.py) to define the means of calling the urls and also contain some functionality of our pages
		- [linked and pathed html templates using Django framework](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/) to make sure each page is accessible 
		- [created base.html](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/base.html) for formatting templates to ensure reusable and flexible code
		- **Sprint 2**
		- work done mostly within **kody** branch but also **develop** and **demo**
		- [configured websockets](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_project/settings.py) based on the Django framework
		- [chat functionality](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project) based on the Django framework
		- [chat UI](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/chat.html) 
		- [chat room UI](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/chat_room.html) 
		- **Sprint 3**
		- work done mostly within **develop** and **demo**
		- [configured channels, integrated redis](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/asgi) based on the Django framework
		- [chat room displays user info](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project) based on the Django framework
		- [chat room more user friendly with scroll and mobile responsive](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/chat_room.html)
		- [better chat page UI, displays list of matches](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/chat.html) 
		- [save chat history to model](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/chat_room.html)
		- [reconnecting websocket](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/static/js/hunny_app/reconnecting-websocket.js) 
		- [improved landing page](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/landing.html) 
		- [matchroom more user friendly](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/)
		- [overall frontend fixes](https://bitbucket.org/cs3398-f21-vulcans/hunny/src/kody/hunny_project/hunny_app/templates/)
	- ### **Next steps:**
		- need unique chat rooms for each match
		- chat history loads backwards

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
- dev -
git clone 
pip install -r requirements
open docker
docker run -p 6379:6379 -d redis:5
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver

## Project Status
Project is: _in progress_

## What Went Well
- We are all pretty familiar with the Django framework now, so we didn't have to spend so much time researching before approaching our issues.
- We have all of the backend implemented for our main features.

## What Went Well (Individual)
- **Emma**
	- **Pro:** We were able to implement all of the main features that we originally wanted to include in the project.
	- **Con:** The file structure of our project still violates a lot of SOLID principles which led to some merge conflicts.

## What We Can Do Better (Individual)
- **Emma:** Create tests for the features that we have already implemented so that we can ensure no new developments will prevent parts of our features from working as expected. I already have a lot of experience using Selenium and Jenkins to automate test cases and think that my skills would be more useful there and contribute to the overall success of the project.

## What is Currently Impeding Us From Performing Better
- Some of us have different ideas about what pages and features should be included in the project at this point.
- Although we have weekly meetings, commitments outside of class are preventing some of us from devoting more time to the project.

## Acknowledgements
https://channels.readthedocs.io/en/stable/ - django channels documentation 
https://github.com/justdjango/justchat - for channels
https://github.com/joewalnes/reconnecting-websocket - for reconnecting websocket

## Contact
Created by [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
- [@kodygentry](github.com/kodygentry)
