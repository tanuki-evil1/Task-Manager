from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User


class AuthRequiredMixin(LoginRequiredMixin):
    auth_message = _('You are not logged in! Please log in.')

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


class UserPermissionMixin:
    """
    Authorisation check.
    Prohibits changing an item created by another user.
    """
    permission_message = None
    permission_url = None

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])

        if request.user != user and not user.is_anonymous:
            messages.error(request, self.permission_message)
            return redirect(self.permission_url)

        return super().dispatch(request, *args, **kwargs)


class AuthorDeletionMixin:
    author_message = None
    author_url = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().author.id:
            messages.error(self.request, self.author_message)
            return redirect(self.author_url)
        return super().dispatch(request, *args, **kwargs)
