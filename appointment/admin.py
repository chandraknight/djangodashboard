from django.contrib import admin

# Register your models here.
from appointment.models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ('patient',)
    search_fields=('patient', 'doctor')