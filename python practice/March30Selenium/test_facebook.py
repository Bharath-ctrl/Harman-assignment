import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("@gmail.com")
time.sleep(1)
driver.find_element_by_name("pass").send_keys("***********")
time.sleep(5)

driver.find_element_by_name("login").send_keys(Keys.ENTER)
time.sleep(10)

driver.close()
print("Testcase completed")

