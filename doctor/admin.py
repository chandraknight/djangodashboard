from django.contrib import admin
from doctor.models import DoctorProfile
# Register your models here.
# Custom admin for Student
@admin.register(DoctorProfile)
class DoctorAdmin(admin.ModelAdmin):
    list_display= ('user',)
    search_fields = ('email', 'username')
    