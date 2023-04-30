from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Firefox()
driver.get(URL)

xpath_loc = '//*[@id="articlecount"]/a[1]'


article_count = driver.find_element(By.XPATH, xpath_loc)
# To click
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "View source")
# To click
# all_portals.click()

search_box = driver.find_element(By.NAME, "search")
# To Type in any input box
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)


# driver.quit()
