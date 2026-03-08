"""
    Main program for the Flight Deal Finder.
    Uses DataManager, FlightSearch, and NotificationManager.
"""

# ************************ IMPORTS **************************** #
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

from pprint import pprint
import time
from datetime import datetime, timedelta


# ************************ INITIAL SETUP **************************** #
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

# ************************ GET SHEET DATA **************************** #
sheet_data = data_manager.getDestination_data()
pprint(sheet_data)

# ************************ FILL MISSING IATA CODES **************************** #
for row in sheet_data:
    if row["iataCode"] in ("", None):
        code = flight_search.get_iataCode(row["city"])
        time.sleep(2)

        if code:
            row["iataCode"] = code
            data_manager.update_iata_code(row["id"], code)

print("\nUpdated sheet data:")
pprint(sheet_data)

data_manager.destination_data = sheet_data

# ************************ FLIGHT SEARCH **************************** #
origin = "LON"

for r in sheet_data:
    dest = r["iataCode"]

    if dest in ("", None):
        print(f"Skipping {r['city']} — no IATA code.")
        continue

    flight = flight_search.find_cheapest_flight(
        origin,
        dest,
        tomorrow,
        six_months
    )

    # Skip if no flight found
    if flight.price in (None, "N/A"):
        print(f"No flights found for {r['city']}")
        continue

    # Convert price to float safely
    try:
        current_price = float(flight.price)
    except ValueError:
        print(f"Invalid price for {r['city']}: {flight.price}")
        continue

    lowest_price = r["lowestPrice"]

    # Debug
    print(f"{r['city']} : £{current_price}")
    print(f"Comparing {current_price} with {lowest_price}")

    # Build WhatsApp message for EVERY city
    if current_price < lowest_price:
        message = (
            f"🔥 DEAL FOUND!\n"
            f"Only £{current_price} to fly from {origin} to {dest}.\n"
            f"Depart: {flight.out_date}\nReturn: {flight.return_date}\n"
            f"Lowest price on sheet: £{lowest_price}"
        )
    else:
        message = (
            f"📊 Price Update for {r['city']}:\n"
            f"Current price: £{current_price}\n"
            f"Lowest price on sheet: £{lowest_price}\n"
            f"No deal yet, but keeping an eye on it!"
        )

    notification_manager.send_whatsapp(message)