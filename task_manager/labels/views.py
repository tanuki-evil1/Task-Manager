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
    extra_context = {'title': _('Labels')}


class LabelCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully created')
    extra_context = {'title': _('Create label'), 'button_text': _('Create')}


class LabelUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully changed')
    extra_context = {'title': _('Change label'), 'button_text': _('Change')}


class LabelDeleteView(SuccessMessageMixin, DeleteProtectionMixin, AuthRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully deleted')
    protected_message = _('It is not possible to delete a label '
                          'because it is in use')
    protected_url = reverse_lazy('labels_index')
    extra_context = {'title': _('Delete label'), 'button_text': _('Yes, delete')}
