from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.power.no/hjem/rengjoering-og-stoevsuging/robotstoevsuger/xiaomi-mi-robot-vacuum-mop-2-pro-robotstoevsuger-hvit/p-1248012/"

driver = webdriver.Firefox()
driver.get(URL)

xpath_loc = "/html/body/pwr-main/div/div/pwr-product-page/div[1]/section[1]/div/div/div[4]/div[2]/div[3]/div/div[1]/div/pwr-product-price/div/div[1]/pwr-price-label/div/pwr-price"

# price_element = driver.find_element(By.XPATH, "//pwr-price[@type='integer']")
price_element = driver.find_element(By.XPATH, xpath_loc)
price = price_element.text.strip()

print(price)

driver.quit()
