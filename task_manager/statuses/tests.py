from django.test import TestCase, Client
from django.urls import reverse
from .models import Status
from .forms import StatusCreateForm
from task_manager.utils import load_data
from task_manager.users.models import User


class StatusTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = load_data('user.json')
        self.user = User.objects.create_user(**self.data['setup'])
        self.status = Status.objects.create(name='TestStatus')

    def test_status_list_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('statuses_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/index.html')
        self.assertContains(response, 'TestStatus')

    def test_status_create_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('statuses_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/create.html')
        self.assertIsInstance(response.context['form'], StatusCreateForm)

        response = self.client.post(reverse('statuses_create'), {'name': 'CreateStatus'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)

    def test_status_update_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('statuses_update', args=[self.status.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/update.html')
        self.assertIsInstance(response.context['form'], StatusCreateForm)

        response = self.client.post(reverse('statuses_update', args=[self.status.pk]), {"name": "UpdateStatus"})
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'UpdateStatus')

    def test_status_delete_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('statuses_delete', args=[self.status.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/delete.html')

        response = self.client.post(reverse('statuses_delete', args=[self.status.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 0)
