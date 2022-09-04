import requests
from flight_data import FlightData

apikey = "79ev18S27p0Twdl38nASAsiuyjDLZ0hU"
id = "anbarasananbarasan1105"
endpoint = "https://tequila-api.kiwi.com"


class FlightSearch:
    def get_name_code(self, city_name):
        end_point = f"https://tequila-api.kiwi.com/locations/query"
        headers = {"apikey": apikey}
        query = {"term": city_name,
                 "location_types": "city"}
        response = requests.get(url=end_point, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def checkflight(self, originalcity, destination_code, from_time, to_time):
        headers = {"apikey": "79ev18S27p0Twdl38nASAsiuyjDLZ0hU"}
        query = {
            "fly_from": originalcity,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        flight_responce = requests.get(url=f"{endpoint}/v2/search", headers=headers, params=query)
        try:
            data = flight_responce.json()["data"][0]
            flightdata = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        except IndexError:
            print(f"flight data not found ")
            return None
        # flightdata = FlightData(
        #     price=data["price"],
        #     origin_city=data["route"][0]["cityFrom"],
        #     origin_airport=data["route"][0]["flyFrom"],
        #     destination_city=data["route"][0]["cityTo"],
        #     destination_airport=data["route"][0]["flyTo"],
        #     out_date=data["route"][0]["local_departure"].split("T")[0],
        #     return_date=data["route"][1]["local_departure"].split("T")[0]
        # )
        return flightdata




