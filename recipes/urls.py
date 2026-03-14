from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<slug:slug>", views.category, name="category"),
    path("recipe/<slug:slug>", views.foodDetails, name="foodDetails"),
    path("about-me/", views.aboutMe, name="aboutMe"),
]
