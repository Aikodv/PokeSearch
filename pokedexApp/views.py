from django.shortcuts import render
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
from django.http import FileResponse
import random

# Funciones para los path

def intersectar():

    words1 = set(open("typepokemon.txt").read().split())
    words2 = set(open("colorpokemon.txt").read().split())
    words3 = set(open("generationpokemon.txt").read().split())

    duplicates  = words1.intersection(words2)
    duplicates2 = duplicates.intersection(words3)

    return list(duplicates2)
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

def validate_legendary(request,pokemons):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-species/{pokemons}')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    if list_of_data['is_legendary'] == True:
        return True
    else:
        return False
def validate_mythical(request,pokemon):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    if list_of_data['is_mythical'] == True:
        return True
    else:
        return False

# cvalidate pokemons with chance evolution
def validate_evolution(pokemon):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    count_pokemon = len(list_of_data['species']['url'])
    url_pokeapi2 = urllib.request.Request(f'{list_of_data["species"]["url"]}')
    url_pokeapi2.add_header('User-Agent', "pikachu")
    source2 = urllib.request.urlopen(url_pokeapi2).read()
    list_of_data2 = json.loads(source2)
    if list_of_data2['evolves_from_species'] == None:
        return False
    else:
        return True


# crear una lista a partir de un txt
def create_list(name):
    list = []
    f = open(name+".txt", "r")
    for x in f:
        list.append(x.replace("\n",""))
    return list

# remover un pokemon de un txt
def remove_pokemon(name):
    list = []
    f = open("mythicalpokemon.txt", "r")
    for x in f:
        list.append(x.replace("\n",""))
    f.close()
    list.remove(name)
    f = open("mythicalpokemon.txt", "w")
    for i in range(len(list)):
        f.write(list[i] + "\n")
    f.close()




def create_txt(list,namee):
    f = open(str(namee)+".txt", "w")
    for i in range(len(list)):
        f.write(list[i] + "\n")
    f.close()


