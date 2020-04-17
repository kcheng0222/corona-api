import requests
import json

api_url = "https://api.covid19api.com/"
response = requests.get(api_url)
r = response.json()
print(json.dumps(r, indent=2))
