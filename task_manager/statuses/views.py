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
    extra_context = {'title': _('Statuses')}


class StatusCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully created')
    extra_context = {'title': _('Create status'), 'button_text': _('Create')}


class StatusUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = StatusCreateForm
    model = Status
    template_name = 'base_form.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully changed')
    extra_context = {'title': _('Change status'), 'button_text': _('Change')}


class StatusDeleteView(SuccessMessageMixin, DeleteProtectionMixin, AuthRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully deleted')
    protected_message = _('It is not possible to delete a status '
                          'because it is in use')
    protected_url = reverse_lazy('statuses_index')
    extra_context = {'title': _('Delete status'), 'button_text': _('Yes, delete')}
