import os
import re
os.environ["PATH"] += os.pathsep + r'C:\Users\inamd\Downloads\chromedriver_win32'
from selenium import webdriver as wd

driver=wd.Chrome()
driver.get("http://127.0.0.1:8000/login")
driver.find_element_by_name("username").send_keys("xyz")
driver.find_element_by_name("password").send_keys("abcd6796")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.get("http://127.0.0.1:8000/feedBack/")
driver.find_element_by_name("email").send_keys("inamdaraakarsh@gmail.com")
driver.find_element_by_name("ratings").send_keys("3")
driver.find_element_by_name("suggestions").send_keys("Good Website")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.get("http://127.0.0.1:8000/feedBack/ViewFeedBack/")