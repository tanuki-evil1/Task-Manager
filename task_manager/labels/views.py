from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.mixins import AuthRequiredMixin
from .forms import LabelCreateForm
from .models import Label


class IndexView(AuthRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'
    ordering = 'id'


class LabelCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    form_class = LabelCreateForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')
    success_message = 'Метка успешно создана'
    extra_context = {'title': 'Создать метку', 'button_text': 'Создать'}


class LabelUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = LabelCreateForm
    model = Label
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels_index')
    success_message = 'Метка успешно изменена'
    extra_context = {'title': 'Изменение метки', 'button_text': 'Изменить'}


class LabelDeleteView(SuccessMessageMixin, AuthRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = 'Метка успешно удалена'
    extra_context = {'title': 'Удаление метки', 'button_text': 'Да, удалить'}
