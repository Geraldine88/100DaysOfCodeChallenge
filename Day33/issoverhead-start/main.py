import requests
from datetime import datetime
import smtplib
import time

my_gmail = 'gingerme26coder@gmail.com'
my_yahoomail = 'ginderme26coder@yahoo.com'
gmail_password = 'vorh fygq ndjq jsvs'

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def iss_overhead():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=5)
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True
        return False
    except Exception as e:
        print(f"  ⚠️ Error checking ISS position: {e}")
        return None

def night():
    try:
        parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=5)
        response.raise_for_status()
        data = response.json()
        sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.now().hour

        if time_now >= sunset_hour or time_now <= sunrise_hour:
            return True
        return False
    except Exception as e:
        print(f"  ⚠️ Error checking nighttime: {e}")
        return None


    #If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Checking conditions...")

    iss_check = iss_overhead()
    night_check = night()

    print(f"  ISS overhead: {iss_check}")
    print(f"  Is nighttime: {night_check}")

    # Only send email if BOTH are explicitly True (not None)
    if iss_check is True and night_check is True:
        print("🚀 ISS is overhead and it's dark! Sending email...")
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=gmail_password)
                connection.sendmail(
                    from_addr=my_gmail,
                    to_addrs=my_yahoomail,
                    msg="Subject: Look Up☝\n\nThe ISS is above you in the sky."
                )
            print("✅ Email sent successfully!")
        except Exception as e:
            print(f"❌ Error sending email: {e}")
    else:
        print("⏳ Conditions not met. Waiting...")

    time.sleep(5)




