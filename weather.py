# Getting weather from API form https://open-meteo.com/  we want to see as a chart
# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m

import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min"
    # today = datetime.now()
    # week_ago = today - timedelta(days=7)
    # start_date = week_ago.strftime("%Y-%m-%d")  # picks only y and m and d
    # end_date = today.strftime("%Y-%m-%d")  # picks only y and m and d
    response = requests.get(url)  # it'll give you 200 back
    data = response.json()  # it will give you the json format
    return data["daily"]


lat = input("Enter the latitude : ")
lon = input("Enter the longitude : ")

daily_data = get_weather(lat, lon)

df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)
df["data"] = pd.to_datetime(df["date"])
print(df)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker="o", label="Max_temp")
plt.plot(df["date"], df["min_temp"], marker="o", label="Min_temp")

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.title("Weather - Past 7 Days ")
plt.legend()

# Rotating X for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("weather_chart.png")
plt.show()

if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/weather.csv", index=False)
print("Data saved to data/weather.csv")
