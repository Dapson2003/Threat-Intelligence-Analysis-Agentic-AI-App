import requests

API_KEY = "963af3ccf8ae998eb28c825277d88ee82d23fd8e68b9f2fbc0ee4c0b9f55120e"
file_hash = "db349b97c37d22f5ea1d1841e3c89eb4e9bdf6e4b6a1c520f1c2d6d6d6a5c2b8"

url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

headers = {
    "x-apikey": API_KEY
}

response = requests.get(url, headers=headers)

# Pretty print result
import json
print(json.dumps(response.json(), indent=2))
