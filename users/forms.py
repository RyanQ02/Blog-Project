from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Specify fields within the Register form the user needs to fill out to register an account.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
