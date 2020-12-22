import requests

MY_LAT = 19.195630
MY_LNG = 72.832960

API_KEY = "your_key"
parameters = {
    "lat": MY_LAT,
    "lon":MY_LNG,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}
url = f"https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url=url,params=parameters)
data = response.json()
# print(data)

will_rain = False

for i in range(0,12):
    if int(data["hourly"][i]["weather"][0]["id"])<700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")