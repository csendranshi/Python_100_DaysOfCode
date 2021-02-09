import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=url)
data = response.json()

lng = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

iss_position = (lng,lat)

print(iss_position)