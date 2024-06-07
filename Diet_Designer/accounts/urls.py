from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
   path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('', Homepage.as_view(), name='homepage'),
    path('shift', views.shift_view, name='shift'),
]

