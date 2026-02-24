from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

# Register AppUser proxy model under MYAPP section
@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active')
    list_filter = ('is_active', 'date_joined')
    search_fields = ('username', 'email')

