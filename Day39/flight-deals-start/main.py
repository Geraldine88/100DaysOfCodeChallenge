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

# ************************ GET CUSTOMER EMAILS **************************** #
customer_data = data_manager.get_customer_emails()

# Detect correct email key
email_key = "email"
if len(customer_data) > 0:
    # auto-detect if it's emailAddress instead
    if "emailAddress" in customer_data[0]:
        email_key = "emailAddress"

emails = [row[email_key] for row in customer_data]

print("\nCustomer emails:")
print(emails)

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

    # Try direct flights first
    flight = flight_search.check_flights(
        origin,
        dest,
        tomorrow,
        six_months,
        is_direct=True
    )

    # If no direct flights → try indirect
    if flight is None:
        print(f"No direct flights for {r['city']}. Searching indirect flights...")
        flight = flight_search.check_flights(
            origin,
            dest,
            tomorrow,
            six_months,
            is_direct=False
        )

    # If still None → skip
    if flight is None:
        print(f"No flights found at all for {r['city']}")
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

    # Determine stop text
    if flight.stops == 0:
        stop_text = "Direct flight"
    else:
        stop_text = f"{flight.stops} stop(s)"

    # WhatsApp message
    if current_price < lowest_price:
        message = (
            f"🔥 DEAL FOUND!\n"
            f"GBP {current_price} from {origin} to {dest}.\n"
            f"{stop_text}\n"
            f"Depart: {flight.out_date}\nReturn: {flight.return_date}\n"
            f"Lowest price on sheet: GBP {lowest_price}"
        )
    else:
        message = (
            f"📊 Price Update for {r['city']}:\n"
            f"Current price: GBP {current_price}\n"
            f"{stop_text}\n"
            f"Lowest price on sheet: GBP {lowest_price}\n"
            f"No deal yet, but monitoring!"
        )

    # Send WhatsApp
    notification_manager.send_whatsapp(message)

    # Email message
    email_message = (
        f"Low price alert!\n\n"
        f"Destination: {r['city']}\n"
        f"Price: GBP {current_price}\n"
        f"Route: {stop_text}\n"
        f"From: {flight.origin_airport}\n"
        f"To: {flight.destination_airport}\n"
        f"Depart: {flight.out_date}\n"
        f"Return: {flight.return_date}\n"
    )

    # Send email to all customers
    notification_manager.send_email(emails, email_message)