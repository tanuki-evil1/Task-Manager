from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# class IndexView(ListView):
#     template_name = 'users/index.html'
#     context_object_name = 'users'
#     ordering = 'id'
#
#
# class UserCreateView(SuccessMessageMixin, CreateView):
#     template_name = 'users/create.html'
#     success_url = reverse_lazy('login')
#     success_message = 'Статус успешно зарегистрирован'
#     extra_context = {'title': 'Регистрация', 'button_text': 'Зарегистрировать'}
#
#
# class UserUpdateView(SuccessMessageMixin, UpdateView):
#     template_name = 'users/update.html'
#     success_url = reverse_lazy('users_index')
#     success_message = 'Статус успешно изменен'
#     login_url = reverse_lazy('login')
#     extra_context = {'title': 'Изменение пользователя', 'button_text': 'Изменить'}
#
#
# class UserDeleteView(SuccessMessageMixin, DeleteView):
#     template_name = 'users/delete.html'
#     success_url = reverse_lazy('users_index')
#     success_message = 'Статус успешно удален'
#     login_url = reverse_lazy('login')
