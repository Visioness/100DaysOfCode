from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

URL = 'https://orteil.dashnet.org/experiments/cookie/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


upgrade_names = ['Cursor', 'Grandma', 'Factory', 'Mine', 'Shipment', 'Alchemy lab', 'Portal', 'Time machine']


cookie = driver.find_element(By.ID, value='cookie')
#cookie_count = int(driver.find_element(By.ID, value='money').text)

timeout = time.time() + 5
game_over = time.time() + 60*15

while True:
    cookie.click()

    if time.time() > timeout:
        for n in range(len(upgrade_names) - 1, -1, -1):
            try:
                if int(driver.find_element(By.ID, value='money').text.replace(',', '')) > int(driver.find_element(By.CSS_SELECTOR, value=f'[id*="buy{upgrade_names[n]}"] b').text.split()[-1].replace(',', '')):
                    driver.find_element(By.ID, value=f'buy{upgrade_names[n]}').click()
                    time.sleep(0.015)
                    #cookie_count = int(driver.find_element(By.ID, value='money').text)

            except ValueError:
                print(f'Value error while upgrading {upgrade_names[n]}')
                print(driver.find_element(By.CSS_SELECTOR, value=f'[id*="buy{upgrade_names[n]}"] b').text)
                continue
        timeout = time.time() + 15

    #if time.time() > game_over:
    #    print(driver.find_element(By.ID, value='cps').text)
    #    break
