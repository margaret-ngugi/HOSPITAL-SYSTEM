from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=("name","age","gender","phone_number","date_of_birth","email")
admin.site.register(Patient,PatientAdmin) 

