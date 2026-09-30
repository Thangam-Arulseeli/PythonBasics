### Install ---  pip install python-dotenv  -> to use the .env file variables
# NOTE : .env file is ignored in git push

from dotenv import load_dotenv # import dotenv and import load_dotenv
import os # import os module 

load_dotenv()

database_host = os.getenv("DATABASE_HOST")
database_port = os.getenv("DATABASE_PORT")
database_name= os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
database_password= os.getenv("DATABASE_PASSWORD")


print(database_host)
print(database_port)
print(database_name)
print(database_user)
print(database_password)

'''
Configuration Module
======================
Create:
----------
employee_app/
│
├── main.py
├── .env
│
└── config/
    ├── __init__.py
    └── settings.py

settings.py
------------
import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "Employee Management System"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)

DATABASE_HOST = os.getenv(
    "DATABASE_HOST",
    "localhost"
)

DATABASE_PORT = int(
    os.getenv("DATABASE_PORT", "5432")
)

main.py
--------
from config.settings import (
    APP_NAME,
    APP_ENV,
    DATABASE_HOST,
    DATABASE_PORT
)

print("Application:", APP_NAME)
print("Environment:", APP_ENV)
print("Database:", DATABASE_HOST)
print("Port:", DATABASE_PORT)
This is directly preparing the fresher for configuration in FastAPI projects.
################################

Required Project Structure
---------------------------
employee_management/
│
├── main.py
├── .env
├── requirements.txt
│
├── data/
│   └── employees.csv
│
├── reports/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── employee/
│   ├── __init__.py
│   ├── employee_service.py
│   └── validation.py
│
├── utils/
│   ├── __init__.py
│   ├── csv_handler.py
│   ├── json_handler.py
│   └── file_manager.py
│
└── exceptions/
    ├── __init__.py
    └── employee_exceptions.py



'''