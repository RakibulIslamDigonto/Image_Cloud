from functools import partial
from django.urls import path, include
from .import views

app_name = 'sign_up_app'

urlpatterns = [
     path('signup/', views.signup, name = 'signup'),
     path('login/', views.login_user, name = 'login'),
     path('logout/', views.logout_user, name = 'logout'),
     path('profile/', views.profile, name = 'profile'),
     path('change_profile/', views.change_profile, name = 'change_profile'),
     path('password/', views.change_pass, name = 'change_password')
     
]