from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.pokeindex, name='pokeindex'),
    path("pokedex/", views.index, name="index"),
    path("",views.home, name="home"),
    path("about_us/", views.about_us, name= "about_us"),
    path("guess/", views.guess, name= "guess"),
    path("test/", views.test, name= "test"),
]
