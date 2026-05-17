import selenium
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("abc123@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("gokul")
#xpath--> //tagname[@attribute='value']
#css--> tagname[attribute='value']
#static dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert"success" in message









time.sleep(5)