from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import User


class AuthRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        # Добавляем собственное сообщение об ошибке
        messages.error(self.request, 'Вы не авторизованы! Пожалуйста, выполните вход.')

        # Перенаправляем на страницу входа
        return redirect('login')


class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        # Получаем профиль по первичному ключу из URL
        user = get_object_or_404(User, pk=kwargs['pk'])

        # Проверяем, является ли текущий пользователь владельцем профиля
        if request.user != user:
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect(reverse_lazy('users_index'))

        return super().dispatch(request, *args, **kwargs)
