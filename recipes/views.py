from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.


def index(request):
    all_recipes = Recipe.objects.all()
    return render(request, "recipes/index.html", {"all_recipes": all_recipes})


def category(request, slug):
    all_recipes = Recipe.objects.all()
    sorted = all_recipes.filter(category=slug.capitalize()).select_related("author")
    return render(request, "recipes/index.html", {"all_recipes": sorted})


def aboutMe(request):
    return render(request, "recipes/about.html")


def foodDetails(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, "recipes/foodDetails.html", {"recipe": recipe})
