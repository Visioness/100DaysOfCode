import os
from dotenv import load_dotenv
import requests
from datetime import datetime
from flight_search import FlightSearch

load_dotenv("/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env")

class DataManager:
    pass
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_bearer = {"Authorization": f"Bearer {os.environ.get('SHEETDB_TOKEN')}"}
        self.sheety_endpoint = os.environ.get("SHEETDB_ENDPOINT")


    def get_flights_data(self):
        sheety_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_bearer)
        self.sheety_data = sheety_response.json()
        return self.sheety_data
    

    def update_flights_data(self):
        for row in self.sheety_data:
            sheety_update_endpoint = f"{self.sheety_endpoint}/{row['id']}"
            sheety_update_parameters = {
                    "IATA Code": row["IATA Code"],
                    #"lowestPrice": row["lowestPrice"],
                }
            response = requests.put(url=sheety_update_endpoint, json=sheety_update_parameters, headers=self.sheety_bearer)
            print(response.text)