from django.db import models

# Create your models here.
class Appointment(models.Model):
    
    date = models.DateField()
    time = models.TimeField()
