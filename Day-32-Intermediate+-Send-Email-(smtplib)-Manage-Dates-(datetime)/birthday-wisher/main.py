##################### Extra Hard Starting Project ######################
import pandas
import smtplib
from datetime import datetime
import random

current = datetime.now()
birthday_list = []
my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"


# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
for person in birthdays:
    if person["month"] == current.month and person["day"] == current.day:
        birthday_list.append(person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in birthday_list:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        message = letter.read().replace("[NAME]", person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject:Happy Birthday!\n\n{message}")
