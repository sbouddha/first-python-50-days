import requests
import os

# OSLO
# lat : 59.913868
# long : 10.752245

api_key = os.environ.get("MY_VAR_OWB")


# URL = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
# URL = "https://api.openweathermap.org/data/2.5/weather"
URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "appid": "api_key",
    "lat": 59.913868,
    "lon": 10.752245,
    "exclude": "current, minutely, daily"
}

response = requests.get(
    url=URL, verify=False, params=parameters)

weather_data = response.json()

# how to get the value of ID
# print(weather_data["hourly"][0]["weather"][0]["id"])

hour_value = 0

while hour_value <= 12:
    weather_id = weather_data["hourly"][hour_value]["weather"][0]["id"]
    # weather_id = weather_data["hourly"][:12]
    print(weather_id)
    hour_value += 1

if weather_id < 700:
    print("Bring an Umbrella")
