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

## REST API
  [Local Home](http://127.0.0.1:8000/api/)
  
  [Local User-Library](http://127.0.0.1:8000/api/lib/1)
  
  [Local Book-Edit](http://127.0.0.1:8000/api/book/1/edit)
  
  ## FrontEnd
  [Local Home](http://127.0.0.1:8000)
  
  [Local User-Library](http://127.0.0.1:8000/lib/1)
  
  [Local Book-Edit](http://127.0.0.1:8000/book/1/edit)
