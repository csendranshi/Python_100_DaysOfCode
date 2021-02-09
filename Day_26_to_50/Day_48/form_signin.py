from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL="http://secure-retreat-92358.herokuapp.com/"

driver.get(URL)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("Python")
last_name.send_keys("Gupta")
email.send_keys("blahblah@example.com")

submit = driver.find_elements_by_css_selector("form button")
# email.send_keys(Keys.ENTER)
submit.click()


# driver.quit()