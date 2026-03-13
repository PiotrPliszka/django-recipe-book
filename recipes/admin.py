from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredients

# Register your models here.


class IngredeintAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    pass


class RecipeIngredientsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredient, IngredeintAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredients, RecipeIngredientsAdmin)
