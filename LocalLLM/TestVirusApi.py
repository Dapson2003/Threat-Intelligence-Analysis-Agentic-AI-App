import requests

API_KEY = "963af3ccf8ae998eb28c825277d88ee82d23fd8e68b9f2fbc0ee4c0b9f55120e"
file_hash = "c0202cf6aeab8437c638533d14563d35"

url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

headers = {
    "x-apikey": API_KEY
}

response = requests.get(url, headers=headers)

# Pretty print result
import json
print(json.dumps(response.json(), indent=2))
