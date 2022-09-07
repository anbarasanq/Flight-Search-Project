
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
notification_manager = NotificationManager()
datamanager = DataManager()
flightsearch = FlightSearch()
sheet_data = datamanager.get_data()
originalplace = "LHR"
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
         row["iataCode"] = flightsearch.get_name_code(row["city"])
         datamanager.data = sheet_data
         datamanager.update_data()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
for destination in sheet_data:
    newflight = flightsearch.checkflight(originalcity=originalplace,
                             destination_code=destination["iataCode"],
                             from_time=tomorrow,
                             to_time=six_month_from_today)
    if newflight is None:
        continue

    if newflight.money < destination["lowestPrice"]:
        message=f"Low price alert! Only £{newflight.money} to fly from {newflight.cityfrom}-{newflight.flyfrom} to" \
                f" {newflight.cityto}-{newflight.flyto},from {newflight.out_date} to {newflight.return_date}."
        if newflight.stop_overs > 0:
            message += f"\nFlight has {newflight.stop_overs} stop over, via {newflight.via_city}."
            print(message)
            notification_manager.send_sms(message)




