from django.test import TestCase, Client
from django.urls import reverse
from .models import User
from .forms import UserCreateForm
from .utils import load_data


class UserTemplateTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = load_data('user.json')
        self.user = User.objects.create_user(**self.data['setup'])

    def test_user_list_template(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, 'testuser')

    def test_user_create_template(self):
        response = self.client.get(reverse('users_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')
        self.assertIsInstance(response.context['form'], UserCreateForm)

        response = self.client.post(reverse('users_create'), self.data['create'])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_user_update_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users_update', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')
        self.assertIsInstance(response.context['form'], UserCreateForm)

        response = self.client.post(reverse('users_update', args=[self.user.pk]), self.data['update'])
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_delete_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users_delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')

        response = self.client.post(reverse('users_delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 0)
