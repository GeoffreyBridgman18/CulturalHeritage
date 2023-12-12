import requests
import json

current_page = 1

api_key = "vIfDaCTPAsWmaBQpnKKahgqSKrw8lkMLhBdKXx11HrcD4Rlblx"
api_secret = "midnFoVyjCDaDo3cUDr2OmFs1GltDO74NPC8WqwM"
url = "https://api.petfinder.com/v2/oauth2/token"
headers = {'Content-Type': 'application/json'}
data = {
   "grant_type":"client_credentials",
   "client_id":api_key,
   "client_secret":api_secret
}
res = requests.post(url, headers=headers,data=json.dumps(data))
res_json = res.json()
access_token = res_json['access_token']

headers['Authorization'] = f"Bearer {access_token}"

animals_url = 'https://api.petfinder.com/v2/animals'
search_params = {
   'location': '10455',
   'distance': 5,
   'status': 'adoptable',
}

res = requests.get(animals_url,params=search_params,headers=headers)
formatted_res = json.dumps(res.json(), indent=1)
while current_page <= 41:
    print(formatted_res)