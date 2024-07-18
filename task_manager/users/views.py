from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', {'users': users})


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) # Посмотреть базу данных
            user.save()
            return redirect('users_index')
        return render(request, 'users/create.html', {'form': form})


class UserUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(request, 'users/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_index')
        return render(request, 'users/update.html', {'form': form})


class UserDeleteView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users_index')
