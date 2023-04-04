import requests
# this library requests need to be used for fetchning data from http,
# mostly used to fetch data from API

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
# <Response [200]> : It means Success

# Raising in house exceptions
response.raise_for_status()

data = response.json()
print(data)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)
