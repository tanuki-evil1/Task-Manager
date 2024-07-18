from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя', 'autofocus': True, 'autocapitalize': None, 'autocomplete': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'autocomplete': 'current-password'}))