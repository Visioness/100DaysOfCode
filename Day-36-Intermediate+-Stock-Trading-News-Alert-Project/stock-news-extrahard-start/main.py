import requests
import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from twilio.rest import Client

load_dotenv("/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHAVANTAGE_API_KEY,
}
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_data = stock_response.json()
stock_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]

yesterday_close = float(stock_list[0]["4. close"])
thedaybefore_close = float(stock_list[1]["4. close"])
change = (yesterday_close - thedaybefore_close) * (100 / thedaybefore_close)

if abs(change) >= 0:
    updown = "🔻" if change < 0 else "🔺"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()
news_list = news_data["articles"][:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
email_message = ""
for news in news_list:
    email_message += f"Headline: {news['title']}\nBrief: {news['description']}\n\nSource: {news['source']['name']} -- {news['url']}\n\n\n\n"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
            body=f"\n{STOCK}: {updown}{abs(change):.3f}%\n\n\n{email_message}",
            )

print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
