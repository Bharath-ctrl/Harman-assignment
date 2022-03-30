from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
print("test case started")
driver.get("https://www.amazon.in")
driver.find_element_by_id("twotabsearchtextbox").send_keys("Men's Watch")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(3)
driver.find_element_by_partial_link_text("2,199").click()
time.sleep(10)
driver.close()
print("test case exited successfully")