from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='labels_index'),
    path('create/', views.LabelCreateView.as_view(), name='labels_create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='labels_update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='labels_delete'),
]
