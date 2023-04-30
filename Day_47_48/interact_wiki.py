from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Firefox()
driver.get(URL)

xpath_loc = '//*[@id="articlecount"]/a[1]'
article_count = driver.find_element(By.XPATH, xpath_loc)
print(article_count.text)

driver.quit()
