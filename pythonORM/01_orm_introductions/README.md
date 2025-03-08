# Python ORM

Object-Relational Mapping (ORM) allows manipulating databases using common classes and objects.
Provides a layer of abstraction that hides the complexity of the database schema and relationships
### - Benefits of ORM
- Can automate some common tasks:
  - Creating, updating, and deleting records
  - Validating data
  - Managing transactions and connections
  - ORM reduces explicit SQL queries and is much less vulnerable to SQL injection
```
# Define POST variables
uname = request.POST['username']
passwd = request.POST['password']

# SQL query vulnerable to SQLi
SELECT id FROM users WHERE username='" + uname + "' AND password= '" + passwd + "'

# Set the passwd field
password' OR 1=1

# Database server runs the following SQL query
SELECT id FROM users WHERE username='username' AND password='password' OR 1=1'
```

### - Popular ORM Tools for Python

- Django
  - A great tool for building web applications rapidly
- web2py
  - An open source full-stack Python framework
- SQLObject
  - An ORM that provides an object interface to your database
- SQLAlchemy
  - Provides persistence patterns designed for efficient and high performing database access

### - Drawbacks of ORM
When it comes to complex queries and aggregations that require high performance and flexibility
- Can generate inefficient or suboptimal SQL queries
  - Poor performance
  - Excessive memory usage
  - Unexpected errors
- Limits control and customization over the SQL queries and operations
  - Harder to optimize
  - May not support some advanced features or functions

### - Database Drivers
Database Driver (module/connector) is a computer program that implements a protocol for a database connection
- Works like an adapter that connects a generic interface to a
specific database vendor implementation
- Accesses the physical data through a stand-alone engine
- Submits SQL statements to and retrieves results from the engine

![img.png](images/db_drivers.png)
### - Psycopg2
PostgreSQL database adapter for Python programming language
- Use the Psycopg2 module to:
  - Connect to PostgreSQL
  - Perform SQL queries and database operations
  - Psycopg2 is an external module

| Module/Connector                           | Psycopg2                        |
|--------------------------------------------|---------------------------------|
| ![img.png](images/module_connector.png)    | ![img.png](images/psycopg2.png) |


## Django & Django ORM

### - What is Framework?
- Platform for developing software applications
- Provides a foundation on which software developers can build programs for a specific platform
- A framework includes an API
- May include code libraries, a compiler and other programs used in the software development process

Django ORM - tightly coupled with Django framework, ability to handle medium to low complexity queries and medium to 
huge datasets. Migrations are another useful feature


### - Django Application
#### App vs Project
| Django App                                                                      | Django Project                                                   |
|---------------------------------------------------------------------------------|------------------------------------------------------------------|
| A Web application that does something - e.g., a blog system or a small task app | A collection of configurations and apps for a particular website |
| One app can be used in multiple projects                                        | The project can contain multiple apps                            |


Practice
---
### - Create virtual environment, activate or deactivate
```
python -m venv .venv
```

Activate `.venv` or deactivate it
```
source ./.venv/bin/activate
OR
deactivate
```

### - Install requirements
```
pip install django
```

### - Install Psycopg2
```
pip install psqcopg2-binary
```

### - Create an empty Django project
```
django-admin startproject {project-name}
```
### - Project Structure
`__init__.py`
- The direcotry is a python package

`settings.py`
- The configuration file for the Django Project

`urls.py`
- Contains the list of URLs

`manage.py`
- Tool for executing commands


### - Applied Migration(s):
```aiignore
python manage.py migrate
```
This will by default create `db.sqlite3` DB.

### - Run development server
The general syntax for running the Django development server on a different port is:
```aiignore
python manage.py runserver <port_number>
OR 
python manage.py runserver <ip_address>:<port_number>
```
The `runserver` command starts the development server on the internal IP at port 8000 by default

### - Django Application
Creating a Django App 
```aiignore
python manage.py startapp <app>
```
Django automatically generates the basic directory structure of an app
### - Directory Structure
`admin.py` - The admin site module

`models.py` - The models of the app

`views.py`  - The views of the app

`migrations` - Command-line utility for propagating changes in models

###  - Including an App
To include an app in a project, add a reference to the app in the INSTALLED_APPS setting
```aiignore
In Settings.py module, in array INSTALLED_APPS = [ ..., 'tasks']  add <new_apps> at end.
```
![img.png](images/include_apps.png)

### - To create *<requirements.txt>* use:
```
pip freeze > requirements.txt
```
### - Install requirements
```aiignore
pip install -r requirement.txt
```
### - Additional pip commands
```aiignore
pip install <package_name>          	  # Install a package
pip uninstall <package_name>        	  #  Uninstall a package
pip install --upgrade <package_name>  	  # Upgrade a package
pip list                            	  # List all installed packages
pip show <package_name>             	  # Show details of a package
pip freeze                                # Display installed packages in a format compatible for requirements.txt
pip freeze > requirements.txt       	  # Save installed packages to a file
pip install -r requirements.txt     	  # Install packages from a file
pip list --outdated                   	  # List outdated packages
pip install --upgrade <package_name>  	  # Upgrade a specific package
```
### - Create superuser for admin site
```aiignore
python manage.py createsuperuser
```

### - Django dbshell

- An interactive command-line interface shell environment
- A very useful tool for SQL database debugging when working on a Django application
```aiignore
python manage.my dbshell
```
* In case you receive an Error like: "CommandError: You appear not to have the 'psql' program installed 
or on your path"
```aiignore
\dt command shows all tables in the current database
\d <table_name> command shows a specific table
```
using Django dbshell - Queries
```
SELECT * FROM <table_name>;
```
### - Create packege
Zip on mac/linux
```aiignore
zip -r project.zip . -x "*.idea*" -x "*.venv*" -x "*__pycache__*"
```
Zip on Windows
```aiignore
Get-ChildItem -Path . -Recurse -Force |
  Where-Object { $_.FullName -notmatch "\.idea|\.venv|__pycache__" } |
  Compress-Archive -DestinationPath .\project.zip

```
---
