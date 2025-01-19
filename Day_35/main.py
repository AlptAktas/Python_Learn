import requests

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "412a0837570718deb703b7936b6c5042"


parameters={
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": API_KEY
}


response = requests.get(url=URL, params=parameters)
response.raise_for_status()

print(response.json())