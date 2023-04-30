from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

driver = webdriver.Firefox()
driver.get(URL)

xpath_event_name_loc = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a'
xpath_event_date_loc = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time'

event_names_links = driver.find_elements(By.XPATH, xpath_event_name_loc)
event_dates_links = driver.find_elements(By.XPATH, xpath_event_date_loc)

events_list = []
for i in range(len(event_names_links)):
    event_name = event_names_links[i].text
    event_date = event_dates_links[i].text
    # as we are passing 2 values , so need to pass as tuple
    events_list.append((event_name, event_date))

events_dict = {}
for i in range(len(event_names_links)):
    events_dict[i] = {
        "date": event_dates_links[i].text,
        "name": event_names_links[i].text
    }

print(events_list)
print(events_dict)

driver.quit()
