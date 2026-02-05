##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd
import os

# Your email credentials (use environment variables or app password for security)
my_gmail = 'gingerme26coder@gmail.com'
my_yahoomail = 'ginderme26coder@yahoo.com'
gmail_password = 'vorh fygq ndjq jsvs'

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.
birthday_data = pd.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
todayMonth = now.month
TodayDay = now.day

# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

birthday_dict = {
    (row['month'], row['day']): row
    for i, row in birthday_data.iterrows()
}

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if (todayMonth, TodayDay) in birthday_dict:
    celebrant = birthday_dict[(todayMonth, TodayDay)]

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    template_files = [f for f in os.listdir('letter_templates') if f.endswith('.txt')]
    random_temp = random.choice(template_files)
    with open(f'letter_templates/{random_temp}') as letter_file:
        letter_content = letter_file.read()

    letter_content = letter_content.replace('[NAME]', celebrant['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)

        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=celebrant['email'],
            msg=f"Subject: Happy Birthday!\n\n{letter_content}"
        )

