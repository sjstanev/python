from django.db import models

# Create your models here.
class TempData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=100)