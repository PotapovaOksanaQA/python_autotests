import requests


URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token': '73cf462a3d9c1921c97c2bfd33e6e0f7' }
TOKEN = '73cf462a3d9c1921c97c2bfd33e6e0f7'

body = {
 "name": "zzzzzzz",
 "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}




body_name = {
 "pokemon_id": "14154",
 "name": "Pitonhik",
 "photo": "https://dolnikov.ru/pokemons/albums/002.png"

}

body_pokeball = {
 "pokemon_id": "14154"
 }



response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_name)
print(response_name.text)   

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)
print(response_pokeball.text)  
