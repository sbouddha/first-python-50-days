from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config
import time


LINKEDIN_USER_ID = config("LINKEDIN_USER_ID")
LINKEDIN_PASSWORD = config("LINKEDIN_PASSWORD")
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3569548795&f_LF=f_AL&geoId=103819153&keywords=data%20engineer&location=Norway&refresh=true"

driver = webdriver.Firefox()
driver.get(URL)

# Click on Sign In Button to Sign in
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Wait for the next page to load.
time.sleep(2)

# Fill the Sign in details
xpath_username = '//*[@id="username"]'
xpath_password = '//*[@id="password"]'

email_box = driver.find_element(By.XPATH, xpath_username)
email_box.send_keys(LINKEDIN_USER_ID, Keys.ENTER)

pass_box = driver.find_element(By.XPATH, xpath_password)
pass_box.send_keys(LINKEDIN_PASSWORD, Keys.ENTER)

sign_in_button.click()

# driver.quit()
