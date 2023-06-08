from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
