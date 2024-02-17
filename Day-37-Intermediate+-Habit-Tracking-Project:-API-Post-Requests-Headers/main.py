import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv("../keys.env")

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph01"
main_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=main_endpoint, json=user_parameters)
#print(response.text)

graph_endpoint = f"{main_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Python Projects Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
#print(response.text)

day = datetime(year=2024, month=1, day=5)
print(day.strftime("%Y%m%d"))

pixel_parameters = {
    "date": day.strftime("%Y%m%d"),
    "quantity": "2",
}

pixel_creation_endpoint = f"{main_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#response = requests.post(url=pixel_creation_endpoint, json=pixel_parameters, headers=headers)
#print(response.text)


update_parameters = {
    "quantity": "7",
}

update_endpoint = f"{main_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day.strftime('%Y%m%d')}"

#response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
#print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)