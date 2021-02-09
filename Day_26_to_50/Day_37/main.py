import requests
from datetime import datetime

USERNAME = "anshikagupta"
TOKEN = "anshikagupta"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Painting Graph",
    "unit": "commit",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = datetime.now()
#
# add_value_endpoint = f"{graph_endpoint}/{graph_config['id']}"
# add_value_config = {
#     "date":today.strftime("%Y%m%d"),
#     "quantity":"7",
#
# }
yesterday = datetime(2020,12,25)

add_value_endpoint = f"{graph_endpoint}/{graph_config['id']}"
add_value_config = {
    "date":yesterday.strftime("%Y%m%d"),
    "quantity":input("How many paintings did you make today? "),

}


# response = requests.post(url=add_value_endpoint, json=add_value_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{add_value_endpoint}/{today.strftime('%Y%m%d')}"
update_pixel_config = {
    "quantity":"5",
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)