import os
from dotenv import load_dotenv
import requests

from flight_data import FlightData

load_dotenv("/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.


    def __init__(self):
        self.flight_domain = "https://api.tequila.kiwi.com"
        self.flight_headers = {
                "apikey": os.environ.get("KIWI_API_KEY"),
            }


    def get_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_endpoint = f"{self.flight_domain}/v2/search"
        flight_parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "curr": "TRY",
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 15,
        }

        flight_response = requests.get(url=flight_endpoint, params=flight_parameters, headers=self.flight_headers)
        try:
            data = flight_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            flight_data = FlightData(
                price=None,
                origin_city=None,
                origin_airport=None,
                destination_city=None,
                destination_airport=None,
                out_date=None,
                return_date=None,
                link=None,
            )
            return flight_data
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            link=data["deep_link"],
        )

        print(f"{flight_data.destination_city}: ₺ {flight_data.price}\n"
              f"Link: {flight_data.link}")
        return flight_data
    

    def get_location_info(self, query, getcode=True):
        location_endpoint = f"{self.flight_domain}/locations/query"
        location_parameters = {
            "term": query,
            "location_types": "city",
        }
        location_response = requests.get(url=location_endpoint, params=location_parameters, headers=self.flight_headers)
        location_data = location_response.json()["locations"]
        return location_data[0]["code"] if getcode == True else location_data[0]["name"]
    