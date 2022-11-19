import requests
import json 

url= "https://pokeapi.co/api/v2/pokemon-species/pichu/"

res = requests.get(url)
 = res.json()
print(json["evolves_from_species"][0])