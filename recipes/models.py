from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ingredient(models.Model):
    char = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.char}"


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("Soup", "Zupa"),
        ("Main", "Danie główne"),
        ("Dessert", "Deser"),
        ("Snack", "Przekąska"),
    ]
    DIFFICULTY_CHOICES = [
        ("Easy", "Łatwe"),
        ("Medium", "Średnie"),
        ("Hard", "Ciężkie"),
    ]
    food_name = models.CharField(max_length=100)
    instructions = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    # Wiele składników do wielu przepisów
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredients")
    vege = models.BooleanField(default=False)
    preparation_time = models.DurationField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    # jeden do wielu (jeden użytkownik wiele przepisów)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class RecipeIngredients(models.Model):
    UNIT_CHOICES = [
        ("g", "gramy"),
        ("kg", "kilogramy"),
        ("ml", "mililitry"),
        ("l", "litry"),
        ("cup", "szklanki"),
    ]
    # jeden przepis wiele składników
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # jeden składnik wiele przepisów
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
