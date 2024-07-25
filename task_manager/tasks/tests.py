from django.test import TestCase, Client
from django.urls import reverse
from .models import Task
from .forms import TaskCreateForm
from task_manager.utils import load_data
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = load_data('user.json')
        self.user = User.objects.create_user(**self.data['setup'])
        self.status = Status.objects.create(name='TestStatus')
        self.label = Label.objects.create(name='TestLabel')
        self.task = Task.objects.create(name='TestTask', description='TestTask', status=self.status, author=self.user,
                                        executor=self.user)

    def test_task_list_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('tasks_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')
        self.assertContains(response, 'TestTask')

    def test_task_create_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('tasks_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/create.html')
        self.assertIsInstance(response.context['form'], TaskCreateForm)

        response = self.client.post(reverse('tasks_create'),
                                    {'name': 'CreateTask', 'description': 'CreateTask', 'executor': self.user.pk,
                                     'status': self.status.pk})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('tasks_update', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/update.html')
        self.assertIsInstance(response.context['form'], TaskCreateForm)
        response = self.client.post(reverse('tasks_update', args=[self.task.pk]),
                                    {'name': 'UpdateTask', 'description': 'UpdateTask', 'executor': self.user.pk,
                                     'status': self.status.pk})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'UpdateTask')

    def test_task_delete_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('tasks_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/delete.html')

        response = self.client.post(reverse('tasks_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
