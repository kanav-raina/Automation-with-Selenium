import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("/home/kanav/Downloads/automation/chromedriver")
driver.get("https://google.com")

#Locate the search box element
search_box=driver.find_element_by_name("q")
time.sleep(5)

#type in your search query into the search box
search_box.send_keys("seleniumhq"+Keys.RETURN)

time.sleep(10)
print(driver.title)
driver.close()
