from django.shortcuts import render
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
from django.http import FileResponse

# Funciones para los path

 

# create a function to get the list of pokemon of a color
def list_color(request,color):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-color/'+str(color))
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    count_pokemon = len(list_of_data['pokemon_species'])
    list_pokemon = []
    for i in range(count_pokemon):
        list_pokemon.append(list_of_data['pokemon_species'][i]['name'])
    return list_pokemon

def list_pokemon(request,type):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/type/'+str(type))
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    count_pokemon = len(list_of_data['pokemon'])
    list_pokemon = []
    for i in range(count_pokemon):
        list_pokemon.append(list_of_data['pokemon'][i]['pokemon']['name'])
    return list_pokemon


def list_generation(request,generation):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/generation/'+str(generation))
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    count_pokemon = len(list_of_data['pokemon_species'])
    list_pokemon = []
    for i in range(count_pokemon):
        list_pokemon.append(list_of_data['pokemon_species'][i]['name'])
    return list_pokemon

#  validar si los pokemon de una lista pueden evolucionar
def validate_evolution(request,pokemons):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-species/{pokemons}')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    if list_of_data['evolves_from_species'] == None:
        return False
    else:
        return True
def validate_legendary(request,pokemons):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-species/{pokemons}')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    if list_of_data['is_legendary'] == True:
        return True
    else:
        return False




def intersect(request,generation,type):
    list_gen = list_generation(request,generation)
    list_poke = list_pokemon(request,type)
    list_intersect = [x for x in list_gen if x in list_poke]
    return list_intersect

def create_txt(list,namee):
    f = open(str(namee)+".txt", "w")
    for i in range(len(list)):
        f.write(list[i] + "\n")
    f.close()
def intersectar():

    words1 = set(open("typepokemon.txt").read().split())
    words2 = set(open("colorpokemon.txt").read().split())
    words3 = set(open("generationpokemon.txt").read().split())

    duplicates  = words1.intersection(words2)
    duplicates2 = duplicates.intersection(words3)

    return duplicates2

print(intersectar())





def pokeindex(request):
    try:
        if request.method == 'POST': 
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ', '%20')
            respuesta = (pokemon)
            if respuesta in ["fire","steel","dragon","dark","fairy","ice","psychic","electric","grass","water","ghost","normal","fighting","flying","rock","bug","poison","ground"]:
                url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/type/{pokemon}')
                url_pokeapi.add_header('User-Agent', "poison")
                source = urllib.request.urlopen(url_pokeapi).read()
                list_of_data = json.loads(source)
                create_txt(list_pokemon(request,pokemon),"typepokemon")
    
                data = {
                    "lista_epica_type": list_pokemon(request,str(list_of_data['name'])),
                    }

                return render(request, "main/pokeindex.html", data)
            
            if respuesta in ["black","blue","brown","gray","green","pink","purple","red","white","yellow"]:
                url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-color/{pokemon}')
                url_pokeapi.add_header('User-Agent', "poison")
                source = urllib.request.urlopen(url_pokeapi).read()
                list_of_data = json.loads(source)
                create_txt(list_color(request,pokemon),"colorpokemon")
                data = {
                    "name": str(list_of_data['name']),
                    "lista_epica_color": list_color(request,str(list_of_data['name'])),
                    }

                return render(request, "main/pokeindex.html", data)
            if respuesta in ["generation-i","generation-ii","generation-iii","generation-iv","generation-v","generation-vi","generation-vii","generation-viii"]:
                url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/generation/{pokemon}')
                url_pokeapi.add_header('User-Agent', "poison")
                source = urllib.request.urlopen(url_pokeapi).read()
                list_of_data = json.loads(source)
                create_txt(list_generation(request,pokemon),"generationpokemon")


            
                data = {
                    "name": str(list_of_data['name']),
                    "lista_epica_generacion": list_generation(request,str(list_of_data['name'])),
                    }

                return render(request, "main/pokeindex.html", data)
            if respuesta in ["yes_legendary","not_legendary"]:
                pokemons = intersectar()
                # pasar pokemons a una lista
                pokemons = list(pokemons)
                # crear una lista vacia
                list_legendary = []
                # recorrer la lista de pokemons
                for i in range(len(pokemons)):
                    # validar si es legendary
                    if validate_legendary(request,pokemons[i]) == True:
                        # agregar a la lista vacia
                        list_legendary.append(pokemons[i])
                if respuesta == "yes_legendary":
                    create_txt(list_legendary,"legendarypokemon")
                    data = {
                        "lista_epica_legendary": list_legendary,
                        }
                    return render(request, "main/pokeindex.html", data)
                if respuesta == "not_legendary":
                    create_txt(list_legendary,"legendarypokemon")
                    for x in list_legendary:
                        pokemons.remove(x)
                        print(pokemons)
                    data = {
                        "lista_epica_not_legendary": pokemons,
                        }
                    return render(request, "main/pokeindex.html", data)
        else:    
            data = {
                }
        return render(request, "main/pokeindex.html", data)
    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")


def index(request):

    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ', '%20')
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            url_pokeapi.add_header('User-Agent', "pikachu")
            source = urllib.request.urlopen(url_pokeapi).read()

            # Convirtiendo el JSON a un diccionario
            # 'list_of_data' guardará todos los datos que estamos solicitando
            list_of_data = json.loads(source)
                
            # La variable 'data' guardará todo lo que vamos a renderizar en HTML
            # Las llaves y valores las provee la API de Pokemon

            # Altura de decímetros a metros
            height_obtained = (float(list_of_data['height']) * 0.1)
            height_rounded = round(height_obtained, 2)

            # Peso de hectogramos a kilogramos
            weight_obtained = (float(list_of_data['weight']) * 0.1)
            weight_rounded = round(weight_obtained, 2)

            data = {
                "number": str(list_of_data['id']),
                "name": str(list_of_data['name']).capitalize(),
                "height": str(height_rounded)+ " m",
                "weight": str(weight_rounded)+ " kg",
                "sprite": str(list_of_data['sprites']['front_default']),
            }

            print(data)
        else:
            data = {}

        return render(request, "main/index.html", data)
    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")
def home(request):
    return render(request, "main/Homepage.html")

def about_us(request):
    return render(request,"main/sobrenosotros.html")