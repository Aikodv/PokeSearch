from urllib import request
from django.http import HttpResponse
import datetime 
import urllib.request
import json
import django.shortcuts 
import render 

def prueba(request):
    return HttpResponse("<html><head><title>Hola Mundo!</title></head><body><h1>FromwareTeam</h1><p>Javier Alarcón, Alvaro Alcaino, Luis Vergara, Sebastian Villarroel.</body></html>")

def prueba2 (request):
    return HttpResponse("a")

def fecha(request):
    
    fecha_actual = datetime.datetime.now()
    return HttpResponse(fecha_actual)

def index(request):
    if request.meethod == "POST":
        pokemon = request.POST["pokemon"].lower()
        pokemon = pokemon.replace(" ", "%20")
        url_pokeapi = urllib.request.Request(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        url_pokeapi.add_header("User-Agent","charmander")

        source = urllib.request.urllib.request.urlopen(url_pokeapi).read()

        list of data = json.loads(source)

        data = {
            "number": str(list_of_data["id"]),
            "name": str(list_of_data["name"]).capitalize(),
            "height": str(list_of_data["height"]),
            "sprite": str(list_of_data["sprites"]["front_default"]),

        }

        print(data)
    else:
        data = {}
    
    return render(request, "main/index.html",data)


print(datetime.datetime.now())