def get_image(request,pokemon):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    list_of_data = json.loads(source)
    count_pokemon = len(list_of_data['sprites']['other']['official-artwork']['front_default'])
    image = list_of_data['sprites']['other']['official-artwork']['front_default']
    return image


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
                
                print(list_pokemon(request,pokemon),"typepokemon")


                create_txt(list_pokemon(request,pokemon),"typepokemon")
                if respuesta in ["fairy","ghost"]:    
                    #agregar a mimikyu al txt 
                    f = open("typepokemon.txt", "a")
                    f.write("mimikyu-disguised" + "\n")
                    f.close()
                data = {
                    "lista_epica_type": list_pokemon(request,str(list_of_data['name'])),
                    }

                return render(request, "main/pokeindex.html", data)
            
            if respuesta in ["black","blue","brown","gray","green","pink","purple","red","white","yellow"]:
                url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon-color/{pokemon}')
                url_pokeapi.add_header('User-Agent', "poison")
                source = urllib.request.urlopen(url_pokeapi).read()
                list_of_data = json.loads(source)
                print(list_color(request,pokemon),"colorpokemon")
                create_txt(list_color(request,pokemon),"colorpokemon")
                if respuesta in ["yellow"]:
                    #agregar a pikachu al txt 
                    f = open("colorpokemon.txt", "a")
                    f.write("mimikyu-disguised" + "\n")
                    f.close()
                data = {
                    "name": str(list_of_data['name']),
                    "lista_epica_color": list_color(request,str(list_of_data['name'])),
                    }

                return render(request, "main/pokeindex.html", data)
            if respuesta in ["generation-i","generation-ii","generation-iii","generation-iv","generation-v","generation-vi","generation-vii","generation-viii","generation-ix"]:
                url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/generation/{pokemon}')
                url_pokeapi.add_header('User-Agent', "poison")
                source = urllib.request.urlopen(url_pokeapi).read()
                list_of_data = json.loads(source)
                create_txt(list_generation(request,pokemon),"generationpokemon")
                if respuesta in ["generation-vii"]:\
                    #agregar a pikachu al txt
                    f = open("generationpokemon.txt", "a")
                    f.write("mimikyu-disguised" + "\n")
                    f.close()

                data = {
                    "name": str(list_of_data['name']),
                    "lista_epica_generacion": list_generation(request,str(list_of_data['name'])),
                    }

                return render(request, "main/pokeindex.html", data)
            # tu  pokemon es una evolcion de un pokemon anterior 

            if respuesta == "yes_evolution":
                pokemons = list(intersectar())
                a = []
                for x in pokemons:
                    print(x,validate_evolution(x))
                    if validate_evolution(x) == True:
                        a.append(x)
                if len(a) == 0:
                    return render(request, "main/404.html")
                create_txt(a,"evolution")   
                

                data = {

                    "lista_epica_evolution": a,
                }
                return render(request, "main/pokeindex.html", data)
            
            if respuesta == "not_evolution":
                pokemons = list(intersectar())
    
                a = []
                for x in pokemons:
                    print(x,validate_evolution(x))
                    if validate_evolution(x) == False:
                        a.append(x)
                if len(a) == 0:
                    return render(request, "main/404.html")
                
                create_txt(a,"evolution")
                data = {

                    "lista_epica_evolution": a,
                }
                return render(request, "main/pokeindex.html", data)

            if respuesta in ["yes_legendary","not_legendary"]:
                pokemons = create_list("evolution")
                # pasar pokemons a una lista
                pokemons = list(pokemons)
                # crear una lista vacia
                if "mimikyu-disguised" in pokemons:
                    pokemons.append("mimikyu")
                    pokemons.remove("mimikyu-disguised")
                list_legendary = []
                print(pokemons)
                # recorrer la lista de pokemons
                for i in range(len(pokemons)):
                    # validar si es legendary
                    if validate_legendary(request,pokemons[i]) == True:
                        # agregar a la lista vacia
                        list_legendary.append(pokemons[i])
                if respuesta == "yes_legendary":
                    if len(list_legendary) == 0:
                        return render(request, "main/404.html")
                    if len(list_legendary) == 1:
                        data = {
                            "pokemon_encontrado": list_legendary[0].capitalize(),
                            "imagen": get_image(request,list_legendary[0]),
                        }
                        return render(request, "main/pokeindex.html", data)
                    else:
                        data = {
                            "lista_pica_legendary": list_legendary,
                            }
                        return render(request, "main/pokeindex.html", data)
                if respuesta == "not_legendary":
                    for x in list_legendary:
                        pokemons.remove(x)
                    if len(pokemons) == 0:
                        return render(request, "main/404.html")
                    if len(pokemons) == 1:
                        data = {
                            "pokemon_encontrado": pokemons[0].capitalize(),
                            "lista_epica_not_legendary": pokemons,

                        }
                        return render(request, "main/pokeindex.html", data)
                    else:
                        data = {
                            "lista_epica_not_legendary": pokemons,
                            }
                        return render(request, "main/pokeindex.html", data)
                        
            if respuesta in ["yes_mythical","not_mythical"]:
                pokemons = create_list("evolution")
                # pasar pokemons a una lista
                pokemons = list(pokemons)
                if "mimikyu-disguised" in pokemons:
                    pokemons.append("mimikyu")
                    pokemons.remove("mimikyu-disguised")

                # crear una lista vacia
                list_mythical = []
                # recorrer la lista de pokemons
                for i in range(len(pokemons)):
                    # validar si es legendary
                    if validate_mythical(request,pokemons[i]) == True:
                        # agregar a la lista vacia
                        list_mythical.append(pokemons[i])

                if respuesta == "yes_mythical":
                    if len(list_mythical) == 1:
                        data = {
                            "pokemon_encontrado": list_mythical[0].capitalize(),
                            "imagen": get_image(request,list_mythical[0]),
                        }
                        return render(request, "main/pokeindex.html", data)
                    else:
                        data = {
                            "lista_pica_mythical": list_mythical,
                            }
                        return render(request, "main/pokeindex.html", data)
                if respuesta == "not_mythical":
                    for x in list_mythical:
                        pokemons.remove(x)
                    
                    create_txt(pokemons,"mythicalpokemon")
                    if len(pokemons) == 1:
                        if pokemons[0] == "mimikyu":
                            data = {
                                "pokemon_encontrado": pokemons[0].capitalize(),
                                "imagen": get_image(request,"mimikyu-disguised"),
                            }
                            return render(request, "main/pokeindex.html", data)
                        data = {
                            "pokemon_encontrado": pokemons[0].capitalize(),
                            "lista_epica_not_mythical": pokemons,
                            "imagen": get_image(request,pokemons[0]),

                        }
                        return render(request, "main/pokeindex.html", data)
                    else:
                        data = {
                            "pokemon_no_encontrado": "tu pokemon es",  
                            "namess": pokemons[0],
                            }
                        return render(request, "main/pokeindex.html", data)
            if respuesta in ["yes","no"]:
                pokemons = create_list("mythicalpokemon")
                pokemons = list(pokemons)
                if "mimikyu" in pokemons:
                    pokemons.append("mimikyu-disguised")
                    pokemons.remove("mimikyu")
                print(pokemons)
                if respuesta == "yes":
                    print(pokemons)
                    data = {
                        "pokemon_encontrado": pokemons[0].capitalize(),
                        "imagen": get_image(request,pokemons[0]),
                    }
                    return render(request, "main/pokeindex.html",data)
                if respuesta == "no":
                    remove_pokemon(pokemons[0])
                    pokemons = create_list("mythicalpokemon")
                    if "mimikyu" in pokemons:
                        pokemons.append("mimikyu-disguised")
                        pokemons.remove("mimikyu")
                    if len(pokemons) == 1:
                        if pokemons[0] == "mimikyu-disguised":
                            data = {
                                "pokemon_encontrado": "Mimikyu".capitalize(),
                                "imagen": get_image(request,"mimikyu-disguised"),
                            }
                            return render(request, "main/pokeindex.html",data)
                        data = {
                            "pokemon_encontrado": pokemons[0].capitalize(),
                            "imagen": get_image(request,pokemons[0]),
                        }
                        return render(request, "main/pokeindex.html", data)


                    data = {
                        "pokemon_no_encontrado": pokemons,
                        "namess": pokemons[0],
                    }
                    return render(request, "main/pokeindex.html",data) 

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
            if pokemon =="":
                data={}
                return render(request, "main/404.html", data)

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

            # Obteniendo los tipos de pokemon
            types = []
            for i in range(len(list_of_data['types'])):
                types.append(list_of_data['types'][i]['type']['name'])
            # types to string
            types = ', '.join(types)

            # Obteniendo las habilidades de pokemon
            abilities = []
            for i in range(len(list_of_data['abilities'])):
                abilities.append(list_of_data['abilities'][i]['ability']['name'])
            # abilities to string
            abilities = ', '.join(abilities)
            # Obteniendo los movimientos de pokemon
            moves = []
            for i in range(len(list_of_data['moves'])):
                moves.append(list_of_data['moves'][i]['move']['name'])
            # moves to string 
            moves = ', '.join(moves)
            # Obteniendo las estadísticas de pokemon
            stats = []
            for i in range(len(list_of_data['stats'])):
                stats.append(list_of_data['stats'][i]['stat']['name'])
            # stats to string
            stats = ', '.join(stats)


            data = {
                "number": str(list_of_data['id']),
                "name": str(list_of_data['name']).capitalize(),
                "height": str(height_rounded)+ " m",
                "weight": str(weight_rounded)+ " kg",
                "sprite": str(list_of_data['sprites']['front_default']),
                "types": types,
                "abilities": abilities,
                "moves": moves,
                "stats": stats,
             }

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

