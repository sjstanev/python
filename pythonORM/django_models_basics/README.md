# Django Models Basics
- [Introduction to Models](#introduction-to-model)
- [Defining a Model](#defining-a-model)
- [Migrations Basics](#migrations-basics)

## Introduction to Models
Models define the structure of stored data 
- Containing the essential **fields** and **behaviors** of the data
- Each model maps to a **single database table**
- Django Model is a Python class that subclasses `django.db.models.Model`
- Each attribute of the model represents a **database field**

### Model Benefits
- Work with database data using **Python code**
- Don't have to write **low-level SQL** queries
- Focus on the **data** and the **business logic**
- Django **automatically** creates the needed queries and executes them

## Defining a Model
![img.png](../images/defining_model.png)

- Each Django application has a **models.py** file
- Create your model there. You need to subclass **models.Model**

```aiignore
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
```

### The most important and required part of a model
- Field names should not conflict with **reserved words**
- Field names cannot have **more than one underscore** in a row and cannot **end with** an **underscore**
- Each field is **an instance** of the appropriate **Field class**

### Field Types
- They determine the **column type** in a database table (e.g., INTEGER, VARCHAR, TEXT)
- Django has dozens of **built-in field** types
- Technically, they are defined in `django.db.models.fields`

### String Field Types
- **CharField**
  - Appropriate for small- to large-sized strings
  - Has one extra argument - max_length (required for all database backends included with Django except PostgreSQL)
- **TextField**
  - Appropriate for large texts
  - When specifying max length, it won't be enforced at the model or database level

### Numeric Field Types
- **IntegerField** - Stores integers
- **PositiveIntegerField** - Stores integers that could be either positive or zero
- **FloatField** - Stores floating-point numbers
- **DecimalField**
  - Stores fixed-precision decimal numbers
  - Two required arguments - max_digits and decimal_place
  
### Date/Time Field Types
- **DateField** - stores a date
- **TimeField** - stores a time
- **DateTimeField** - stores a date and a time
- **They have two extra field arguments (not required)**:
  - **auto_now** - Sets the field to now every time the object is saved
  - **auto_now_add** - Sets the field to now when the object is first created

### More Useful Field Types
- **BooleanField** - Stores Booleans - either **True** or **False** 
- **URLField** 
  - CharField for URLs
  - max_length is 200 by default 
- **EmailField**
  - CharField that **checks** if the value is a valid email address
  - max_length is 254 by default
  
### Field Arguments
- A certain set of **field-specific** or **common arguments**
  - **max_length** argument specifies the size of the VARCHAR field. It is a **field-specific, required** argument
  - **null**, **blank**, **default**, **primary_key**, etc. are **common optional arguments**
- If you do not specify **primary_key=True** for any field in your model, Django will automatically add an
**IntegerField** to hold the primary key

### Field Options
- Common SQL **constraints** but in Python code
- Available for **all** field types
- All of them are **optional**
```aiignore
class employee(models.Model):
    ...
    email_address = models.EmailField(unique=True)
```
* **Note:** they are **NOT field-specific** arguments
- **Default** - a default value or default callable object for the field
- **unique** 
  - **False** by default
  - if True, this field must be unique for the table column
- **null** - database-related
  - **False** by default. If True, empty values will be stored as **NULL**
  - Use for non-string fields such as integers, Booleans, and dates
- **blank** - validation-related
  - **False** by default. If True, the field is allowed to be blank
- **primary_key**
  - If **True**, the field becomes the primary key for the model
  - Used to **override** the default primary-key behavior
- The primary key field is **read-only**
- **Note:** If you change the value of the primary key on an existing
object and then save it, a **new object** will be created alongside the old one
- **verbose_name**
  - Most field types take it as an optional **first positional** argument
  - If it isn't given, Django automatically creates it using the **field's attribute name**
  , converting **underscores to spaces**
```aiignore
class Employee(models.Model):
   first_name = models.CharField(
        "First Name", 
        max_length=30)
   last_name = models.CharField(
        "Family Name", 
        max_length=40)
   email_address = models.EmailField(unique=True)
```
- **editable** 
  - **True** by default
  - if **False** it modifies the field so:
     - It is not able to be filled/edited
     - It disappears from all forms
```aiignore
class Employee(models.Model):
    ...
    email_address = models.EmailField(editable=False)
```
- Used to hide some fields such as encrypted code, verifications, etc.

### Choices Option
- **choices**
  - Use a **sequence** consisting of **iterables** of **exactly two items** to create choices
  - A new migration is **automatically created** each time the list of choices changes
```aiignore
MONTHS = [
    ('Jan', 'January'), # 'value to be set on the model', 'human-readable name'
    ('Feb', 'February'),
    ('Mar', 'March'),
    ...
]
```
- It appears as **select box** with the created choices instead of a standard text field
#### Class TextChoices
```aiignore
class MonthsTextChoices(models.TextChoices):
    JAN = "Jan", "January"
    FEB = "Feb", "February"
    ...
```
## Migrations Basics
### How Models Turn into DB tables
- Use models to create a **database schema** for your app
- Use **migrations** to **propagate changes** you make in your models (add, delete, modify fields, etc.)
  - First, **create migrations**
    - **makemigrations**  command
  - Next, **apply those changes** to the database
    - **migrate** command
#### **migrate** - Use to add changes made to the models into the database
```aiignore
python manage.py makemigrations
python manage.py migrate
```