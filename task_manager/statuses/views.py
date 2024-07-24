from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.mixins import AuthRequiredMixin
from .forms import StatusCreateForm
from .models import Status


class IndexView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    ordering = 'id'


class StatusCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    form_class = StatusCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно создан'
    extra_context = {'title': 'Создать статус', 'button_text': 'Создать'}


class StatusUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = StatusCreateForm
    model = Status
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно изменен'
    extra_context = {'title': 'Изменение статуса', 'button_text': 'Изменить'}


class StatusDeleteView(SuccessMessageMixin, AuthRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно удален'
    extra_context = {'title': 'Удаление статуса', 'button_text': 'Да, удалить'}
