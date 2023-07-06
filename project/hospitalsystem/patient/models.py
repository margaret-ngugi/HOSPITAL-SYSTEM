from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()

