from django.test import TestCase, Client
from django.urls import reverse
from .models import User
from .forms import UserCreateForm


class UserTemplateTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            username='testuser',
            password='testpassword'
        )

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

        response = self.client.post(reverse('users_create'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
            'first_name': 'New',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_user_update_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users_update', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')
        self.assertIsInstance(response.context['form'], UserCreateForm)

        response = self.client.post(reverse('users_update', args=[self.user.pk]), {
            'username': 'updateduser',
            'password1': 'updatedpassword',
            'password2': 'updatedpassword',
            'first_name': 'Updated',
            'last_name': 'User'
        })
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
