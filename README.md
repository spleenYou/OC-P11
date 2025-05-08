<img src='https://user.oc-static.com/upload/2020/09/22/16007798203635_P9.png' alt='Logo Güdlft'>

## Description

Project Güdlft - Improve a Python web application through testing and debugging

Güdlft is a company that has created a digital platform to coordinate strength competitions. Güdlft has set up a team called Regional Outreach to create a lighter (and cheaper) version of their current platform for regional organisers. The aim of the application is to streamline the management of competitions between clubs.

The prototype is stored in this [GitHub repository](https://github.com/OpenClassrooms-Student-Center/Python_Testing).
In the issue section of this repository are bugs to fix and features to implement. The second step 
is to create functional and integration tests to make sure the functionality.

## Installation
open terminal
1. clone the repository: <br>
`git clone https://github.com/spleenYou/OC-P11.git`
2. go to folder: <br>
`cd OC-P11`
3. install the virtual environment: <br> 
`python3 -m venv .venv`
4. activate the virtual environment with following command: 
   - on MacOS and Linux: `source .venv/bin/activate`
   - on Windows: `.venv\Scripts\activate` 
5. install all dependencies with: <br>
`pip install -r requirements.txt`
6. run the server with:
    ```
    export FLASK_APP=server
    export FLASK_ENV=development
    flask run
    ```

## Current setup

The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
* competitions.json - list of competitions
* clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.