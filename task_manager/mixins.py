from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User


class AuthRequiredMixin(LoginRequiredMixin):
    auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')

    def handle_no_permission(self):
        # Добавляем собственное сообщение об ошибке
        messages.error(self.request, self.auth_message)

        # Перенаправляем на страницу входа
        return redirect(reverse_lazy('login'))


class UserIsOwnerMixin:
    permission_message = _("У вас нет прав для изменения другого пользователя.")
    permission_url = reverse_lazy('users_index')

    def dispatch(self, request, *args, **kwargs):
        # Получаем профиль по первичному ключу из URL
        user = get_object_or_404(User, pk=kwargs['pk'])

        # Проверяем, является ли текущий пользователь владельцем профиля
        if request.user != user:
            messages.error(request, self.permission_message)
            return redirect(self.permission_url)

        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class AuthorDeleteMixin:
    author_message = _("Задачу может удалить только ее автор")
    author_url = reverse_lazy('tasks_index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().author.id:
            messages.error(self.request, self.author_message)
            return redirect(self.author_url)
        return super().dispatch(request, *args, **kwargs)
