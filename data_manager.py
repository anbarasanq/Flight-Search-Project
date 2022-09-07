import requests
end_point = "https://api.sheety.co/b32b14177f5feb387046fab3afb6ebb1/copyOfFlightDeals/prices"


class DataManager:
    def __init__(self):
        self.data = {}

    def get_data(self):
        responce = requests.get(f"{end_point}")
        data1 = responce.json()
        print(data1)
        self.data1 = data1["prices"]
        return self.data1

    def update_data(self):
        for city in self.data:
            fresult = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheet = requests.put(url=f"{end_point}/"
                                     f"{city['id']}",
                                     json=fresult)
