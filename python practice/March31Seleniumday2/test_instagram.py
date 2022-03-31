from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
import time

username=input("Username: ")
password=input("Password: ")
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.instagram.com")
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_class_name("L3NKy").click()
time.sleep(10)
driver.close()