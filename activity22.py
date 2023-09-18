from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time
service = FirefoxService(log_output="geckodriver.log")
driver = webdriver.Firefox(service=service)
driver.get("https://technotrail.site/register")
reg_link = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[5]/button")
reg_link.click()
time.sleep(3)
nameInput=driver.find_element(By.ID,"name")
nameInput.send_keys("Gayathra")
emailInput=driver.find_element(By.ID,"email")
emailInput.send_keys("gayathradissa@mail.com")
passwordInput=driver.find_element(By.ID,"password")
passwordInput.send_keys("randompassword")
passwordconfirmInput=driver.find_element(By.ID,"password_confirmation")
passwordconfirmInput.send_keys("randompassword")

register = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/div[5]/button")
reg_link.click()

driver.close()
print("sample test case successfully completed")

