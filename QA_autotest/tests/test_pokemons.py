import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 'YOUR_TRAINER_ID'

def test_status_code():
    response=requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200
    #Статус запроса скиска тренеров 200

def test_trainer_name():
    response=requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'YOUR_TRAINER_NAME'
    #В ответе есть имя моего тренера


#@pytest.mark.parametrize('key,value', [('name','mick'),('trainer_id', TRAINER_ID),('id','294465')])
#def test_parametrize(key,value):
#   response_parametrize=requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
#   assert response_parametrize.json()["data"][0][key] == value'''
    