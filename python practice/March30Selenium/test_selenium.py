import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("harman")
time.sleep(10)

driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(10)

driver.close()
print("Testcase completed")

