from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserCreateForm
from .models import User
from task_manager.mixins import UserIsOwnerMixin, AuthRequiredMixin, DeleteProtectionMixin
from django.utils.translation import gettext_lazy as _


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    extra_context = {'title': _('Пользователи')}


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('login')
    success_message = _('Пользователь успешно зарегистрирован')
    extra_context = {'title': _('Регистрация'), 'button_text': _('Зарегистрировать')}


class UserUpdateView(AuthRequiredMixin, UserIsOwnerMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm  # Подумать
    template_name = 'base_form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('Пользователь успешно изменен')
    permission_message = _('У вас нет прав для изменения другого пользователя.')
    permission_url = reverse_lazy('users_index')
    extra_context = {'title': _('Изменение пользователя'), 'button_text': _('Изменить')}


class UserDeleteView(AuthRequiredMixin, UserIsOwnerMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('Пользователь успешно удален')
    permission_message = _('У вас нет прав для изменения другого пользователя.')
    permission_url = reverse_lazy('users_index')
    protected_message = _('Невозможно удалить пользователя, потому что он используется')
    protected_url = reverse_lazy('users_index')
    extra_context = {'title': _('Удаление пользователя'), 'button_text': _('Да, удалить')}
