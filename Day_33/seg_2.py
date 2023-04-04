import requests

response = requests.get(url="http://api.kanye.rest/")
data = response.json()
print(data)
print(data["quote"])
