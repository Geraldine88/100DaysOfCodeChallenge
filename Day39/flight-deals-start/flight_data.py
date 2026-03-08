# class FlightData:
#     def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
#         self.price = price
#         self.origin_airport = origin_airport
#         self.destination_airport = destination_airport
#         self.out_date = out_date
#         self.return_date = return_date
#
#     def findCheapFlights(data):
#
class FlightData:
    def __init__(self, data):
        if data is None:
            self.price = "N/A"
            self.origin_airport = "N/A"
            self.destination_airport = "N/A"
            self.out_date = "N/A"
            self.return_date = "N/A"
            return

        offer = data["data"][0]  # cheapest flight

        self.price = offer["price"]["total"]

        # Outbound
        out_seg = offer["itineraries"][0]["segments"][0]
        self.origin_airport = out_seg["departure"]["iataCode"]
        self.out_date = out_seg["departure"]["at"].split("T")[0]

        # Return
        ret_seg = offer["itineraries"][1]["segments"][0]
        self.destination_airport = ret_seg["arrival"]["iataCode"]
        self.return_date = ret_seg["departure"]["at"].split("T")[0]