from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from task_manager.forms import LoginUserForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    authentication_form = LoginUserForm
    template_name = 'login.html'
    success_message = 'Вы залогинены'
    next_page = reverse_lazy('index')



class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('users_create')
