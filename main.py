from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys("iphones")
driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']").click()
list = driver.find_elements(By.XPATH, "//span[@class = 'a-size-medium a-color-base a-text-normal']")
print(str(len(list))+' products found')

for i in list:
    print(i.text)

driver.quit()