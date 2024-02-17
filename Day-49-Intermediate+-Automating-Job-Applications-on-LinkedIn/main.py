import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from dotenv import load_dotenv
import time

load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')
URL = 'https://www.linkedin.com/jobs'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

email_adress = driver.find_element(By.ID, value='session_key')
email_password = driver.find_element(By.ID, value='session_password')
sign_in_button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

# Signing In
email_adress.send_keys(os.environ.get('LINKEDIN_EMAIL'))
email_password.send_keys(os.environ.get('LINKEDIN_PASSWORD'))
sign_in_button.click()

# Searching Python Related Jobs
jobs = driver.find_element(By.CSS_SELECTOR, value='#global-nav > div > nav > ul > li:nth-child(3) > a')
jobs.click()

time.sleep(2)
ember_id = int(driver.find_element(By.CSS_SELECTOR, value='#global-nav-search > div > div').get_attribute('id').lstrip('ember'))
print(ember_id - 1)
search_keyword = driver.find_element(By.CSS_SELECTOR, value=f'#jobs-search-box-keyword-id-ember{ember_id - 1}')
location_keyword = driver.find_element(By.CSS_SELECTOR, value=f'#jobs-search-box-location-id-ember{ember_id - 1}')

location_keyword.send_keys('Worldwide')
search_keyword.send_keys('python', Keys.ENTER)

#experience_filter = driver.find_element(By.CSS_SELECTOR, value='#search-reusables__filters-bar > ul > li:nth-child(4) > div')
#experience_filter_one = driver.find_element(By.XPATH, value='//*[@id="artdeco-hoverable-artdeco-gen-49"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label')
#experience_filter_two = driver.find_element(By.XPATH, value='//*[@id="artdeco-hoverable-artdeco-gen-49"]/div[1]/div/form/fieldset/div[1]/ul/li[2]/label')
#experience_filter_showresult = driver.find_element(By.CSS_SELECTOR, value='#ember433')
#easy_apply_filter = driver.find_element(By.CSS_SELECTOR, value='#search-reusables__filters-bar > ul > li:nth-child(7) > div')

time.sleep(2)
#experience_filter.click()
#experience_filter_one.click()
#experience_filter_two.click()
#experience_filter_showresult.click()
#easy_apply_filter.click()




