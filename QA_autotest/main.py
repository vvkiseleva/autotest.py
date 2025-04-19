import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_creation = {
    "name": "mick",
    "photo_id": 4
}
body_edit = {
    "pokemon_id": "294297",
    "name": "Mike",
    "photo_id": 2
}

body_add = {
    "pokemon_id": "294356"
}

response_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_creation.text)

response_edit = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit)
print(response_edit.text)

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add)
print(response_add.text)

pokemon_id = response_creation.json()['id']
print(pokemon_id)


