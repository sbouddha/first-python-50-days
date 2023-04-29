from bs4 import BeautifulSoup
import requests
import urllib3
import smtplib
from decouple import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

urllib3.disable_warnings()

my_email = config("MY_EMAIL")
my_password = config("MY_PASSWORD")
to_mail_id = config("MY_EMAIL_1989")
URL = "https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_4?crid=3BPPBOJKU41ON&keywords=instapot&qid=1682783945&sprefix=instapo%2Caps%2C186&sr=8-4&th=1"
BUY_PRICE = 15000
response = requests.get(URL, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')

price_str = soup.find(class_="a-price-whole").getText()
price_int = int(price_str.replace(",", "").rstrip("."))

print(price_int)


def send_email():
    message = MIMEMultipart()
    message["From"] = my_email
    message["To"] = to_mail_id
    message["Subject"] = "Buy The Cooker"
    body = "Price Reduced You should Buy it now"
    message.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))
    text = message.as_string()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_mail_id, msg=text)


if price_int < BUY_PRICE:
    send_email()
else:
    pass
