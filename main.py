
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
notification_manager = NotificationManager()
datamanager = DataManager()
flightsearch = FlightSearch()
sheet_data = datamanager.get_data()
originalplace = "LON"
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
    try:
        if newflight.money < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £20 to fly from {newflight.cityfrom}-"
                        f"{newflight.flyfrom} to {newflight.cityto}-{newflight.flyto},"
                        f" from {newflight.out_date} to {newflight.return_date}."
            )
    except AttributeError:
        pass
    




