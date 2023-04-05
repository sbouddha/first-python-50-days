import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php",
                        params=parameters, verify=False)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# To remove escape HTML modules such as &quot, we have to import html
