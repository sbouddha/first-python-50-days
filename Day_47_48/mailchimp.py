from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://login.mailchimp.com/signup/"

driver = webdriver.Firefox()
driver.get(URL)

xpath_button = '//*[@id="create-account-enabled"]'

email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("neo_chimpmail@gmail.com", Keys.ENTER)

username_box = driver.find_element(By.NAME, "username")
username_box.send_keys("", Keys.ENTER)

pass_box = driver.find_element(By.NAME, "password")
pass_box.send_keys("ComplexPassword@123", Keys.ENTER)

# wait for the sign-up button to be clickable
button_click = driver.find_element(By.CSS_SELECTOR, "form button")

# click the sign-up button
button_click.click()

# driver.quit()
