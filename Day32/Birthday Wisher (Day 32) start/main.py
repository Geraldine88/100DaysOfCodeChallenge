# import smtplib
#
#
# my_gmail = 'gingerme26coder@gmail.com'
# my_yahoomail = 'ginderme26coder@yahoo.com'
# gmail_password = 'vorh fygq ndjq jsvs'
#
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:# smtp for gmail
#     # CREATING A NEW SMTP OBJECT
#
#     #securing our connection to our email server from 3rd party interception(Transport Layer Security or TLS)
#     connection.starttls()
#
#     # Login
#     connection.login(user=my_gmail, password=gmail_password)
#
#     # Send mail
#     #connection.sendmail(from_addr=my_gmail,to_addrs=my_yahoomail, msg = "Hello, Ginger The Coder")
#     # I wanna avoid yahoomail from spamming very simple messages
#     #Note, still didn't work. I had to flag my_gmail as not spam in yahoomail, but I still saw the message
#     connection.sendmail(
#         from_addr=my_gmail,
#         to_addrs=my_yahoomail,
#         msg = f"Subject: Hello\n\nHello,Ginger The Coder from {my_gmail}. \n Hope you\'re having fun with Python.")
#
#closing the connection, but we can avoid it with file opening as you'll see above
#connection.close()
#
                #   Datetime
# import datetime as dt
#
# """
#     dt = module
#     datetime = class
#     now = method to get the current date and time
# """
# now = dt.datetime.now()
# year = now.year
# month = now.month
# weekday = now.weekday()
# day = now.day
# time = now.strftime("%H:%M:%S")
# print(f"Current Date: {now}\n"
#       f"Current Time: {time} \n"
#       f"Current Weekday: {weekday} \n"
#       f"Current Day: {day} \n"
#       f"Current Month: {month} \n"
#       f"Current Year: {year}")
#
#
# # Setting a date of our own like date of birth
# dob = dt.datetime(year = 1963, month = 7, day = 7)
# print(f"\nNino the Wise's birthday: {dob}")


# CHALLENGE
# OBJECTIVE: Send a motivational quote via email on the current weekday

# LIBRARY IMPORTATIONS
import smtplib
import datetime as dt
import random

# TODO : 1 - Use the datetime module to obtain the current day of the week
now = dt.datetime.now()
weekday = now.weekday()

# TODO: 2 - Open the quotes file and obtain the list of quotes
with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()

# TODO: 3 - Use the random module to pick a random quote from the list of quotes
random_quote = random.choice(quote_list)

# TODO: 4 - Use smtplib to send the email to yourself

my_gmail = 'gingerme26coder@gmail.com'
my_yahoomail = 'ginderme26coder@yahoo.com'
gmail_password = 'vorh fygq ndjq jsvs'

days_of_week = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_gmail, password=gmail_password)

    if days_of_week["Tuesday"] == weekday:
        connection.sendmail(
        from_addr=my_gmail,
        to_addrs=my_yahoomail,
        msg=f"Subject: Daily Motivation \n\n Hi, Ginger.\n"
            f"Tuesday Quote: {random_quote}"
    )
