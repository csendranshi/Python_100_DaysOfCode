from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

username = os.environ['linkedin_username']
password = os.environ['linkedin_password']
PHONE = "1234567893"

URL = "https://www.linkedin.com/jobs/search/?currentJobId=2298533133&f_E=1&f_JT=I&geoId=102713980&keywords=data%20analyst&location=India"
chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(username)
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()