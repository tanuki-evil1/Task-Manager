from django.db import models

from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)