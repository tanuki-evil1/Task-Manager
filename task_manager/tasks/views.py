from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from task_manager.users.models import User
from task_manager.mixins import AuthRequiredMixin, AuthorDeleteMixin

from .filters import TaskFilter
from .forms import TaskCreateForm
from .models import Task


class IndexView(AuthRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = 'id'
    extra_context = {'title': 'Создать задачу', 'button_text': 'Показать'}


class TaskCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно создана'
    extra_context = {'title': 'Создать задачу', 'button_text': 'Создать'}

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно изменена'
    login_url = reverse_lazy('login')
    extra_context = {'title': 'Изменение задачи', 'button_text': 'Изменить'}


class TaskDeleteView(AuthRequiredMixin, AuthorDeleteMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Задача успешно удалена'
    extra_context = {'title': 'Удаление задачи', 'button_text': 'Да, удалить'}
