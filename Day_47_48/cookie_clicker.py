from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Firefox()
driver.get(URL)

xpath_button = '//*[@id="cookie"]'

cookie_button = driver.find_element(By.XPATH, xpath_button)

for i in range(100):
    cookie_button.click()

# driver.quit()
