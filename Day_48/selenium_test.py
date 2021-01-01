from selenium import webdriver

chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.in/Muji-Point-Black-0-38mm-Japan/dp/B01N8QNC59/ref=sr_1_1?dchild=1&keywords=muji&qid=1609431990&sr=8-1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://python.org")
event_time = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events={}
for n in range(len(event_time)):
    events[n] = {
        "time":event_time[n].text,
        "name":event_names[n].text
    }

print(events)

driver.quit()