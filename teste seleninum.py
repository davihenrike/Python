
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()  

try:

    driver.get("https://jade-bombolone-93cca5.netlify.app/")

    driver.find_element('xpath','//*[@id="menu"]/ul/li[2]/a').click()

    time.sleep(3)

    driver.find_element('xpath','//*[@id="menu"]/ul/li[3]/a').click()

    time.sleep(3)

    driver.find_element('xpath','//*[@id="menu"]/ul/li[4]/a').click()

    time.sleep(3)

    driver.find_element('xpath','//*[@id="menu"]/ul/li[5]/a').click()

    time.sleep(3)
finally:

    driver.quit()
