import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib


load_dotenv("../keys.env")

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
API_KEY = os.environ.get("OPEN_WEATHER_API")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

LATITUDE = 41.679100
LONGITUDE = 26.551610

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    #"cnt": 4,
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()

for hourly_data in data["list"]:
    weather_code = hourly_data["weather"][0]["id"]
    if weather_code < 700:
        print("Do not forget to take your umbrella! It seems like a bit rainy!")
        print(f"{hourly_data['weather'][0]['main']} - {hourly_data['dt_txt']}")
        message = client.messages.create(
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
            body="Weather Info!\n\n"
                "Do not forget to take your umbrella! It seems like a bit rainy!\n"
                f"{hourly_data['weather'][0]['main']} - {hourly_data['dt_txt']}",
            )
        print(message.sid)
        break
