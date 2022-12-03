from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('add', views.add, name='Add task'),
    path("<int:pk>/", views.task_detail, name='Task detail')
]
