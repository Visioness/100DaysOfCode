from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')


URL = 'https://en.wikipedia.org/wiki/Main_Page'
URL2 = 'https://secure-retreat-92358.herokuapp.com/'
XPATH = '//*[@id="articlecount"]/a[1]'
MY_EMAIL = os.environ.get('MY_EMAIL')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL2)

#article_count = driver.find_element(By.XPATH, value=XPATH)
#print(article_count.text)

fname = driver.find_element(By.NAME, value='fName')
lname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.CLASS_NAME, value='btn-primary')

fname.send_keys('Aygun Servet')
lname.send_keys('Zurnaci')
email.send_keys(MY_EMAIL)
button.click()

