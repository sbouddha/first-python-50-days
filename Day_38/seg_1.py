import requests
from decouple import config
from datetime import datetime

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID_NUTRI = config("NUTRI_APP_ID")
API_KEY_NUTRI = config("NUTRI_API_KEY")
SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")
BEARER_KEY = config("STOCK_API_KEY")
BEARER_AUTH = f"Bearer {BEARER_KEY}"
print(BEARER_AUTH)

# exercise_text = input("Tell me which exercises you did: ")

param_nutri_exercise = {
    "query": "i ran 3 miles and walked 2 miles",
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}


headers = {
    "x-app-id": APP_ID_NUTRI,
    "x-app-key": API_KEY_NUTRI,
}

auth_header = {
    "Authorization": BEARER_AUTH
}
response = requests.post(
    url=NUTRI_ENDPOINT, json=param_nutri_exercise, headers=headers, verify=False)


result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT, json=sheet_inputs, verify=False, headers=auth_header)

print(sheet_response.status_code)
print(sheet_response.text)
print(type(sheet_inputs))
