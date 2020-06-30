from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    DineIn = models.BooleanField
    CarryOut = models.BooleanField
    Delivery = models.BooleanField

