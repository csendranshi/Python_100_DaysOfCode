from selenium import webdriver
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)


#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 10
ten_sec = time.time() + 60 * 10  #10seconds

cookie_tag = driver.find_element_by_id("cookie")

while 1:
    cookie_tag.click()
    if time.time() > timeout:

        store_item_prices = driver.find_elements_by_css_selector("#store b")
        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        item_prices = []

        for price in store_item_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 10

    if time.time() > ten_sec:
        cookie_per_sec = driver.find_element_by_id("cps").text
        print(cookie_per_sec)

        break