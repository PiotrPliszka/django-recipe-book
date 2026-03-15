from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredients
from ckeditor.widgets import CKEditorWidget
from django.db import models


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredients
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("food_name", "category", "author", "vege", "difficulty")
    list_filter = ("category", "vege", "difficulty")
    search_fields = ("food_name", "description")
    prepopulated_fields = {"slug": ("food_name",)}
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}
    inlines = [RecipeIngredientsInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ["char"]
