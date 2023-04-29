from bs4 import BeautifulSoup
import requests

URL = "https://www.power.no/hjem/rengjoering-og-stoevsuging/robotstoevsuger/xiaomi-mi-robot-vacuum-mop-2-pro-robotstoevsuger-hvit/p-1248012/"

response = requests.get(URL, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')

price_element = soup.find(class_="_ngcontent-ebd-c161")
print(price_element)
