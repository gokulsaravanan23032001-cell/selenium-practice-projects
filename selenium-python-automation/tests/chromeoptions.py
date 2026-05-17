from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
chrome_options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)