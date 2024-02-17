import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv("/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env")
MY_EMAIL = os.environ.get("MY_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
TARGET_PRICE = 600


product_url = "https://www.amazon.com.tr/Apple-MMTN2TU-Lightning-Konnekt%C3%B6rl%C3%BC-Kulakl%C4%B1k/dp/B07B9WNSSF?ref_=Oct_d_otopr_d_13710018031_5&pd_rd_w=oC4kn&content-id=amzn1.sym.d7bc3525-ada1-4cd4-a625-1199009392b2&pf_rd_p=d7bc3525-ada1-4cd4-a625-1199009392b2&pf_rd_r=NHCSNT78P9KGAVYYHA0G&pd_rd_wg=8Oqke&pd_rd_r=daf3436c-1d41-4c75-b075-f80f4c84598a&pd_rd_i=B07B9WNSSF"

product_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Accept-Language": "en,en-GB;q=0.9,en-US;q=0.8",
    "X-Forwarded-For": "95.12.112.112",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

product_response = requests.get(url=product_url, headers=product_headers)
#print(product_response.text)

soup = BeautifulSoup(product_response.text, "lxml")

product_brand = soup.select_one("tr.a-spacing-small.po-brand td.a-span9 span.a-size-base.po-break-word").getText()
product_model = soup.select_one("tr.a-spacing-small.po-model_name td.a-span9 span.a-size-base.po-break-word").getText()

product_price_whole = int(soup.find(class_="a-price-whole", name="span").getText().rstrip(',').replace('.', ''))
product_price_fraction = int(soup.find(class_="a-price-fraction", name="span").getText())
price_symbol = soup.find(class_="a-price-symbol", name="span").getText()

price = float(f"{product_price_whole}.{product_price_fraction}")
print(f"{product_brand} - {product_model}: {price:.2f} {price_symbol}")


# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
if price < TARGET_PRICE:
    subject = f"{product_brand} - {product_model} Price Alert!"
    body = f"Better price on {product_brand} - {product_model} product!\n"\
        f"Target Price: ₺{TARGET_PRICE}\nCurrent Price: ₺{price}\n"\
        f"Here is the link not to miss that opportunity!\n\n{product_url}"
    message = MIMEText(body, 'plain', 'utf-8')
    message['Subject'] = subject

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message.as_string())