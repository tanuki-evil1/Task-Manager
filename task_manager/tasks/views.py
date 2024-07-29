from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

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
    extra_context = {'title': _('Задачи'), 'button_text': _('Показать')}


class TaskCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Задача успешно создана')
    extra_context = {'title': _('Создать задачу'), 'button_text': _('Создать')}

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskDetailView(AuthRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    extra_context = {'title': _('Просмотр задачи')}


class TaskUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'base_form.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Задача успешно изменена')
    extra_context = {'title': _('Изменение задачи'), 'button_text': _('Изменить')}


class TaskDeleteView(AuthRequiredMixin, AuthorDeleteMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Задача успешно удалена')
    author_message = 'Задачу может удалить только ее автор'
    author_url = reverse_lazy('tasks_index')
    extra_context = {'title': _('Удаление задачи'), 'button_text': _('Да, удалить')}
