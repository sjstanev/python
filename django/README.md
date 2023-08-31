# --------------------- Creating VENV and Installing Django ----------------------------------------

# Create project directory 
cd /home
mkdir learning_log
cd learning_log

# Install python venv and create named virtual environment (ll_venv)
apt install python3.11-venv
python -m venv ll_env

# Activating the Virtual Environment "(ll_env)learning_log$"
source ll_env/bin/activate 
# To stop using a virtual environment, enter deactivate

# Installing Django
pip install --upgrade pip
pip install django

# ----------------------------- Create Projcet ----------------------------------------

# Creating a Project in Django
django-admin startproject ll_project .
### Don’t forget this dot, or you might run into some configuration issues when you deploy the app. If you forget the dot, delete the files and folders that were created (except ll_env) and run the command again. ###

# Creating the Database
python manage.py migrate


# allow host in setting.py by adding the following line
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.82.225"]

# Viewing the Project
python manage.py runserver 0.0.0.0:8000

# Starting an App
python manage.py startapp learning_logs
