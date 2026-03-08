"""
    This file will need to use the DataManager,FlightSearch, FlightData,
    NotificationManager classes to achieve the program requirements.
"""
# ************************ IMPORTATIONS **************************** #
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

from pprint import pprint
import time
from datetime import datetime, timedelta


# ************************ CALLING FUNCTIONS **************************** #
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=180)

depart_time = tomorrow.strftime("%Y-%m-%d")
return_date = six_month.strftime("%Y-%m-%d")

# TODO: 4. Pass everything stored in the "prices" key back to the main.py file and store it
#  in a variable called 'sheet_data', so that you can print the sheet_data from main.py
sheet_data = data_manager.getDestination_data()

pprint(sheet_data)

# TODO: 5. In main.py check if sheet_data contains any values for the "iataCode" key.
"""
    If not, then the IATA Codes column is empty in the Google Sheet. 
    In this case, pass each city name in sheet_data one-by-one to the FlightSearch class. 
    For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code. 
    You should use the response from the FlightSearch class to update the sheet_data dictionary.
"""
# TODO : loop through rows and fill missing IATA codes
for r in sheet_data:
    if r["iataCode"] in ("", None):
        iata = flight_search.get_iataCode(r["city"])
        time.sleep(2)

        if iata:
            r["iataCode"] = iata
            data_manager.update_iata_code(r["id"], iata)
        # city = r['city']
        # iata = flight_search.get_iataCode(city)
        # row_id = r["id"]
        #
        # data_manager.update_iata_code(row_id, iata)

print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
#data_manager.update_iata_code()

origin = "LON"
for r in sheet_data:
    destination = r["iataCode"]

    flight = flight_search.find_cheapest_flight(
        origin,
        destination,
        depart_time,
        return_date,
    )

    print(f"{r['city']} : £{flight.price}")

    # Skip if no flight is found
    if flight.price == "N/A":
        continue

    # Now, compare the prices
    if float(flight.price) < r["lowestPrice"]:
        print(f"Lower Price flight found to {r['city']}")

        message = (
            f"Low price alert! Only £{flight.price} to fly "
            f"from {flight.origin_airport} to {flight.destination_airport}, "
            f"departing {flight.out_date} and returning {flight.return_date}."
        )

        notification_manager.send_whatsapp(message)
