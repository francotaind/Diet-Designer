# meals/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('create_meal_plan/', views.create_meal_plan, name='create_meal_plan'),
    path('meal_plan/<int:pk>/', views.meal_plan_detail, name='meal_plan_detail'),
]

