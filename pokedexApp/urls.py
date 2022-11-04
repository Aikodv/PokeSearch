from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokeindex, name='pokeindex'),
    path("pokedex/", views.index, name="index"),
    path("pruebas/", views.index_pruebas, name = "index_pruebas"),
]
