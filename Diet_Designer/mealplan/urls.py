from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('generate/', views.generate_meal_plan, name='generate_meal_plan'),
]

