import requests
#from datetime import datetime
from twilio.rest import Client

API_KEY = ""

# --------------------------------- TWILIO DETAILS -------------------------------------------
account_sid = ""
auth_token = ""

# --------------------------------------------------------------------------------------------

# Open weather maps endpoint
OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"

# Weather parameters: For Seattle, WA
WEATHER_PARAMS = {
    "lat": 47.603230,
    "lon": -122.330276,
    "appid": API_KEY,
    "cnt": 4, # cnt is the number of timestamps, which will returned 4 time intervals.
}

response = requests.get(
    url=OWM_ENDPOINT,
    params=WEATHER_PARAMS
)

response.raise_for_status()

weather_data = response.json()

# Get the actual weather condition
# If ID code any timestamp is < 700, advice user to bring an umbrella in the next 12 hours

#Print out weather id from weather data
weather_data_list = weather_data["list"]
#print(weather_data_list[0]['weather'][0]['id'])
"""
    weather_data_list[0] → first dictionary

    ['weather'] → list of weather objects
    
    [0] → first weather dictionary
    
    ['id'] → the actual value
"""



"""
# Condition codes
code_id_1 = weather_data_list[0]["weather"][0]["id"]
code_id_2 = weather_data_list[1]["weather"][0]["id"]
code_id_3 = weather_data_list[2]["weather"][0]["id"]
code_id_4 = weather_data_list[3]["weather"][0]["id"]

list_condition_codes  = [
    data["weather"][0]["id"]
    for data in weather_data_list
]
what_to_do = ["bring umbrella" if _ < 700 else "no umbrella"
              for _ in list_condition_codes]
print(what_to_do)
"""





# OR better still

is_rain = False
for hour_data in weather_data_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        is_rain = True
if is_rain:
    # CREATING A TWILIO CLIENT TO SEND MESSAGE
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Rain alerter. Remember to take an umbrella!☔",
        from_= "+18774613445",
        to=""
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Rain alerter. No need for an umbrella",
        from_= "+18774613445",
        to="+"
    )

    print(message.status)



