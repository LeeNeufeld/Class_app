This README file will explain deployment and structure of the Morals Classifier Application. Also important settings perameters will be discussed

INSTALL and deployment:

The app was built using the Django web framework. All execute functions are run using python 3.7. 
To open the app files please follow these steps:
1.Save the "Classification_app" folder to your machine
2. In your chosen text editor go to FILE -> Open Folder -> navigate to the "Classification_app" Folder
3. This will open the "Classification_app" Folder in your editor to allow you to edit the files. 

Activating the virtual enivironment
1. You need to change the VIRTUAL_ENV PATH to where you have the located on your machine
2. the ACTIVATE file is found in venv -> Scripts -> activate
3. open a terminal/command line in your text editor
4. CD into the "venv" Folder
5. Once in the folder type "activate.bat" to activate the virtual enivironment. you are within the enivironment if (venv) appears before the path in your terminal

Activating a localhost server
1. Activate your virtual enivironment in your terminal
2. in your terminal type "python manage.py runserver"
3. you will be provided with a localhost URL when the host is running

Collecting Static files, Migrating Models, deployment to Google Cloud Platform
1. For static files and Models please go to https://www.djangoproject.com/ and review the documentation
2. For deployment on GCP please go to https://cloud.google.com/python/django/flexible-environment to review the documentation

App Subfolders
This section will list the apps subfolders and what information can be found it them

Classapp folder: 
 - pycache: used to house the python exe files these are auto created when you start a Django app
 - static: house all static files for the app such as pictures and style sheets
 - init.py: python init script. auto created when you start a Django app
 - settings.py: this file holds all of the different login and setting info for your app to connect to the database, google cloud instance and email
     - Change Database:
         - open settings.py file
         - scroll down to Database and fill in these fields:     
            'ENGINE': ,
            'NAME': ,
            'USER': ,
            'PASSWORD': ,
            'HOST': ,
            'PORT': ,
    
     - Change Email:
        - open settings.py file
        - scroll to email settings
        - enter the requested values in these fields:
            EMAIL_USE_TLS = 
            EMAIL_HOST = 
            EMAIL_HOST_USER = 
            EMAIL_HOST_PASSWORD = 
            EMAIL_PORT = 

 - urls.py: houses the url patterns to render the Django admin page

questions folder:
    - models.py: defines the questions model that is pulled from the database
    other folders are stock default files

response folder: this folder hoses the regex defenitions for postal code in the models.py file. The models within the file are there for leaderboard functionaility,
but due to database structure changes these models are now obsolite and are only still in the app as place holders until a new leaderboard is created. 
the other files in the folder are stock default files

sentences folder:
    - models.py: contains models defining the sentence information and connection to the database. 
    the other files are stock default files


Templates folder:
     - this folder holds all of the HTML files to display the webpages

Tutorial folder:
     - created for future use. all folders are currently stock default files

Users Folder:
     - admin.py holds the model that overrides the default django user model. this allows for the use of custom login perams such as using the email as the username for login
     - forms.py holds the custom forms and definitions for the profile and edit profile pages
     - models.py holds all models that form the user and all sentence and response related tables for the database
     - urls.py holds all of the url patterns that render the pages in the web browser
     - views.py holds all of the logic for rendering each individual page and is the connection between the HTML files and the Database
      - all other files and folders are stock default files

venv folder:
     - this holds all of the stock scripts and commands to implement the virtual enivironment

app.yaml file:
     - this allows the Google Cloud Platform to deploy the application

Models.py (in the root folder)
     - this holds all models that were migrated from a legacy database. This file was a default file that was created when the migrate was initiated

README.txt file:
     - details important asspects of the file structure of the application

requirements.txt file: 
     - holds all dependantcies and versions to be installed automatically by Gogle Cloud Platform when the app is deployed     