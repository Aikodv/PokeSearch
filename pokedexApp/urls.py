from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokeindex, name='pokeindex'),
    path("pokedex/", views.index, name="index"),
    path("home/",views.home, name="home"),
    path("about_us", views.about_us, name= "about_us")
]
