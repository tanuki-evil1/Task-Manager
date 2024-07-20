from django import forms
from django.contrib.auth.forms import AuthenticationForm

from task_manager.users.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя', 'autofocus': True, 'autocapitalize': None, 'autocomplete': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'autocomplete': 'current-password'}))

    class Meta:
        model = User
        fields = ('username', 'password')