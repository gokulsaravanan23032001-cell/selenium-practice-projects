from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time
driver =webdriver.Chrome()
driver.get("https://www.google.com")
name="gokul"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
alerttxt = alert.text
print(alerttxt)
assert name in alerttxt
alert.accept()
#alert.dismiss()


time.sleep(2)