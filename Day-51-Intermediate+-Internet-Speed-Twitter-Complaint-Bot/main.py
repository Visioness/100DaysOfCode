from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

SPEED_TEST_URL = 'https://www.speedtest.net/'
TWEET_URL = 'https://twitter.com/home'
TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_VERIFY = os.environ.get('TWITTER_VERIFY')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 80
        self.up = 16


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        self.start_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.start_button.click()
        time.sleep(45)
        self.cur_down = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.cur_up = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f'In Contract: Download -> {self.down}Mbps, Upload -> {self.up}Mbps\n'
              f'Yours: Download -> {self.cur_down}Mbps, Upload -> {self.cur_up}Mbps')

    
    def post_tweet(self):
        self.driver.get(TWEET_URL)
        time.sleep(2)
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')

        email_input.send_keys(TWITTER_EMAIL)
        next_button.click()
        time.sleep(2)

        verify_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        verify_input.send_keys(TWITTER_VERIFY)
        verify_next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        verify_next_button.click()
        time.sleep(1)

        password_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login_button.click()
        time.sleep(3)

        tweet_input = self.driver.find_element(By.XPATH, value='//div[@role="textbox"]')
        tweet_input.send_keys(f'In Contract: Download -> {self.down} Mbps, Upload -> {self.up} Mbps\nMine: Download -> {self.cur_down} Mbps, Upload -> {self.cur_up} Mbps')
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
        post_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.post_tweet()