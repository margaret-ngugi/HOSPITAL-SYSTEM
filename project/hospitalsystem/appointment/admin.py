from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=("time","date")
admin.site.register(Appointment,AppointmentAdmin)
