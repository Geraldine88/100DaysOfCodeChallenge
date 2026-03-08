import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(
            os.environ["TWILIO_SID"],
            os.environ["TWILIO_AUTH_TOKEN"]
        )
        self.from_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.to_number = os.environ["TWILIO_VERIFIED_NUMBER"]

    def send_sms(self, message):
        sms = self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=self.to_number
        )
        print(f"SMS sent: {sms.sid}")

    def send_whatsapp(self, message):
        whatsapp = self.client.messages.create(
            body=message,
            from_=f"whatsapp:{self.from_number}",
            to=f"whatsapp:{self.to_number}"
        )
        print(f"WhatsApp sent: {whatsapp.sid}")