import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "[your_emailid]"
MY_PASSWORD = "[your_password]"


MY_LAT = 19.195630
MY_LNG = 72.832960

def is_iss_overhead():
    url1 = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=url1)
    data = response.json()

    lng = float(data["iss_position"]["longitude"])
    lat = float(data["iss_position"]["latitude"])

    iss_position = (lng, lat)
    print(iss_position)
    # Your position within +5 -5 of the iss position
    if (abs(lat - MY_LAT) <= 5) and (abs(lng - MY_LNG) <= 5):
        print("hi")
    else:
        print("bye")


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    if hour_now >= sunset_hour or hour_now <= sunrise_hour:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="[receiver's email_id]",
            msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky!"
        )
