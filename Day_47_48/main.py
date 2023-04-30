from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.in/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_4?crid=26JQZJS0VB7ZQ&keywords=instant%2Bpot&qid=1682845033&s=kitchen&sprefix=instant%2Bpo%2Ckitchen%2C123&sr=1-4&th=1"

driver = webdriver.Firefox()
driver.get(URL)

price_element = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")
price_text = price_element.text
price = int(price_text.replace(",", "").rstrip("."))

print(price)

# driver.close()
# driver.quit()
