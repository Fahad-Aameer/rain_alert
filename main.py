import requests
from twilio.rest import Client

api_key = "899a49d7cca39194b8b08befbd2012ab"
forcast = "http://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC0380a7ad4d16a32c85861a6ce2070f57"
auth_token = "e2dfa8066b83dcaf487846ad357920aa"

parameters = {
    'lat': 12.511580,
    'lon': 79.130127,
    'appid': api_key,
}

response = requests.get(forcast, params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data['list'][:4]

will_rain = False
for i in weather_data:
    weather_id = i["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It might rain today, bring an Umbrella.",
        from_='+19704998758',
        to='0123456789'
    )
    print(message.status)
