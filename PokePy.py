from urllib import response
import requests
import json
url  = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)
print(response.json)