from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import os
from dotenv import load_dotenv
import time
import random

load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')

ACCOUNT = 'barisozcan'
INSTAGRAM_EMAIL = os.environ.get('INSTAGRAM_EMAIL')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get('https://www.instagram.com/')

email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
password_input = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
login_button = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')

email_input.send_keys(INSTAGRAM_EMAIL)
password_input.send_keys(INSTAGRAM_PASSWORD)
login_button.click()
time.sleep(3)

info = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')))
info.click()

notifications = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
notifications.click()

driver.get(f'https://www.instagram.com/{ACCOUNT}')

followers = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')))
followers.click()


for i in range(2):
    try:
        followers_popup = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')))  
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers_popup)
        time.sleep(2)
    except TimeoutException:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pop_content"]/div[1]/div[3]/div[1]/label[2]/input'))).click()

    
for account in driver.find_elements(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div/div[3]/div/button'):
    try:
        delay = random.uniform(1.5, 3.5)
        account.click()
        time.sleep(delay)
    # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
        cancel_button.click()