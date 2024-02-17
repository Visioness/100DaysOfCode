import requests
from datetime import datetime
import smtplib
import time
import os



MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = os.environ.get('MY_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

#Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    global iss_latitude, iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return True if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 else False


def is_night():
    global sunrise, sunset
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    return True if time_now >= sunset or time_now <= sunrise else False


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS IS CLOSE!\n\n"
                                                                        "Look up! ISS is close to you, maybe you can see it in the sky!\n"
                                                                        f"Current location of ISS: {iss_latitude}, {iss_longitude}\n"
                                                                        f"Your location: {MY_LAT}, {MY_LONG}\n\n"
                                                                        "-Aygun")

    time.sleep(60)