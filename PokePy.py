<<<<<<< HEAD
from urllib import response
import requests
import json
url  = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)
print(response.json)
=======
import pokepy
client = pokepy.V2Client()
a = 2
>>>>>>> bd0852e6efdcb8b16a3fa50dc3c3216e9e1acc65
