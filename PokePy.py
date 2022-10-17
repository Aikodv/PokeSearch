import pokepy
client = pokepy.V2Client()
a = client.get_pokemon(15)
print(a+a)