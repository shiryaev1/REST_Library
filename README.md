# REST_Library

## Installation & Setup

* $ git clone https://github.com/shiryaev1/REST_Library.git
* $ cd REST_Library
* $ sudo -u postgres psql postgres
  =# CREATE DATABASE lib_db;


* $ virtualenv library
* $ source library/bin/activate 


* (venv) $ pip install -r requirements.txt
* (venv) $ python manage.py migrate
* (venv) $ python manage.py loaddata fixtures/initial_data.json
* (venv) $ python manage.py runserver 0.0.0.0:8000
