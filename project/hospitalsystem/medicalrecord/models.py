from django.db import models

# Create your models here.
class MedicalRecord(models.Model):
  
    diagnosis = models.TextField()
    prescription = models.TextField()
