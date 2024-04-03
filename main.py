import requests
from secrets import ACCOUNT_SID, AUTH_TOKEN, OWM_ENDPOINT, WEATHER_PARAMS
from twilio.rest import Client

response = requests.get(OWM_ENDPOINT, params=WEATHER_PARAMS)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Its going to rain today, bring an umbrella!",
        from_="TWILIO PHONE NUMBER HERE",
        to="MY PHONE NUMBER HERE"
    )

print(weather_data["list"][0]["weather"][0]["id"])
print(response.status_code)
print(response.json())
