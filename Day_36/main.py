import requests
from datetime import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_KEY = "your_key"
NEWS_KEY = "your_key"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()

# print(news_data)

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)
dates = stock_data["Time Series (Daily)"]
print(dates)

if dates[str(yesterday)]:
    yesterday_close = float(dates[str(yesterday)]["4. close"])

if dates[str(day_before_yesterday)]:
    day_before_yesterday_close = float(dates[str(day_before_yesterday)]["4. close"])

difference = (yesterday_close - day_before_yesterday_close)
print(difference)
up_down = None
if difference > 0:
    up_down ="🔺"
else:
    up_down = "🔻"

percent_diff = round((difference / yesterday_close) * 100)

if abs(percent_diff) > 5:
    news_params = {
        "apiKey": NEWS_KEY,
        "q": COMPANY_NAME
    }
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = response_news.json()

    # print("Get News ")
    top_news = [f"{STOCK_NAME} {up_down}{percent_diff}\nHeadline: {i['title']}. \nBrief: {i['description']}" for i in news_data["articles"][:3]]
    print(top_news)


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
