# DJANGO PROJECT
> Use Django to create Web APPs
- [Create VENV](#create-venv)
- [Install Django](#install-django)
- [Create Project](#create-project)
- [View the Project](#view-the-project)
- [Starting APPs](#starting-apps)


## Create VENV

Create project directory 
```
cd /home
mkdir learning_log
cd learning_log
```
Install python venv and create named virtual environment (ll_venv)
```
apt install python3.11-venv
python -m venv ll_env
```

Activating the Virtual Environment `(ll_env)learning_log$`
```
source ll_env/bin/activate
```
To stop using a virtual environment, enter `deactivate`

## Install Django
```
pip install --upgrade pip
pip install django
```

## Create Project
Creating a Project in Django
```
django-admin startproject ll_project .
```
*Don’t forget this dot, or you might run into some configuration issues when you deploy the app. If you forget the dot, delete the files and folders that were created (except ll_env) and run the command again.*

Creating the Database
```
python manage.py migrate
```

*allow host in setting.py by adding the following line*
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.82.225"]
```

## View the Project
```
python manage.py runserver 0.0.0.0:8000
```

## Starting APPs
```
python manage.py startapp learning_logs
```
