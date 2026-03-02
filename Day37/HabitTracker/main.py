import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# USERNAME = "geraldine2026"
# TOKEN = "TokenG26*2026"

load_dotenv()
USERNAME = os.getenv("PIXEL_USERNAME")
TOKEN = os.getenv("PIXEL_TOKEN")

GRAPH_ID = "graph1"
TODAY_TIME = datetime.now().strftime("%Y%m%d")
YESTERDAY_TIME = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")

"""
    [required] The date on which the quantity is to be recorded. 
    It is specified in yyyyMMdd format.
"""

# Pixela Endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# Graph Endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Post a pixel Endpoint
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Update a pixel Endpoint
update_yesterday_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY_TIME}"

# Delete a pixel Endpoint
delete_yesterday_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY_TIME}"



user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# CREATE A NEW GRAPH ON PIXELA FOR OUR USER NAME
graph_configs = {
    "id": GRAPH_ID,
    "name": "CodingGraph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#response = requests.post(url=graph_endpoint, json=graph_configs, headers=headers)
#print(response.text)



# POST A PIXEL
pixel_params = {
    "date": TODAY_TIME,
    "quantity": input("How many code commits did you do today? : "),
    "optionalData": "{\"reason\":\"Count code dedication\"}"
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# Updating yesterday's pixel
"""
    So, I lied that I made 19 commits yesterday. 
    I'm sincerely sorry. I love purple and wanted to see its intensity.
    Now, I wanna 
    use the PUT method to edit yesterday's pixel
"""

# Updating yesterday's pixel
update_params = {
    "quantity": "2",
    "optionalData": "{\"reason\":\"Count code dedication\"}"
}

# response = requests.put(
#     url=update_yesterday_endpoint,
#     headers=headers,
#     json=update_params
# )
#
# print(response.text)

# Delete a pixel
# response = requests.delete(
#     url=delete_yesterday_endpoint,
#     headers=headers
# )
#
# print(response.text)


# response = requests.delete(
#     url=delete_yesterday_endpoint,
#     headers=headers
# )
#
# print(response.text)



