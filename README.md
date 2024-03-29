# SkyMarket

Avito like application.

Django REST API backend + SkyPro frontend

![Main page](https://habrastorage.org/webt/mt/0z/8y/mt0z8y5rpla6zylgwmnufftembw.jpeg)

![Product page](https://habrastorage.org/webt/s1/dw/ne/s1dwne1vipg9koaq-n82lywzciy.jpeg)


### Requirements
* Python >3.7
* Docker

## Usage

Install the required dependencies by running the following command: `pip install -r requirements.txt`

Run the following command in the market_postgres folder to start the Docker containers and build the project:
`docker-compose up -d --build`

Apply database migrations by running the following command: `python3 manage.py migrate`

Fill the database with initial data by running the following command: `python3 manage.py loadall`

Start the Django server: `python3 manage.py runserver`

Access the frontend at `localhost:3000`

API documentation is available at `http://127.0.0.1:8000/api/redoc-tasks/`

## Application Features:
- User registration, login/logout, and changing user information in a profile
- Reset password by email and set a new password
- List of ads in the user profile
- Create, change, and delete ads (contains title, description, price, and image)
- Add, change, and delete comments under ads

## Tests
To run the tests, execute the following command: `pytest`

The tests cover all views and functionalities related to ads and comments.

Please make sure to have the necessary dependencies installed from the `requirements.txt` file before running the tests.