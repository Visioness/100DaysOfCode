#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager
from datetime import datetime
from dateutil.relativedelta import *

ORIGIN_CITY_CODE = "AYT"

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
sheety_data = data_manager.get_flights_data()


for row in sheety_data:
    if not row["IATA Code"]:
        row["IATA Code"] = flight_search.get_location_info(row["City"])

now = datetime.now()
today = now.strftime("%d/%m/%Y")
date = (now + relativedelta(months=+6)).strftime("%d/%m/%Y")

for row in sheety_data:
    flight = flight_search.get_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=row["IATA Code"],
        from_time=today,
        to_time=date,
    )
    if flight.price:
        if flight.price < int(row["Lowest Price"]):
            notification_manager.send_sms(
                f"\nLow price alert!\nOnly ₺{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                f" to {flight.destination_city}-{flight.destination_airport}\n"
                f"from {flight.out_date} to {flight.return_date}.\n\n"
                f"Link : {flight.link}"
            )

#data_manager.update_flights_data()
