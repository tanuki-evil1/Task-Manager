from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import UserCreateForm
from .models import User
from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from django.utils.translation import gettext_lazy as _


class IndexView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users')}


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {'title': _('Create user'), 'button_text': _('Register')}


class UserUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm  # Подумать
    template_name = 'base_form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users_index')
    extra_context = {'title': _('Update user'), 'button_text': _('Update')}

    def dispatch(self, request, *args, **kwargs):
        # Получаем профиль по первичному ключу из URL
        user = get_object_or_404(User, pk=kwargs['pk'])

        # Проверяем, является ли текущий пользователь владельцем профиля
        if request.user != user:
            messages.error(request, self.permission_message)
            return redirect(self.permission_url)

        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(AuthRequiredMixin, DeleteProtectionMixin,
                     SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User is successfully deleted')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users_index')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users_index')
    extra_context = {'title': _('Delete user'), 'button_text': _('Yes, delete')}

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])

        if request.user != user:
            messages.error(request, self.permission_message)
            return redirect(self.permission_url)

        return super().dispatch(request, *args, **kwargs)
