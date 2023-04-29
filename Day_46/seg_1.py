from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings()
URL = "https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_4?crid=3BPPBOJKU41ON&keywords=instapot&qid=1682783945&sprefix=instapo%2Caps%2C186&sr=8-4&th=1"

response = requests.get(URL, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')

price_str = soup.find(class_="a-price-whole").getText()
price_int = int(price_str.replace(",", "").rstrip("."))

print(price_int)


if price_int < 15000:
    print("Price Reduced You should Buy it now")
else:
    print("Price Too High")
