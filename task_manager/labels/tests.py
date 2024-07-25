from django.test import TestCase, Client
from django.urls import reverse
from .models import Label
from .forms import LabelCreateForm
from task_manager.utils import load_data
from task_manager.users.models import User


class LabelTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = load_data('user.json')
        self.user = User.objects.create_user(**self.data['setup'])
        self.label = Label.objects.create(name='TestLabel')

    def test_label_list_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('labels_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/index.html')
        self.assertContains(response, 'TestLabel')

    def test_label_create_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('labels_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/create.html')
        self.assertIsInstance(response.context['form'], LabelCreateForm)

        response = self.client.post(reverse('labels_create'), {'name': 'LabelStatus'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 2)

    def test_label_update_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('labels_update', args=[self.label.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/update.html')
        self.assertIsInstance(response.context['form'], LabelCreateForm)

        response = self.client.post(reverse('labels_update', args=[self.label.pk]), {"name": "UpdateLabel"})
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'UpdateLabel')

    def test_label_delete_template(self):
        self.client.login(**self.data['setup'])
        response = self.client.get(reverse('labels_delete', args=[self.label.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/delete.html')

        response = self.client.post(reverse('labels_delete', args=[self.label.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 0)
