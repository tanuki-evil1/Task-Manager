from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin
from .forms import LabelCreateForm
from .models import Label


class IndexView(AuthRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'
    extra_context = {'title': _('Метки')}


class LabelCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Метка успешно создана')
    extra_context = {'title': _('Создать метку'), 'button_text': _('Создать')}


class LabelUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Метка успешно изменена')
    extra_context = {'title': _('Изменение метки'), 'button_text': _('Изменить')}


class LabelDeleteView(SuccessMessageMixin, DeleteProtectionMixin, AuthRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Метка успешно удалена')
    protected_message = _('Невозможно удалить метку, потому что она используется')
    protected_url = reverse_lazy('labels_index')
    extra_context = {'title': _('Удаление метки'), 'button_text': _('Да, удалить')}
