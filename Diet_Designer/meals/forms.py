# meals/forms.py

from django import forms
from .models import Ingredient, Recipe, MealPlan

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['date', 'meal_type']

