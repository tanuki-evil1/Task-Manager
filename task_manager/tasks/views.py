from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import TaskCreateForm
from .models import Task


class IndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    ordering = 'id'


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = TaskCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно создан'
    extra_context = {'title': 'Создать статус', 'button_text': 'Создать'}


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно изменен'
    login_url = reverse_lazy('login')
    extra_context = {'title': 'Изменение статуса', 'button_text': 'Изменить'}


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Статус успешно удален'
    login_url = reverse_lazy('login')
    extra_context = {'title': 'Удаление статуса', 'button_text': 'Да, удалить'}
