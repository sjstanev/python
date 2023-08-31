# DJANGO PROJECT
> Use Django to create Web APPs
- [Create VENV](#create-venv)
- [Install Django](#install-django)
- [Create Project](#create-project)
- [View the Project](#view-the-project)
- [Starting APPs](#starting-apps)
- [Modify the Database](#modify-the-database)


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
python manage.py startapp learning_logs_apps
```

Add our app to this list by modifying INSTALLED_APPS so it looks like this:

```
INSTALLED_APPS = [
    # My apps.
    'learning_logs_apps',

    # Default django apps.
    'django.contrib.admin',
    --snip--
]
```
## Modify the Database

```
python manage.py makemigrations learning_logs_apps
python manage.py migrate
```
*Whenever we want to modify the data that Learning Log manages, we’ll follow these three steps: modify `models.py`, call `makemigrations` on learning_logs_apps, and tell Django to `migrate` the project.*

---

- [Django Admin Site](#django-admin-site)
- [Entry Model](#entry-model)

## Django Admin Site

Setting Up a Superuser
```
python manage.py createsuperuser
```
## Entry Model

```
from django.db import models

class Topic(models.Model):
    --snip--

  class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."
```


Migrating the Entry Model
```
python manage.py makemigrations learning_logs_apps
python manage.py migrate
```



