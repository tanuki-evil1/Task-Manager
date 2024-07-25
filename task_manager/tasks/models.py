from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor')
    created_at = models.DateTimeField(auto_now_add=True)
    label = models.ManyToManyField(Label, blank=True, through='TaskLabelRelation', through_fields=('task', 'label'))

    def __str__(self):
        return self.name


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
