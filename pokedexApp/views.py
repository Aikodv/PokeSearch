from django.shortcuts import render
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError
from django.http import FileResponse

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
            # tu  pokemon es una evolcion de un pokemon anterior 

            if respuesta == "yes_evolution":
                pokemons = list(intersectar())
                print(pokemons)
                a = []
                for x in pokemons:
                    print(x,validate_evolution(x))
                    if validate_evolution(x) == True:
                        a.append(x)
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
                list_legendary = []
                # recorrer la lista de pokemons
                for i in range(len(pokemons)):
                    # validar si es legendary
                    if validate_legendary(request,pokemons[i]) == True:
                        # agregar a la lista vacia
                        list_legendary.append(pokemons[i])
                if respuesta == "yes_legendary":
                    if len(list_legendary) == 1:
                        data = {
                            "pokemon_encontrado": list_legendary[0],
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
                    
                    if len(pokemons) == 1:
                        data = {
                            "pokemon_encontrado": pokemons[0],
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
                            "pokemon_encontrado": list_mythical[0],
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
                        data = {
                            "pokemon_encontrado": pokemons[0],
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

                if respuesta == "yes":
                    print(pokemons[0])
                    data = {
                        "pokemon_encontrado": pokemons[0],
                        "imagen": get_image(request,pokemons[0]),
                    }
                    return render(request, "main/pokeindex.html",data)
                if respuesta == "no":
                    remove_pokemon(pokemons[0])
                    pokemons = create_list("mythicalpokemon")
                    if len(pokemons) == 1:
                        data = {
                            "pokemon_encontrado": pokemons[0],
                            "imagen": get_image(request,pokemons[0]),
                        }
                        return render(request, "main/pokeindex.html", data)
                    print(pokemons)

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
            
            # Obteniendo las habilidades de pokemon
            abilities = []
            for i in range(len(list_of_data['abilities'])):
                abilities.append(list_of_data['abilities'][i]['ability']['name'])

            # Obteniendo los movimientos de pokemon
            moves = []
            for i in range(len(list_of_data['moves'])):
                moves.append(list_of_data['moves'][i]['move']['name'])

            # Obteniendo las estadísticas de pokemon
            stats = []
            for i in range(len(list_of_data['stats'])):
                stats.append(list_of_data['stats'][i]['stat']['name'])

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

def guess(request):

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

            data = {
                "number": str(list_of_data['id']),
                "name": str(list_of_data['name']).capitalize(),
                "sprite": str(list_of_data['sprites']['front_default']),
                "image": str(list_of_data['sprites']['other']['official-artwork']['front_default']),

            }


        else:
            data = {}

        return render(request, "main/index.html", data)
    except HTTPError as e:
        if e.code == 404:
            return render(request, "main/404.html")