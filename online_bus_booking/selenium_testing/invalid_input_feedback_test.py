import unittest
import os
import re
os.environ["PATH"] += os.pathsep + r'C:\Users\inamd\Downloads\chromedriver_win32'
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys


class Login(unittest.TestCase):

    driver=wd.Chrome()

    def test_no_ratings(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login")
        driver.find_element_by_name("username").send_keys("xyz")
        driver.find_element_by_name("password").send_keys("abcd6796")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.get("http://127.0.0.1:8000/feedBack/")
        elem = driver.find_element_by_name("email")         
        elem.send_keys("inamdaraakarsh@gmail.com")
        elem.send_keys(Keys.RETURN)
        assert "No Ratings given." in driver.page_source

    def test_invalid_ratings(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login")
        driver.find_element_by_name("username").send_keys("xyz")
        driver.find_element_by_name("password").send_keys("abcd6796")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.get("http://127.0.0.1:8000/feedBack/")
        driver.find_element_by_name("email").send_keys("inamdaraakarsh@gmail.com")
        driver.find_element_by_name("ratings").send_keys("6")
        driver.find_element_by_name("suggestions").send_keys("Good Website")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Invalid Ratings given." in driver.page_source

    def test_invalid_ratings2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login")
        driver.find_element_by_name("username").send_keys("xyz")
        driver.find_element_by_name("password").send_keys("abcd6796")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.get("http://127.0.0.1:8000/feedBack/")
        driver.find_element_by_name("email").send_keys("inamdaraakarsh@gmail.com")
        driver.find_element_by_name("ratings").send_keys("-1")
        driver.find_element_by_name("suggestions").send_keys("Good Website")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Invalid Ratings given." in driver.page_source

    def test_invalid_ratings3(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login")
        driver.find_element_by_name("username").send_keys("xyz")
        driver.find_element_by_name("password").send_keys("abcd6796")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        driver.get("http://127.0.0.1:8000/feedBack/")
        driver.find_element_by_name("email").send_keys("inamdaraakarsh@gmail.com")
        driver.find_element_by_name("ratings").send_keys("dfad")
        driver.find_element_by_name("suggestions").send_keys("Good Website")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Invalid Ratings given.It should be from 1 to 5" in driver.page_source


if __name__ == '__main__':
    unittest.main()