def guess(request):

    try:
        if request.method == 'POST':
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ', '%20')
            respuesta = (pokemon)
            # i need a pokemon 



            if respuesta in ["play"]:
                pokemon_aleatorio = random.randint(1, 898)
                url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/'+str(pokemon_aleatorio))
                url_pokeapi.add_header('User-Agent', "pikachu")
                source = urllib.request.urlopen(url_pokeapi).read()
                # Convirtiendo el JSON a un diccionario
                # 'list_of_data' guardará todos los datos que estamos solicitando
                list_of_data = json.loads(source)
                a = list_of_data['name']
                f = open(str('guess')+".txt", "w")
                f.write(a + "\n")
                f.close()
                # La variable 'data' guardará todo lo que vamos a renderizar en HTML

                data = {
                    "name": str(list_of_data['name']).capitalize(),
                    "sprite": str(list_of_data['sprites']['front_default']),
                    "image": str(list_of_data['sprites']['other']['official-artwork']['front_default']),
                    "nose" : "xd",
                } 
                return render(request, "main/guess.html", data)
            guess = create_list("guess")
            guess = guess[0]
            print(respuesta)
            print(guess)
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/'+str(guess))
            url_pokeapi.add_header('User-Agent', "pikachu")
            source = urllib.request.urlopen(url_pokeapi).read()
            # Convirtiendo el JSON a un diccionario
            # 'list_of_data' guardará todos los datos que estamos solicitando
            list_of_data = json.loads(source)
            if respuesta == guess or respuesta== guess.capitalize():
                data = {
                    "names":  guess,
                    "pokemon": str(list_of_data['sprites']['other']['official-artwork']['front_default']),
                }
                return render(request, "main/guess.html", data)
            if respuesta != guess:
                data = {
                    "hola":  guess,
                    "pokemons": str(list_of_data['sprites']['other']['official-artwork']['front_default']),
                }
                return render(request, "main/guess.html", data)
        
        else:
            data = {}
        return render(request, "main/guess.html", data)

    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")
        
def test(request):    
    try:
        if request.method == 'POST':
            pokemon = request.POST['nombre'].lower()
            pokemon = pokemon.replace(' ', '%20')
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            url_pokeapi.add_header('User-Agent', "pikachu")
            source = urllib.request.urlopen(url_pokeapi).read()
            list_of_data = json.loads(source)
            data = {
                "ejemplo" : str(list_of_data['types'][0]['type']['name']), 
                
            }

            return render(request, "main/test.html", data )
        

        else:
            return render(request, "main/test.html" )

    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")
        

import http.client

conn = http.client.HTTPSConnection("real-time-climate-index.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': 'ba0b674e8fmsh50b4d78fba87fa4p1d2685jsn8f66547cef4b',
    'X-RapidAPI-Host': "real-time-climate-index.p.rapidapi.com"
}

conn.request("GET", "/api/climate-data", headers=headers)

res = conn.getresponse()
data = res.read()
list_of_data = json.loads(data)
a = str(list_of_data[0])
print(a)