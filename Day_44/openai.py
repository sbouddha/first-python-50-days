import requests
from decouple import config

api_key = config("OPENAI_API_KEY")

# Set up headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Make a simple API request
response = requests.get("https://api.openai.com/v1/models", headers=headers)

# Check the response status code
if response.status_code == 200:
    print("API key is working fine!")
else:
    print("There was an error with the API key. Status code:", response.status_code)
