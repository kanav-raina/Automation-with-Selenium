import time
from selenium import webdriver

driver=webdriver.Chrome('/home/kanav/Downloads/automation/chromedriver')
driver.get("https://www.smvdu.ac.in/")

print(driver.title)

time.sleep(20)
driver.close()
