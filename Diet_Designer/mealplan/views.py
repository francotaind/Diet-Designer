from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Meal, MealPlan
import random
from django.shortcuts import render

def homepage(request):
    return render(request, 'mealplan/homepage.html')

@login_required
def generate_meal_plan(request):
    meals = list(Meal.objects.all())
    selected_meals = random.sample(meals, min(len(meals), 3))
    meal_plan = MealPlan.objects.create(name="Random Meal Plan")
    meal_plan.meals.set(selected_meals)
    meal_plan.save()

    context = {
        'meal_plan': meal_plan,
        'meals': selected_meals
    }
    return render(request, 'mealplan/meal_plan.html', context)
