from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUSerCreationForm, CustomUserChangeForm
from .models import CustomUSer

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUSerCreationForm
    form = CustomUserChangeForm
    model = CustomUSer
    list_display = ['email', 'username', 'age', 'address', 'job']

admin.site.register(CustomUSer, CustomUserAdmin)