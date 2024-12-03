from django.contrib import admin

# Register your models here.
# Custom admin for Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active')
    search_fields = ('email', 'username')
