from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('page_1', views.page_1)
]
