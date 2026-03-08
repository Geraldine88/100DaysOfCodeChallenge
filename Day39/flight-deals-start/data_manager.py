# ************************ IMPORTATIONS **************************** #
import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth

load_dotenv()


# ************************ CONSTANTS **************************** #
SHEETY_USERNAME = os.getenv("BASICAUTH_SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("BASICAUTH_SHEETY_PASSWORD")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = SHEETY_USERNAME
        self.password = SHEETY_PASSWORD
        self.endpoint = SHEETY_ENDPOINT

        self.auth = HTTPBasicAuth(self.user, self.password)
        self.Destination_data = {}

    # TODO: 2 Now use the Sheety API to GET all the data in that sheet and print it
    def getDestination_data(self):
        response = requests.get(self.endpoint, auth=self.auth)
        data = response.json()
        self.Destination_data = data['prices']
        #return self.Destination_data

        # TODO: 3. Try importing pretty print with the line from pprint import pprint and printing the
        #  data out again using pprint() to see it formatted.
        return self.Destination_data

    # TODO: 6. In the DataManager Class make a PUT request and use the row id from sheet_data to
    #         update the Google Sheet with the IATA codes. (Do this using code).
    """
        HINT: Remember to check the checkbox to allow PUT requests in Sheety.
    """
    # Updating each row in GoogleSheets with a PUT method
    def update_iata_code(self, row_id, iata_code):
       for city in self.Destination_data:
           new_data = {
               "price": {
                   "iataCode": city["iataCode"],
               }
           }
           put_endpoint = f"{self.endpoint}/{city['id']}"
           response = requests.put(put_endpoint, json=new_data, auth=self.auth)
           print(response.text)





