from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Имя'))
    description = models.TextField(verbose_name=_('Описание'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('Статус'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author', verbose_name=_('Автор'))
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor', verbose_name=_('Исполнитель'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    labels = models.ManyToManyField(Label, blank=True, through='TaskLabelRelation', through_fields=('task', 'label'),
                                    verbose_name=_('Метки'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
