from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreatForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'age']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
