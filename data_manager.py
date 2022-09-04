import requests


class DataManager:
    def __init__(self):
        self.data = {}

    def get_data(self):
        responce = requests.get("https://api.sheety.co/69a863e8fc3e592aa9642d13453a5e48/copyOfFlightDeals/prices")
        data = responce.json()
        self.data = data["prices"]
        return self.data

    def update_data(self):
        for city in self.data:
            fresult = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheet = requests.put(url=f"https://api.sheety.co/69a863e8fc3e592aa9642d13453a5e48/copyOfFlightDeals/"
                                         f"prices/{city['id']}",
                                     json=fresult)
