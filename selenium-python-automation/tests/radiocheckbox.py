from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time
driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radios=driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio in radios:
    if radio.get_attribute("value")== "radio3":
        radio.click()
        assert radio.is_selected()
        break

time.sleep(5)