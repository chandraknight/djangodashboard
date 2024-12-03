from django.contrib import admin
from .models import MyUser

# Custom admin for MyUser
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'get_role', 'is_active', 'is_staff', 'created_at', 'updated_at')
    search_fields = ('email', 'username', 'role')

    # To display the role in list_display
    def get_role(self, obj):
        return obj.get_role_display()  # Converts "ADMIN" to "Admin" it means to display in human readable format
    get_role.short_description = 'Role'  # Name for the column in the admin panel, we can choose our name



