import os
import smtplib

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
        self.my_email = os.getenv("MY_EMAIL")
        self.my_email_password = os.getenv("MY_EMAIL_PASSWORD")
        self.smtp = os.getenv('SMTP_ADDRESS')

    def send_email(self,emails,message):
        with smtplib.SMTP(self.smtp,587) as connection:
            connection.starttls()
            connection.login(self.my_email,self.my_email_password)
            for email in emails:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:New Flight Deal!\n\n{message}".encode("utf-8")
                )

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