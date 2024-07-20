from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserForm
from .models import User
from .utils import UserIsOwnerMixin, AuthRequiredMixin


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(AuthRequiredMixin, UserIsOwnerMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно изменен'
    login_url = reverse_lazy('login')


class UserDeleteView(AuthRequiredMixin, UserIsOwnerMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно удален'
    login_url = reverse_lazy('login')
