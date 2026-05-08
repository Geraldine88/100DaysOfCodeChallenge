STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# "https://newsapi.org/docs/endpoints/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
STOCK_API_KEY = "YKCXWJADR7UUA78B"
NEWS_API_KEY = "0e0f3e00c8c54859a260bcf342188a09"

######################  IMPORTATIONS ##########################
import requests


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then
# print("Get News").
# TODO: FETCH YESTERDAY'S CLOSING STOCK PRICE
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']

# Each item in the data list is composed of only the dictionary values for each day showing open/close etc
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_close_price = yesterday['4. close']
print(yesterday_close_price)
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference
# between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
day_bfor_yesterday = data_list[1]
day_bfor_yesterday_close_price = day_bfor_yesterday['4. close']
print(day_bfor_yesterday_close_price)

diff = abs(float(yesterday_close_price) - float(day_bfor_yesterday_close_price))
print(diff)

#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
diff_pct = (diff / float(yesterday_close_price)) * 100
print(diff_pct)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if diff_pct > 0:
    new_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()['articles']
    print(news_response.json())



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(diff_pct) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK}: {up_down}{diff_pct}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)


