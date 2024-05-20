from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    meals = models.ManyToManyField(Meal)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

