from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User
from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from .filters import TaskFilter
from .forms import TaskCreateForm
from .models import Task


class IndexView(AuthRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    extra_context = {'title': _('Tasks'), 'button_text': _('Show')}


class TaskCreateView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'base_form.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully created')
    extra_context = {'title': _('Create task'), 'button_text': _('Create')}

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskDetailView(AuthRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    extra_context = {'title': _('Task preview')}


class TaskUpdateView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'base_form.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully changed')
    extra_context = {'title': _('Task change'), 'button_text': _('Change')}


class TaskDeleteView(AuthRequiredMixin, AuthorDeletionMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully deleted')
    author_message = _('The task can be deleted only by its author')
    author_url = reverse_lazy('tasks_index')
    extra_context = {'title': _('Delete task'), 'button_text': _('Yes, delete')}

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.id != self.get_object().author.id and not request.user.is_anonymous:
    #         messages.error(self.request, self.author_message)
    #         return redirect(self.author_url)
    #     return super().dispatch(request, *args, **kwargs)
