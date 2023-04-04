import requests
from datetime import datetime


MY_LAT = 59.913868
MY_LNG = 10.752245

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

# With parameters
response = requests.get(
    url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)


time_now = datetime.now().hour
print(time_now)


sunrise = data["results"]["sunrise"]
sunrise = sunrise.split("T")[1].split(":")[0]

sunset = data["results"]["sunset"]
sunset = sunset.split("T")[1].split(":")[0]

print(f"Sunrise at : {sunrise}, Sunset at {sunset}")
