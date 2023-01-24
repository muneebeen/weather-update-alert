import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('WEATHER_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

params = {
    "lat": 52.205338,
    "lon": 0.121817,
    "units": "metric",
    "appid": api_key
}
api_endpoint = f"https://api.openweathermap.org/data/2.5/weather"

response = requests.get(api_endpoint, params=params)
response.raise_for_status()
weather_condition = response.json()['weather'][0]['id']
temperature = response.json()['main']['temp']
if weather_condition < 900:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"It will rain today, carry ☂. Temperature will be {temperature} °C. ",
        from_="Add number",
        to="Add number"
    )

