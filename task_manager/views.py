from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from task_manager.forms import LoginUserForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('users_index')
        print(form.errors)
        return render(request, 'login.html', {'form': form})


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('users_create')
