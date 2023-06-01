# SkyMarket

Django REST API backend

## Usage

Run `docker-compose up --build -d` in the **market_postgres** folder and make migrations.

Fill the database with `python3 manage.py loadall`

Start Django server with `python3 manage.py runserver`

Frontend on the `localhost:3000`

### Now working:
- User registration and login/logout
- Creating ad by user, changing title, description, price and image
- Adding comments under ads  by logged-in users

## Issues

Аpp still under development