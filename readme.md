# Project Title

User Management App

## Description

This project is a simple web application for managing user information. It uses Flask for the backend, SQLAlchemy for database operations, and a basic HTML form for the frontend.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/user-management-app.git
   cd user-management-app

2. Create a virtual environment (recommended):
   ```
   conda create -p env python=3.8        # create virtual env
   conda activate ./env                  # activate the virtual env


3. Install Dependencies
   ``` 
   pip install -r requirements.txt
   ```

## Usages

1. Run the Flask application:
   ``` 
   python app.py
   ```
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

2. Interact with the application:

Visit the root route (/) to view the user information table.
Access the /add route to add new users.


## Deployement

1. Use git for version control and deployment to Heroku. Follow the following commands

    ```
    heroku                                        # check if heroku is working file
    heroku login                                  # login to heroku
    ```
    
    ```
    git init
    git add .
    git commit -m "initial commit"
   git remote -v                                   # check remote
    ```
    
    ```
    heroku create usermanagmentapp                 # Replace with your app-name
    git push heroku main/master
    ```

## App Link

Go through the following link to use the application
https://usermanagmentapp-a0643dd2c584.herokuapp.com/


## Screenshots

![Screenshot 1](screenshots/Screenshot%20(133).png)
*Caption: Front-end -- User Data added .*

![Screenshot 2](screenshots/Screenshot%20(134).png)
*Caption: Updating Harry data to db.*

![Screenshot 2](screenshots/Screenshot%20(132).png)
*Caption: Deleting Harry data from db.*

## Contributing
Contributions are welcome! Reach me out at https://www.linkedin.com/in/deepraj-arya-3060631b7/

