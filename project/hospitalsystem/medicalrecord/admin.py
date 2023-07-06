from django.contrib import admin
from .models import MedicalRecord

# Register your models here.
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display=("diagnosis","prescription")
admin.site.register(MedicalRecord,MedicalRecordAdmin)
