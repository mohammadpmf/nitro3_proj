from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('national_id', 'phone_number', 'gender', 'birthday', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('national_id', 'phone_number', 'gender', 'birthday', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
