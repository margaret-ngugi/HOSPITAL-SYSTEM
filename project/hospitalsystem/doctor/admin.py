from django.contrib import admin
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display=("name","address","specialization","phone_number","email")
admin.site.register(Doctor,DoctorAdmin) 

