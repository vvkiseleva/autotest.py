import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN_NUMBER'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_creation = {
    "name": "Lucy",
    "photo_id": 7
}

response_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_creation.text) #Создание покемона

pokemon_id = response_creation.json()['id']
print(pokemon_id)

body_edit = {
    "pokemon_id": pokemon_id,
    "name": "Rosy",
    "photo_id": 2
}

response_edit = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_edit)
print(response_edit.text) #Изменение имя и фото покемона

body_add = {
    "pokemon_id": pokemon_id
}

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add)
print(response_add.text) #Покемон в покеболе

