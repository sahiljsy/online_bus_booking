import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/sahiljariwala/Desktop/SEM_4/SEPP/lab/selenium/chromedriver_linux64/chromedriver")

#test for invalid details of login
    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_name("username")
        elem.send_keys("jsyyy")
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("password")
        elem.send_keys("abcd6796")
        elem.send_keys(Keys.RETURN)
        assert "Invalid details of login" in driver.page_source


if __name__ == '__main__':
    unittest.main()
