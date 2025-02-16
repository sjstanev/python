from datetime import date

from django.db import models

# Create your models here.

# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birthday = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

# Department Model
class Department(models.Model):

    class Cities(models.TextChoices):
        Sofia = "Sofia", "Sofia",
        Plovdiv = "Plovdiv", "Plovdiv",
        Burgas = "Burgas", "Burgas",
        Varna = "Varna", "Varna"
    code = models.CharField(
        max_length=4,
        primary_key=True,
        unique=True)
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name='Employee Count',
    )
    location = models.CharField(
        max_length=20,
        choices=Cities.choices,
        # OPTIONAL FIELD
        null=True,
        blank=True,
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

# Project Model
class Project(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    duration_in_days = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Duration in Days',
    )
    estimated_hours = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Estimated Hours',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
        blank=True,
        null=True,
        default=date.today()
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
