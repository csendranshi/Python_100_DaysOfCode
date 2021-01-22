import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DOWN_THRESHOLD = 150
UP_THRESHOLD = 10
CHROME_DRIVER_PATH = "D:\chromedriver.exe"
TWITTER_EMAIL = os.environ["twitter_email"]
TWITTER_PASS = os.environ["twitter_password"]
URL ="https://www.speedtest.net/"

class internetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=driver_path)
    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(120)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.up, self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASS)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        # f"Day 51 #100DaysOfCode made a tweet bot using #selenium and #Pyhthon which tweeted this too!\n\n" \
        tweet = f"Day 52 ##100DaysOfCode Made #Instagram follower Bot using #Selenium and #Python\n" \
                f"It clearly increases reach for my photography acc!\n\n" \
                f"#WomenWhoCcode #DEVCommunity #DEVcommunityIN #100daysofpython #CodeNewbie #Developer #Photography #GirlsWhoCode #womenintech #automation "
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

bot = internetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()

