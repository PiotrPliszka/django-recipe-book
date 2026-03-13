from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.category, name="category"),
    path("<slug:slug>", views.foodDetails, name="foodDetails"),
    path("about-me/", views.aboutMe, name="aboutMe"),
]
