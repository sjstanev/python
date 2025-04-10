from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

class Blog(models.Model):
    post = models.TextField()
    author = models.CharField(max_length=35)

class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()

class Recipe(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()
    ingredients = models.TextField()
    cook_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    created_at = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    username = models.CharField(
        max_length=65,
        unique=True,
    )
    first_name = models.CharField(
        max_length=40,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=40,
        blank=True,
        null=True
    )
    email = models.EmailField(
        unique=True,
        default='students@softuni.bg'
    )
    bio = models.TextField(max_length=120)
    profile_image_url = models.URLField()
    created_at = models.DateTimeField(auto_now=True)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20)
    duration_minutes = models.PositiveIntegerField()
    equipment = models.CharField(max_length=90)
    video_url = models.URLField(
        blank=True,
        null=True
    )
    calories_burned = models.PositiveIntegerField(default=1)
    is_favorite = models.BooleanField(default=False)