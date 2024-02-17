from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time


load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')

class Sheet:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(os.environ.get('GOOGLE_RENT_SEARCH_FORM'))

    def send_form(self, address, link, price):
        self.driver.get(os.environ.get('GOOGLE_RENT_SEARCH_FORM'))
        
        address_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        link_input = self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        send_button = self.driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        
        address_input.send_keys(address)
        link_input.send_keys(link)
        price_input.send_keys(price)
        send_button.click()
        time.sleep(0.5)