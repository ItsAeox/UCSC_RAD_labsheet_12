from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://google.com")
name_in = driver.find_element(By.LINK_TEXT, "q")
name_in.send_keys("selenium webdriver")
time.sleep(3)
log_link = driver.find_element(By.NAME, "btnK")
log_link.click()
driver.close()
print("sample test case successfully completed")