from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
browsersortedviggies=[]
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#clcick on columreader
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all veg names->veggielist
viggieWebel=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in viggieWebel:
    browsersortedviggies.append(ele.text)
vegoriginal=browsersortedviggies.copy()
#sort this veggielsit->sorted list
browsersortedviggies.sort()
assert browsersortedviggies == vegoriginal
