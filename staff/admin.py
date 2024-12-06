from django.contrib import admin
from staff.models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ('patient',)
    search_fields=('patient', 'doctor')
    