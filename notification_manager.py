import os
from twilio.rest import Client
account_sid = os.environ.get("TWILLsid")
auth_token = os.environ.get("TWILLtoken")
tonumber = """number you wand to send"""


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="9856166102",
            to=tonumber,
        )
        print(message.sid)



