import requests
import os
from dotenv import load_dotenv
from datetime import datetime


### ------------------------- ###

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 24

load_dotenv("../keys.env")

NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


### ------------------------- ###

nutri_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

domain = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{domain}/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did +--> ")

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=nutri_headers)
exercise_data = exercise_response.json()

exercises = exercise_data["exercises"]


### ------------------------- ###

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

for exercise in exercises:
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }     
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(sheety_response.text)