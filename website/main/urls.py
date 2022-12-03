from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='About'),
    path('add', views.add, name='Add task'),
]
