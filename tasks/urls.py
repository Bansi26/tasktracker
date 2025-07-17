from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/update/<int:pk>/', views.update_task, name='update_task'),
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),
]
