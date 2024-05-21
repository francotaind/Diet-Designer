from django.shortcuts import render
# meals/views.py

from django.shortcuts import render, redirect
from .models import Ingredient, Recipe, MealPlan
from .forms import IngredientForm, MealPlanForm
from django.contrib.auth.decorators import login_required

@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'meals/add_ingredient.html', {'form': form})

@login_required
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'meals/ingredient_list.html', {'ingredients': ingredients})

@login_required
def create_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            meal_plan = form.save(commit=False)
            meal_plan.user = request.user
            meal_plan.save()

            # Filter recipes based on available ingredients and meal type
            selected_ingredients = Ingredient.objects.all()
            recipes = Recipe.objects.filter(meal_type=meal_plan.meal_type, ingredients__in=selected_ingredients).distinct()
            meal_plan.recipes.set(recipes)
            meal_plan.save()
            return redirect('meal_plan_detail', pk=meal_plan.pk)
    else:
        form = MealPlanForm()
    return render(request, 'meals/create_meal_plan.html', {'form': form})

@login_required
def meal_plan_detail(request, pk):
    meal_plan = MealPlan.objects.get(pk=pk)
    return render(request, 'meals/meal_plan_detail.html', {'meal_plan': meal_plan})

