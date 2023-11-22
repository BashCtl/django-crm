# Example of the simple Django CRM application

### Project Structure:
````
django_crm/
├── django_crm
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── website
    ├── admin.py
    ├── apps.py
    ├── froms.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   ├── add_record.html
    │   ├── base.html
    │   ├── home.html
    │   ├── navbar.html
    │   ├── record.html
    │   ├── register.html
    │   └── update_record.html
    ├── tests
    │   ├── __init__.py
    │   ├── test_data
    │   │   ├── invalid_login.csv
    │   │   └── user.json
    │   ├── test_models.py


````

## How to run locally
First clone repo:
````
git clone git@github.com:BashCtl/django-crm.git
````
Navigate to project dir:
````
cd django-crm/django-crm
````
Install dependencies:
````
pip install -r requirements.txt
````
Install MySQL database [Installation guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html)

Create .env file in the root directory, and specify following variables:
````
DB_NAME= <MySQL db name (should be created manually )>
DB_USER= <MySQL db username>
DB_PASSWORD= <MySQL db password>
DB_HOST=localhost
DB_PORT=3306

````

Migrate db:
````
python manage.py migrate
````

Start application:

````
python manage.py runserver
````

Open application on :
````
localhost:8000
````

Register user, and than you can create records in db
