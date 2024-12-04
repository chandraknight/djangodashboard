from django.contrib import admin
from patient.models import PatientProfile
# Register your models here.
# Custom admin for Student
@admin.register(PatientProfile)
class PatientAdmin(admin.ModelAdmin):
    list_display= ('user',)
    search_fields = ('email', 'username')
    readonly_fields = ('age',)