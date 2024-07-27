from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from .models import Task
from task_manager.labels.models import Label


class TaskFilter(FilterSet):

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Label'
    )

    own_tasks = BooleanFilter(
        label='Только свое',
        widget=forms.CheckboxInput,
        method='get_own_tasks',
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor']
