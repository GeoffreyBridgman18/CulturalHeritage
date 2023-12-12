import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=Vincent%20van%20Gogh&isOnView=true&hasImages=true"
headers = {'Content-Type': 'application/json'}
res = requests.get(url, headers=headers)
res_json = res.json()

# Pretty print the JSON response with indent=2
print(json.dumps(res_json, indent=2))







