from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
product = "https://www.amazon.com.tr/Apple-%C3%A7ipli-model-MacBook-laptop/dp/B0C75QJDYY?ref_=ast_sto_dp&th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")


#-#-#-# >>>>> | Amazon Price Tracker | <<<<< #-#-#-#

#price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
#price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
#print(f"The price is {price_whole}.{price_fraction}")


#-#-#-# >>>>> | Different Methods For Getting The Element | <<<<< #-#-#-#

#search_box = driver.find_element(By.ID, value="twotabsearchtextbox")
#search_box = driver.find_element(By.XPATH, value='//*[@id="twotabsearchtextbox"]')
#
#print(search_box.text)
#print(search_box.tag_name)
#print(search_box.get_attribute("placeholder"))

event_dates_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li time")
event_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li a")


events = {}
for n in range(len(event_list)):
    events[n] = {
        "name": event_list[n].text,
        "date": event_dates_list[n].text,
        "link": event_list[n].get_attribute("href"),
    }
pp.pprint(events)


#driver.close()
driver.quit()