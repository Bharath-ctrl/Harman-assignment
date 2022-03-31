from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture()
def setUp():
    global moviename,year,dir_name,distr_name,pro_name,driver
    moviename=input("enter the Movie name: ")
    year=input("Enter the year of release: ")
    dir_name=input("enter the director name: ")
    distr_name=input("enter the distributor name: ")
    pro_name= input("enter the producer name : ")


    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(2)
    driver.close()
def test_movieform(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(2)

    driver.find_element_by_name("mname").send_keys(moviename)
    time.sleep(2)

    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(2)

    driver.find_element_by_name("mdirector").send_keys(dir_name)
    time.sleep(2)

    driver.find_element_by_name("mdist").send_keys(distr_name)
    time.sleep(2)

    driver.find_element_by_name("mproducer").send_keys(pro_name)
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[5]").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(6)
