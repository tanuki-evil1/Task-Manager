from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserCreateForm
from .models import User
from .utils import UserIsOwnerMixin, AuthRequiredMixin


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    ordering = 'id'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'
    extra_context = {'title': 'Регистрация', 'button_text': 'Зарегистрировать'}


class UserUpdateView(AuthRequiredMixin, UserIsOwnerMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm # Убрать сообщение о том, что такое пользователь есть и проверить демо
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно изменен'
    login_url = reverse_lazy('login')
    extra_context = {'title': 'Изменение пользователя', 'button_text': 'Изменить'}


class UserDeleteView(AuthRequiredMixin, UserIsOwnerMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно удален'
    login_url = reverse_lazy('login')
