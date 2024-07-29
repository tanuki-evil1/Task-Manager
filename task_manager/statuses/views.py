from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from .forms import StatusCreateForm
from .models import Status


class IndexView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Статусы')}


class StatusCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Статус успешно создан')
    extra_context = {'title': _('Создать статус'), 'button_text': _('Создать')}


class StatusUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = StatusCreateForm
    model = Status
    template_name = 'base_form.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Статус успешно изменен')
    extra_context = {'title': _('Изменение статуса'), 'button_text': _('Изменить')}


class StatusDeleteView(SuccessMessageMixin, DeleteProtectionMixin, AuthRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Статус успешно удален')
    protected_message = _('Невозможно удалить статус, потому что он используется')
    protected_url = reverse_lazy('statuses_index')
    extra_context = {'title': _('Удаление статуса'), 'button_text': _('Да, удалить')}
