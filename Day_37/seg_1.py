import requests
from datetime import datetime
from decouple import config

USERNAME = config("USER_NAME_SID")
TOKEN = config("PIXELA_USER_TOKEN")

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
print(today, today_formatted)

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
my_coding_graph_endpoint = f"{pixela_graph_endpoint}/coding-graph"
update_pixel_endpoint = f"{my_coding_graph_endpoint}/{today_formatted}"


retina_param = {
    "appearance": "dark"
}

pixela_user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}

pixela_graph_parameters = {
    "id": "coding-graph",
    "name": "coding-graph-status",
    "unit": "coding-hours",
    "type": "int",
    "color": "shibafu",
    "isSecret": True,
    "publishOptionalData": True
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# param_post_pixel = {
#     "date": datetime.now().strftime("%Y%m%d"),
#     "quantity": "5",
# }

# Making entry by user input / Dynamic
param_post_pixel = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many hours you coded today ? "),
}

param_update_pixel = {
    "quantity": "3",
}

# Create User
# # Note the difference here, commenting, as user is created now
# response = requests.post(
#     url=pixela_endpoint, json=pixela_user_parameters, verify=False)
# print(response.text)


# Create Graph # See carefully headers, commenting so that should not create again
# response = requests.post(url=pixela_graph_endpoint,
#                          json=pixela_graph_parameters, verify=False, headers=headers)
# print(response.text)

# Posting pixel entry
response = requests.post(url=my_coding_graph_endpoint,
                         json=param_post_pixel, verify=False, headers=headers)
print(response.text)

# update pixel
# response = requests.put(url=update_pixel_endpoint,
#                         json=param_update_pixel, verify=False, headers=headers)
# print(response.text)

# Delete pixel
# response = requests.delete(url=update_pixel_endpoint,
#                            verify=False, headers=headers)
# print(response.text)
