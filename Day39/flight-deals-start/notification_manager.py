from twilio.rest import Client
import os


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(
            os.environ['TWILIO_SID'],
            os.environ['TWILIO_AUTH_TOKEN']
        )
        self.from_number = os.environ['TWILIO_VIRTUAL_NUMBER']
        self.to_number = os.environ['TWILIO_VERIFIED_NUMBER']

    def send_message(self, message):
        smsMsg = self.client.messages.create(
            body= message,
            from_= self.from_number,
            to = self.to_number
        )
        print(f"SMS sent: {smsMsg.sid}")

    def send_whatsapp(self, message):
        whatsappMsg = self.client.messages.create(
            body= message,
            from_= self.from_number,
            to = self.to_number
        )
        print(f"Whatsapp sent: {whatsappMsg.sid}")