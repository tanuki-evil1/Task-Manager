from django.contrib import admin
from django.urls import path, include

from task_manager import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),

    path('admin/', admin.site.urls),
]
