from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    image = models.ImageField(default='https://www.google.com/')
    dineIn = models.BooleanField
    carryOut = models.BooleanField
    delivery = models.BooleanField

