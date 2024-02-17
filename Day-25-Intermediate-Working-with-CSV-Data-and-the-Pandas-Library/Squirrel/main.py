import csv
import pandas
import random


# Open and read csv files
"""with open("weather_data.csv") as weather:
    weather = csv.DictReader(weather)
    temperatures = []
    for row in weather:
        temperatures.append(row["temp"])"""


# Using Pandas Lib for reading files
"""weather = pandas.read_csv("weather_data.csv")

print(weather)"""


"""weather = pandas.read_csv("weather_data.csv")"""

# Average of the temperatures
"""temperatures = weather["temp"].to_list()
print(sum(temperatures) / len(temperatures))"""

# Max value in the temperatures
"""print(weather["temp"].max())"""

# Row data for day == Monday
"""print(weather[weather["day"] == "Monday"])"""

# Row data for the max value temperature
"""print(weather[weather["temp"] == weather["temp"].max()])"""

# Converting the temperature of Monday to Fahrenheit
"""print(weather[weather.day == "Monday"].temp[0] * 9/5 + 32)"""

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Column Headers for data
"""print(squirrels.keys())"""

# Data for the random chosen column's random chosen row
"""squirrels_column = random.choice(squirrels.keys())
squirrels_row = random.choice(squirrels[squirrels_column].to_list())

print(squirrels_column, squirrels_row)

print(squirrels[squirrels[squirrels_column] == squirrels_row])"""

# Squirrel counts for each fur colors
new_squirrels = {"Fur Color": [], 
                 "Count": []}

new_squirrels["Fur Color"] = squirrels["Primary Fur Color"].dropna().unique().tolist()

for fur in new_squirrels["Fur Color"]:
    new_squirrels["Count"].append(len(squirrels[squirrels["Primary Fur Color"] == fur]))

new_squirrels = pandas.DataFrame(new_squirrels)
new_squirrels.to_csv("Squirrels.csv")