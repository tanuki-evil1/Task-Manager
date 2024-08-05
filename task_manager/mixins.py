from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AuthRequiredMixin(LoginRequiredMixin):
    auth_message = _('Вы не авторизованы! Пожалуйста, выполните вход.')

    def handle_no_permission(self):
        # Добавляем собственное сообщение об ошибке
        messages.error(self.request, self.auth_message)

        # Перенаправляем на страницу входа
        return redirect(reverse_lazy('login'))


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
