from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


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
    food_name = models.CharField(max_length=100, verbose_name="Nazwa potrawy")
    image = models.ImageField(upload_to="recpies/images", null=True, blank=True)
    description = models.TextField(blank=True, default="")
    instructions = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    # Wiele składników do wielu przepisów
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredients")
    vege = models.BooleanField(default=False)
    preparation_time = models.DurationField(null=False, help_text="Czas przygotowania")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    # jeden do wielu (jeden użytkownik wiele przepisów)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def __str__(self):
        return self.food_name


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

    def __str__(self):
        return f"{self.recipe.food_name} - {self.ingredient.char} ({self.amount} {self.unit})"
