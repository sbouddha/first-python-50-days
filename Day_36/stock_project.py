import requests
from datetime import datetime, timedelta
import smtplib
from decouple import config

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

stock_api_key = config("STOCK_API_KEY")
news_api_key = config("NEWS_API_KEY")

my_email = config("MY_EMAIL")
my_password = config("MY_PASSWORD")
to_mail_id = config("MY_EMAIL_1989")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_num = 0

pamameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key
}

today = datetime.today()
yesterday = (today-timedelta(days=1)).strftime('%Y-%m-%d')

pamameters_news = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "publishedAt",
    "language": "en",
    "apikey": news_api_key
}

response_stock = requests.get(
    url=STOCK_ENDPOINT, params=pamameters_stock, verify=False)
data_stock = response_stock.json()


# To get last day Closing Price
previous_day_closure_dict = data_stock["Time Series (Daily)"]

previous_day_list = list(previous_day_closure_dict.items())[0]
prev_day_close_value = float(previous_day_list[1]['4. close'])
print(f"Yesterday Closing Price was : {prev_day_close_value}")

# To get Day before yesterday Closing Price
day_before_closure_dict = data_stock["Time Series (Daily)"]

day_before_list = list(day_before_closure_dict.items())[1]
day_before_close_value = float(day_before_list[1]['4. close'])
print(f"Day before Closing Price was : {day_before_close_value}")

# Difference Percentage
perc_change = round(((prev_day_close_value - day_before_close_value) /
                     prev_day_close_value)*100, 2)
print(f"Percent change in price is : {perc_change}")

# fetch first 3 news
response_news = requests.get(
    url=NEWS_ENDPOINT, params=pamameters_news, verify=False)
data_news = response_news.json()

# print(response_news.request.url)

if perc_change > 0:
    sign = " 🔺 "
else:
    sign = " 🔻 "


def fetch_news():
    global news_num
    while news_num < 1:
        headline_news = data_news["articles"][news_num]["title"]
        brief_news = data_news["articles"][news_num]["description"]
        news_num += 1
        top_news = (
            f"{STOCK}: {sign}{perc_change}%\nHeadline: {headline_news}\nBrief: {brief_news}\n")
        return top_news


def send_email():
    message = MIMEMultipart()
    message["From"] = my_email
    message["To"] = to_mail_id
    message["Subject"] = "Stock Update"
    body = fetch_news()
    message.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))
    text = message.as_string()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_mail_id, msg=text)


if perc_change > 2 or perc_change < -2:
    send_email()
else:
    print("Fluctuation is less than 5 Percent")
