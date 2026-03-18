import requests
#from datetime import datetime
import os
from dotenv import load_dotenv
from flight_data import FlightData

# Load environment variables from .env file
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

AMADEUS_FLIGHT_OFFERS = "https://test.api.amadeus.com/v2/shopping/flight-offers"


# # ************************ CONSTANTS **************************** #
# AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
# AMADEUS_SECRET_KEY = os.getenv("AMADEUS_SECRET_KEY")
#amadeus_base_url = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET_KEY"]
        self._token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        #set your token by calling a separate method where we'll request the token.
        self.token = self._get_new_token()

    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=self._token_endpoint, headers=header, data=data)
        result = response.json()
        return result["access_token"]

    def get_iataCode(self, cityName):
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "keyword": cityName,
            "subType": "CITY,AIRPORT"
        }

        SPECIAL_CASES = {
            "Tokyo": "TYO",
            "Hong Kong": "HKG",
            "Kuala Lumpur": "KUL",
            "Dublin": "DUB",
            "Seychelles": "SEZ"
        }

        if cityName in SPECIAL_CASES:
            return SPECIAL_CASES[cityName]

        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=params)
        data = response.json()

        #print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        # If APT Call fails

        # if response.status_code != 200:
        #     print(f"Error fetching IATA for city {cityName}: {response.text}")
        #     return None
        # data = response.json()

        # No results
        if "data" not in data or len(data["data"]) == 0:
            print(f"No IATA code found for city {cityName}")
            return None

        return data["data"][0]["iataCode"]

    def searchFlights(self, origin, destination, departDate, returnDate):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departDate,
            "returnDate": returnDate,
            "adults" : 1,
            "nonStop" : "true",
            "currencyCode" : "GBP",
            "max": 10
        }

        response = requests.get(url=AMADEUS_FLIGHT_OFFERS, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error fetching flights for {destination}: {response.text}")
            return None

        data = response.json()

        if "data" not in data or len(data["data"]) == 0:
            print(f"No flights found for {destination}")
            return None

        return data

    # def find_cheapest_flight(self, origin, destination, departDate, returnDate):
        data = self.searchFlights(origin, destination, departDate, returnDate)
        return FlightData(data)

    def check_flights(self,  origin, destination, depart, return_date, is_direct=True):
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": depart,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "max": 5
        }

        response = requests.get(FLIGHT_ENDPOINT, headers=headers, params=params)
        data = response.json().get("data", [])

        if not data:
            return None

        flight = data[0]

        # Count stops
        itinerary = flight["itineraries"][0]
        segments = itinerary["segments"]
        stops = len(segments) - 1

        return FlightData(
            price=float(flight["price"]["total"]),
            origin_airport=segments[0]["departure"]["iataCode"],
            destination_airport=segments[-1]["arrival"]["iataCode"],
            out_date=segments[0]["departure"]["at"].split("T")[0],
            return_date=flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
            stops=stops
        )

