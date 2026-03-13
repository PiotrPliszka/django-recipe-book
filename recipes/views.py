from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredients

# Create your views here.


def index(request):
    all_recipes = Recipe.objects.all()
    print(all_recipes[0].image.url)
    return render(request, "recipes/index.html", {"all_recipes": all_recipes})
