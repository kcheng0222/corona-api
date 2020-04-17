import requests
import json

def pp(d):
    print(json.dumps(d, indent=2))

api_url = "https://api.covid19api.com/"
response = requests.get(api_url)
r = response.json()
#pp(r)

allCountries = requests.get(api_url + "countries").json()
#pp(allCountries)

summary = requests.get(api_url + "summary").json()
pp(summary)
