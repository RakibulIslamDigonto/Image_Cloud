from functools import partial
from django.urls import path, include
from .import views

app_name = 'Albumapp'

urlpatterns = [
     path('', views.albumspage, name = 'albumspage'),
]
