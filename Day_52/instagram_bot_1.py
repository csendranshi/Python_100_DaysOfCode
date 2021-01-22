import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "D:\chromedriver.exe"
SIMILAR_ACC = "blackandwhite_art"
USERNAME = os.environ['username']
PASS = os.environ['password']
URL = "https://www.instagram.com/accounts/login/"

class InstaFollower:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get(URL)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        time.sleep(2)
        password.send_keys(PASS)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        try:
            send_security_code_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/span/button')
            send_security_code_button.click()
            time.sleep(60)
            submit_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/div/button')
            submit_button.click()
        except:
            pass




    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        # / html / body / div[5] / div / div / div[2]
        for i in range(5):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            print("scrolled")
            time.sleep(1)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        c=0
        for button in all_buttons:
            try:
                if c%9==0:
                    time.sleep(10)

                time.sleep(3)
                button.click()
                c+=1

            except:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                # / html / body / div[6] / div / div / div / div[3] / button[2]
                cancel_button.click()



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()