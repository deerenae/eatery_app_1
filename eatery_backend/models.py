from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # hours = models.TextField()
    thumb = models.TextField(default=None, blank=True, null=True)
    url = models.TextField(default=None, blank=True, null=True)
    menu_url = models.TextField(default=None, blank=True, null=True)
    phone_numbers = models.CharField(max_length=25)
    has_table_booking = models.TextField(default=None, blank=True, null=True)
    has_online_delivery = models.TextField(default=None, blank=True, null=True)
    carry_out = models.TextField(default=None, blank=True, null=True)

