import requests
from datetime import datetime

MY_LATITUDE = 47.606209
MY_LONGITUDE = -122.332069

# # Getting request of enpoint(url
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# #print(response)
#
# """
#     RESPONSE CODES
#     1XX: HOLD ON
#     2XX: HERE YOU GO
#     3XX: GO AWAY, NO PERMISSION
#     4XX: YOU SCREWED UP, LIKE 404
#     5XX: I(SERVER) SCREWED UP
# """
#
# #print(response.status_code)
# response.raise_for_status()
# data = response.json()
#
# #iss_position longitute and latitude
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)
#
# print(data)

"""
    API PARAMETERS
    This is a way that allows you give your input whem making api request for different outcome
"""
parameters = {
    "lat" :MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "formatted": 0,

}


response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters
)
response.raise_for_status()

data = response.json()
#print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f'Sunrise: {sunrise}')
print(f'Sunset: {sunrise}')



time_now = datetime.now()
print(time_now.hour)



