#Go to openweathermap.org
#Make an account, tap on account, go to "My API Keys"
#Copy API Key and Paste below
import requests

API_KEY = "959f5a22f9f146fb5e02b7ec9d12d654"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")