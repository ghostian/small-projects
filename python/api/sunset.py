"""
Created by cyborgoat at 2022/1/19
Email: cyborgoat@outlook.com

Description
-----------

"""
from datetime import datetime

import requests

london_lat = 51.507351
london_long = -0.127758

parameters = {
    "lat": london_lat,
    "lng": london_long,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data["results"]["sunrise"])
print(data["results"]["sunset"])

time_now = datetime.now()
print(time_now)
