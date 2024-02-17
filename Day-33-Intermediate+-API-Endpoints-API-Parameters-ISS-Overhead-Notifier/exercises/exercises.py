import requests

MY_LAT = 36.896893
MY_LNG = 30.713324

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(data)
print(f"Sunrise: {sunrise}, Sunset: {sunset}")