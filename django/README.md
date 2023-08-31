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
---
## Making Pages

Making web pages with Django consists of three stages: defining `URLs`, writing `views`, and writing `templates`. 
You can do these in any order, but in this project we’ll always start by defining the URL pattern. 
A URL pattern describes the way the URL is laid out. It also tells Django what to look for when matching a browser request with a site URL, so it knows which page to return.

Each `URL` then maps to a particular `view`. The `view` function retrieves and processes the data needed for that page. 
The `view` function often renders the page using a `template`, which contains the overall structure of the page. 
Example:

from django.contrib import admin
from django.urls import path

```
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

The first two lines import the admin module and a function to build URL paths. 
The body of the file defines the urlpatterns variable. 
In this `urls.py` file, which defines URLs for the project as a whole, the urlpatterns variable includes sets of URLs from the apps in the project. 
The list includes the module admin.site.urls, which defines all the URLs that can be requested from the admin site.

To include the URLs for learning_logs_apps, so add the following:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs_apps.urls')),
]

*We’ve imported the `include()` function, and we’ve also added a line to include the module learning_logs_apps.urls.*
