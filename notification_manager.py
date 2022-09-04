
from twilio.rest import Client
account_sid = "AC5f261929cf469dc6400c1877baddad2f"
auth_token = "cf9c7baead6c9ab0dc1389411a5a19bc"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        print("get")
        message = self.client.messages.create(
            body=message,
            from_="9856166102",
            to="+916382674252",
        )
        print(message.sid)



