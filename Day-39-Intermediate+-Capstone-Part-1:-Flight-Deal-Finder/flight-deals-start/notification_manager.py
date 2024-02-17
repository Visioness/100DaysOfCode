import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, text):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
                        .create(
                            from_=TWILIO_VIRTUAL_NUMBER,
                            to=TWILIO_VERIFIED_NUMBER,
                            body=text,
                        )

        print(message.sid)