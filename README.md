# CanCal - Canvas Scraper That helps you manage your assignments!

### Authors: Rui Gou, Ryan McMillan, Sam Brindle, Yu-Wei Hsieh 

## Summary of Project
A web scraper tool that scrapes the Canvas Assignments page for assignments, due dates, and available until dates
After scraping, it takes the data and uploads it to your personal calendar (Google Calendar, Apple Calendar, and/or something else)
Canvas assignments/calendar are important when enrolled in a course but they are isolated to the canvas web app. 
Our application will allow users/students to bring that information to their own personal time management app for 
a more personalized/assessable experience

## UML DOM

![](./DOM.png)

## Python QuickStart on Google Calendar API
### Get the credentials.json before you start it.
In order to test this App, you will need your **OWN** credential to access to Google Calendar API since this still in testing mode.

- Go to [Google API Credential](https://console.cloud.google.com/apis/credentials) to create a credential for OAtuh 2.0.
Select ``+ CREATE CREDENTIALS`` and choose ``OAuth client ID``.
- Make sure you choose ``Desktop app`` for **Application type** and create a name for it.
- Save it and download this credentials file into canvas-scraper folder.
- Rename this credential file to ``credentials.json`` and should be good to go.
- If you want to know more about how Google Calendar API works, go to [Calendar API](https://developers.google.com/calendar/api/quickstart/python?hl=en_US) 
for more details.

### Start the App
- Before using this App, make sure you install all the requirements. Execute ``python install -r requirements.txt``.
- Execute ``python main.py`` to start the APP.
- Make sure you enter correct email address and password.
- Have fun! 
