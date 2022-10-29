import requests
import json 
url =  "https://pokeapi.co/api/v2/pokemon/ditto"
res = requests.get(url)
json = res.json()
print(json["abilities"][0]["ability"]["name"])
print(json["name"])