from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    

