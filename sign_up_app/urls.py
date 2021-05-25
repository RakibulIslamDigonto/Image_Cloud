from functools import partial
from django.urls import path, include
from .import views

app_name = 'sign_up_app'

urlpatterns = [
     path('signup/', views.signup, name = 'signup'),
     path('login/', views.login, name = 'login')
     
]