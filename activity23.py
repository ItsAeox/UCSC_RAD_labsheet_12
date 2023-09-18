from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
import time
service = FirefoxService(log_output="geckodriver.log")
driver = webdriver.Firefox(service=service)
driver.get("https://www.saucedemo.com/")
nameInput=driver.find_element(By.ID,"user-name")
nameInput.send_keys("standard_user")
passwordInput=driver.find_element(By.ID,"password")
passwordInput.send_keys("secret_sauce")
login_button=driver.find_element(By.ID,"login-button")
time.sleep(3)
login_button.click()

select_sort = driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
select_sort.click()
sort_option = driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]")
sort_option.click()
time.sleep(3)
product_name = "Sauce Labs Bike Light"
product_xpath = f"//div[@class='inventory_item_name' and text()='{product_name}']"
product_element = driver.find_element(By.XPATH, product_xpath)
product_element.click()
time.sleep(2)
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()
wait = WebDriverWait(driver, 10)
cart_item_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")))

if cart_item_element:
    print(f"{product_name} is in the cart.")
else:
    print(f"{product_name} is not in the cart.")

time.sleep(3)

driver.close()
print("sample test case successfully completed")

