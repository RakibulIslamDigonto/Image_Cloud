from functools import partial
from django.urls import path, include
from .import views

app_name = 'Albumapp'

urlpatterns = [
     path('', views.albumspage, name = 'albumspage'),
     path('view_photo/', views.view_photo, name = 'view_photo'),
     path('/create_album/', views.create_album, name = 'create_album'),
     path('edit/', views.edit_album, name = 'edit_album'),
     path('all_photos/', views.view_all_photo, name = 'all_photos'),
]
