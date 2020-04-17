import requests

api_url = "https://api.covid19api.com/"
response = requests.get(api_url)
print(response.json())
