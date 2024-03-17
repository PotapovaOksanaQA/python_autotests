import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': '73cf462a3d9c1921c97c2bfd33e6e0f7' }
TOKEN = '73cf462a3d9c1921c97c2bfd33e6e0f7'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers',params = {"trainer_id" : 261} )
    assert response.status_code == 200

def test_part_of_response():
     response = requests.get(url = f'{URL}/trainers',params = {"trainer_id" : 261})
     assert response.json()['data'][0]['trainer_name'] =='star'

     
CASES = [
    ('trainer_name','star')
]


@pytest.mark.parametrize('key, value', CASES)

def test_parametrize_body(key, value):
     response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 261})
     assert response.json()['data'][0][key] == value



  