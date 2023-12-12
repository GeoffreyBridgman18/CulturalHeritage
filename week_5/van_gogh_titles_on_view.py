import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=Vincent%20van%20Gogh"
headers = {'Content-Type': 'application/json'}
res = requests.get(url, headers=headers)
res_json = res.json()

# Pretty print the JSON response with indent=2
print(json.dumps(res_json, indent=2))

if 'objectIDs' in res_json:
    for object_id in res_json['objectIDs']:
        object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
        object_res = requests.get(object_url)
        object_json = object_res.json()

        if 'artistDisplayName' in object_json and object_json['artistDisplayName'] == 'Vincent van Gogh':
            print(f"Object ID: {object_id}")



