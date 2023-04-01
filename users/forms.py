from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUSer

class CustomUSerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUSer
        fields = UserCreationForm.Meta.fields+('age', 'address', 'job')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUSer
        fields = UserChangeForm.Meta.fields